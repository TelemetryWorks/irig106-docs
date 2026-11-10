# Architecture: intended layers and present limits

**Proposed ecosystem design.** The [implementation snapshot](../implementation.md)
is the source of current-state claims. The core, decode, write, index, and shared
types repositories are scaffolds at that snapshot; this book does not define
callable APIs for them.

## Separate traversal from interpretation

The intended pipeline is:

```text
file or transport adapter
  -> validated packet boundaries and routing metadata (core)
  -> selected payloads (decode), setup metadata (TMATS), time references (time)
  -> application results, indexes, or authored recordings
```

This is a responsibility diagram, not an implemented dependency graph. Metadata
and time context may have to be collected before a selected payload can be
interpreted. Core traversal should remain independent of TMATS interpretation;
the contracts still need concrete shared types and reviewed error behavior.

## Borrow buffers when practical

Borrowed byte slices and checked accessors are candidates for avoiding payload
copies within a stable buffer. A typed view must validate lengths, byte order,
optional fields, and alignment requirements; a raw cast is not a parsing strategy.
No `PacketHeaderView` or MIL-STD-1553 packet-view API is promised by this book.

Borrowing is local to an ownership boundary. Buffer reuse, packet reassembly,
normalization, worker messages, and foreign-function boundaries can require owned
storage. “Zero-copy” should describe a measured operation with stated lifetimes,
not the entire ecosystem.

## Keep I/O and domain logic distinct

Offline mappings and streaming buffers could feed the same structural parser
once a parser contract exists. Transport adapters would own buffering and framing;
semantic libraries would receive explicit bytes and context. The existing reader
uses a file mapping, but that does not establish a generic streaming API in core.

See [crate boundaries](crates.md), [scanning](scanner.md), and
[decoding](decoders.md) for the responsibilities and unresolved work. SIMD,
parallelism, and indexing are optimization candidates after correctness and
representative benchmarks establish a baseline.
