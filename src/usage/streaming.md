# Streaming design

**Proposed workflow; no ready-to-run ecosystem ingestion API is verified.**
The [coverage map](../coverage.md) records Chapter 10 UDP streaming as future
work. The time prototype has a streaming correlation module, but a time helper
is not a socket receiver, transport framer, or complete packet pipeline.

A future adapter would receive transport data, apply the chosen transport's
framing rules, and pass complete packet candidates to structural validation.
Do not assume one UDP datagram equals one Chapter 10 packet. Segmentation,
aggregation, sequence handling, and any reassembly must follow the selected
transport specification and have explicit limits.

## Decisions required before implementation

- Bound receive buffers, packet sizes, reassembly state, and queue depth. Define
  timeout, loss, duplication, reordering, and backpressure behavior.
- Distinguish “need more bytes” from corruption. Retain bytes across input chunks
  without exposing borrowed views after their storage is reused.
- Track setup-record changes and time-reference availability. Record missing
  context and the policy used for provisional or delayed answers.
- Preserve source/sequence and byte provenance with diagnostics. Test truncated,
  malformed, lost, and out-of-order inputs as well as a clean stream.

Allocation-free ingestion, fixed latency, and line-rate throughput require
measurement under those policies. They are not guarantees provided by the
current repositories. Start with correctness fixtures and bounded memory, then
measure buffering, framing, scanning, and decoding separately.

TmNS (Chapters 21–28) remains outside the adopted scope. A future Chapter 10 UDP
adapter would not by itself implement TmNS configuration, management, or network
services. Use the [offline reader](offline.md) only for its documented file
inspection task; this book supplies no fictional streaming command or crate API.
