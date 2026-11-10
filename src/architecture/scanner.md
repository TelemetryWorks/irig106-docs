# The Scanner Layer: Fast Traversal & SIMD Optimization

In a traditional Chapter 10 processing pipeline, the bottleneck rarely lies in decoding the payload itself. Instead, the CPU spends the vast majority of its cycles simply hunting for packets, validating headers, and calculating checksums. When dealing with terabyte-scale data lakes or high-throughput live streams, a naive byte-by-byte traversal is insufficient.  
The Scanner Layer is the vanguard of this Rust engine. Its sole responsibility is to locate valid Chapter 10 packets within a byte stream as quickly as the hardware allows, without performing any semantic interpretation of the payload.  

## The Anatomy of the Hunt: `0xEB25`

Every standard IRIG 106 Chapter 10 packet begins with a ubiquitous 16-bit sync pattern: `0xEB25`.  
  
In legacy implementations, finding the next packet often involved reading two bytes, checking the pattern, and if it failed, advancing the pointer by one byte and trying again. This serial, scalar approach guarantees cache misses and poor branch prediction.  
  
Our scanner reimagines this search by treating it as a vector math problem, leveraging Single Instruction, Multiple Data (SIMD) capabilities available on modern ISAs (like AVX-2/AVX-512 on x86_64, or NEON on ARM64).  
  
## Vectorized Sync Searching

Instead of inspecting two bytes at a time, the scanner loads chunks of the data stream (e.g., 32 or 64 bytes) directly into wide CPU registers. Using Rust's `core::arch` or portable `std::simd` intrinsics, we broadcast the `0xEB25` pattern across a parallel register and perform a vectorized equality comparison in a single clock cycle.  
  
Conceptually, the fast path looks like this:  
1. **Load**: Pull 32 bytes of the `&[u8]` stream into a 256-bit vector.
2. **Compare**: Execute a vectorized byte-match against the sync pattern.
3. **Bitmask**: Reduce the vector comparison result to a single bitmask integer.
4. **Trailing Zeros**: Use hardware instructions (like `tzcnt`) to instantly find the exact byte offset of the next potential sync word.
If the vector contains no matches, the scanner jumps forward by 32 bytes instantly. This allows the scanner to skip over massive payloads (like raw video or high-rate PCM) at memory bandwidth speeds.  
  
## The Traversal State Machine

Finding `0xEB25` is only the first step, as false positives can naturally occur within payload data. The scanner operates as a highly optimized state machine:
1. **Hunt**: Use SIMD to find the next `0xEB25`.
2. **Header Validation**: Once a sync word is found, the scanner casts the immediate following bytes into a zero-copy `PacketHeaderView`.
3. **Checksum Verification**: The scanner calculates the header checksum. If the checksum fails, the sync word was a false positive; the scanner advances by one byte and returns to the **Hunt** state.
4. **Secondary Header Check (Optional)**: If the secondary header bit is set, the secondary header checksum is validated.
5. **Yield & Skip**: Once validated, the scanner yields the packet metadata (offset, total length, data type) to the caller. It then uses the `Packet Length` field from the header to instantly advance its internal pointer past the payload, ready to hunt for the next packet.  
  
## Designed for Zero-Copy
  
The scanner does not return allocated Packet structs. It yields lightweight descriptors—essentially a `(usize, usize)` representing the start and end indices of the packet within the buffer, alongside the minimal routing fields (Channel ID, Data Type).  
  
This design allows upstream consumers, such as an indexing worker or a specialized UDP listener, to blast through a data stream at gigabytes per second, selectively constructing zero-copy views only when a specific packet matches the user's filter criteria.  
