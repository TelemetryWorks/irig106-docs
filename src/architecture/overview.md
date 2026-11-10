# A Layered, Zero-Copy Engine 

To achieve maximum throughput and support both live streaming and massive offline analytics, this project abandons the monolithic parser in favor of a layered, agent-friendly packet engine.  

Our core architectural principles are:  

## 1. Separation of Traversal and Interpretation
The most critical hot path in Chapter 10 processing is not semantic decoding; it is byte traversal, header parsing, checksum validation, and dispatch. Our architecture isolates this into a distinct Scanner Layer. This layer walks the file or stream, rapidly identifying packet boundaries and yielding metadata without touching the payload. By decoupling the scanner, we open the door to High-Performance Computing (HPC) techniques, including utilizing SIMD instructions to accelerate sync-word searching and checksum validations across large memory-mapped buffers.

## 2. Zero-Copy Typed Views
Instead of eagerly allocating structs and copying data (as is common in C), this library leverages Rust's ownership and borrowing model to provide zero-copy views over raw &[u8] slices.  
* A `PacketHeaderView<'a>` simply maps to the bytes of the header.
* A `Mil1553PacketView<'a>` provides accessor methods to the underlying bytes without moving them.
Allocations only occur when the user explicitly requests an owned, normalized export of the data. This drastically reduces memory pressure and keeps the hot path cache-friendly.  

## 3. Multi-Crate Modularity
The Chapter 10 standard is vast. Rather than shipping a single, bloated crate, this project is structured as a Cargo workspace.  
* `irig106-core`: Contains the high-speed scanner, base traits, and header definitions.
* `irig106-1553`: Specific decoding logic for 1553 data.
* `irig106-tmats`: Parsing and querying for TMATS setup records.
This allows consumers to pull in exactly what they need, reducing compile times and binary bloat for specialized applications, such as a lightweight UDP listener.  

## 4. Agnostic I/O
The library does not dictate how data is ingested. By operating strictly on byte slices and generic `Read` traits, the core engine seamlessly supports both `mmap` backed file reads for lightning-fast offline indexing, and streaming adapters for live RTPS/UDP network ingestion.  

