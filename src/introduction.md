# The TelemetryWorks IRIG 106 ecosystem

This book introduces the repositories, responsibilities, and intended processing
model for TelemetryWorks telemetry tools. It is an integration guide in progress,
not a claim that the full ecosystem is implemented or compliant.

Start with the [coverage map](coverage.md) for the owner's allocation of standard
chapters, then the [verified implementation snapshot](implementation.md) for what
was actually present on GitHub on **2026-11-10**. The architecture chapters explain
the intended boundaries; the usage chapters distinguish an existing inspection
tool from future integration work.

## Terms and scope

- **Chapter 10 recording:** the recording-file context. In newer editions the
  recorder packet format is in Chapter 11; the common name “Chapter 10 file”
  remains useful, but citations must identify the edition and chapter.
- **Packet:** a header and data body, with optional fields and checksums governed
  by its format. Finding a packet boundary does not decode its measurements.
- **TMATS:** Chapter 9 setup metadata describing telemetry configuration. A
  channel's payload bytes alone may not identify how to interpret measurements.
- **RTC:** the relative time counter. Converting it to absolute time requires a
  time reference and a stated interpretation policy.
- **CSDW:** a channel-specific data word; its meaning depends on the data type
  and format. It is not a universal payload header.
- **TmNS:** the Telemetry Network Standard, Chapters 21–28, outside the adopted
  ecosystem scope for now. Chapter 10 UDP transport is a separate proposed task.

The historical coverage baseline is **106-24R1 (January 2025)**. For exact layouts,
use an edition-specific citation and the provenance-preserving
[standards archive](https://github.com/TelemetryWorks/rcc-106-standards/tree/d0af2e9cc9ff0c3bb012465a46f55de6de88c682).
This book is not a replacement for the standard.

## How to read status statements

**Observed** means source or manifests were inspected at the pinned commits in
the snapshot. It does not mean the sibling was built, tested, benchmarked, or
verified against real recordings. **Historical** means a dated owner decision or
check recorded in the inherited coverage work. **Proposed** means a design or
workflow whose implementation still needs review and verification.

In particular, neither a repository name nor a README feature list establishes a
working API. The TMATS and time READMEs explicitly label their code as prototypes
with known standard disagreements. Follow their current contract documents for
design discussions, not their old examples as a supported integration recipe.
