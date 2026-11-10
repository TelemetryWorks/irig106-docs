# History and direction

TelemetryWorks is organizing IRIG 106 work around separate responsibilities:
packet structure, setup metadata, time interpretation, payload decoding, and
applications. The [coverage map](coverage.md) records the owner's September 2026
allocation of chapters and rebuild decisions. The
[implementation snapshot](implementation.md) records the narrower pushed state.

The earlier book draft described this direction as a finished replacement for
C parsers. That claim was not supported by implementation or comparative
measurements. Language choice alone does not determine copying, allocation,
traversal cost, or throughput: C can expose borrowed buffers, and Rust programs
can allocate and copy. A comparison would need pinned implementations, equivalent
validation and decoding work, representative recordings, hardware details, and
reproducible measurements.

The intended benefit of separating traversal from interpretation is that an
application can reject unneeded packets before decoding their payloads. Whether
that saves meaningful time depends on the workload. No ecosystem-wide speedup,
SIMD implementation, or end-to-end zero-copy guarantee is established here.

The historical requirements retained in the coverage map, including throughput
and test-coverage targets, remain requirements rather than measured results.
The retired prototype research informs future work; it is not evidence that its
features have shipped in the current repositories.
