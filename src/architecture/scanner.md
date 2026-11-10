# Packet scanning

**Current evidence:** `irig106-core` contains only the template library. The
[reader source](https://github.com/TelemetryWorks/irig106-ch10-reader/blob/f1a747401c6ef005d52e863a0de281c036bb872e/src/lib.rs)
contains structural traversal, primary-header checksum computation, bounds
checks, and a bounded scalar recovery search. That code is not evidence of a
SIMD scanner in core, and it has not been executed for this book's snapshot.

## Proposed scanner contract

A scanner should locate packets without requiring semantic payload decoding.
An eventual contract needs to specify at least:

1. Input ownership, accepted editions, and how incomplete input differs from
   malformed input and end of file.
2. Checked packet and data lengths, optional fields, checksum policy, and
   diagnostics carrying offsets and the reason a candidate was rejected.
3. Routing metadata and byte ranges whose lifetimes cannot outlive the buffer.
4. Recovery limits, forward progress, and behavior when a packet is unsupported.

The reader uses sync value `0xEB25`, encoded as bytes `25 EB`. Finding those
bytes identifies a candidate, not a validated packet: the same bytes can occur
inside a payload. After sufficient header bytes arrive, a scanner must check
lengths and the applicable checksums before trusting a skip distance. It must
not read beyond the available buffer or allocate based on an unchecked length.
These are proposed core requirements, not a claim that the reader implements
every one of them.

## SIMD and throughput are proposals

A future implementation could compare multiple bytes at a time during recovery.
It would need a scalar fallback, CPU feature handling, and tests for unaligned
input, buffer tails, cross-chunk sync words, and false positives. Normal traversal
can often advance by validated packet lengths; sync searching and checksumming
are different workloads and need separate measurements.

The earlier draft's single-cycle comparisons, guaranteed cache misses in scalar
code, memory-bandwidth traversal, and gigabytes-per-second throughput were not
backed by code or benchmark evidence. No such guarantee is made here. Profile
representative clean and corrupt recordings before choosing SIMD or parallel
scanning, then report the hardware, data, validation policy, and baseline.
