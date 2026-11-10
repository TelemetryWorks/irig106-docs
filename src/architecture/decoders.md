# Payload decoding

**Current state:** `irig106-decode` is a template library, not a collection of
working telemetry decoders. Its assigned scope is in the
[coverage map](../coverage.md); the [snapshot](../implementation.md) pins the
source inspected. Time and TMATS have separate prototype implementations and
rebuild contracts; their existence does not establish a completed decode pipeline.

## Proposed dispatch boundary

A caller would select a decoder using the packet's data type, format, edition,
and channel configuration. A packet boundary alone does not prove a body is
valid. Decoders should check their own CSDWs, counts, lengths, optional fields,
and message boundaries before exposing values.

For a future MIL-STD-1553 workflow, the caller would select the relevant channel,
obtain its applicable setup metadata, decode the supported bus packet format,
and resolve message time with an explicit time policy. The book intentionally
uses prose here: no bus decoder constructor, iterator, or CLI command is verified
in `irig106-decode` today.

## Context and results

The intended separation is structural bytes from core, configuration context
from TMATS, time interpretation from time, and measurement meaning from decode.
A decoder result should retain channel, packet/message location, and findings so
an application can trace each value to its input. Unknown or unsupported formats
should remain distinguishable from malformed supported formats.

Borrowed views may suit inspection while a packet buffer remains alive. Owned
records may be needed for export or asynchronous consumers. Allocation policy,
units, calibration, and missing-metadata behavior need reviewed contracts and
fixtures; they are not supplied by this book as imaginary APIs.

Chapter 5 audio remains very low priority under the recorded owner decision.
Neither advanced PCM decommutation nor all Chapter 11 body formats should be
inferred to be implemented from the crate's name.
