# IRIG 106 coverage map

> **Status: adopted by the project owner, 2026-09-26.** This page accounts
> for every chapter of IRIG 106 (106-24R1, January 2025, the current
> edition): which crate of the ecosystem owns it, which document describes
> what that crate gives the others, or why the chapter is out of scope. The
> archived standard, with original URLs and checksums, is in
> `TelemetryWorks/rcc-106-standards`.

## How the standard is covered

- **One contract document per repository**, for the chapters it owns,
  written like `irig106-tmats`'s `docs/TMATS-IN-CHAPTER-10.md`: what the crate
  is for, where it sits in Chapter 10 processing, the questions it answers,
  a contract per consumer, what happens when the data are missing or wrong,
  a worked example from the standard, and what changes as a result.
- **This map**, the one place that shows the whole standard is accounted
  for. A chapter marked out of scope keeps its reason, so nothing is
  silently ignored.

## Chapters

| Chapter | Title | Owner | Priority | Contract document |
|---------|-------|-------|----------|-------------------|
| 1 | Introduction | `irig106-docs` (terms; this map) | — | this book |
| 2 | Transmitter and Receiver Systems | out of scope: radio equipment; TMATS's T group describes it | — | — |
| 3 | Frequency Division Multiplexing Telemetry Standards | out of scope: TMATS's M group describes subcarriers | — | — |
| 4 | Pulse Code Modulation Standards | `irig106-decode` (PCM frames, which TMATS's P group describes) | high | to be written |
| 5 | Digitized Audio Telemetry Standard | `irig106-decode` | **very low** — kept in scope at the owner's request, after everything else | to be written |
| 6 | Recorder & Reproducer Command and Control | `irig106-tmats` for §6.2.3.11 (the `.TMATS` command and the `G\SHA` digest); the rest out of scope unless a recorder-control crate is started | — | `irig106-tmats` `docs/TMATS-IN-CHAPTER-10.md` |
| 7 | Packet Telemetry Downlink | `irig106-decode` (Chapter 7 formats, which `P-d\C7` describes) | medium | to be written |
| 8 | Digital Data Bus Acquisition Formatting Standard | `irig106-decode` (bus data in PCM, which TMATS's B group describes) | high | to be written |
| 9 | Telemetry Attributes Transfer Standard | `irig106-tmats` | — | `irig106-tmats` `docs/TMATS-IN-CHAPTER-10.md` |
| 10 | Digital Recording Standards | `irig106-core` (reading recording files), `irig106-write` (writing them) | high | to be written |
| 11 | Recorder Data Packet Format Standard | `irig106-core` (packet structure), `irig106-decode` (data-type bodies), `irig106-time` (time packets), `irig106-tmats` (setup-record packets) | high | per crate |
| 12 | Randomization Methods for Telemetry Systems | `irig106-decode` (derandomising, which `P-d\D7` and `P-d\D8` describe) | medium | to be written |
| 21–28 | Telemetry Network Standard (TmNS) | out of scope for now (below) | — | — |
| Annexes A.1–A.4 | Pulse amplitude modulation; magnetic tape recorders; ADARIO; ARMOR | out of scope | — | — |

## Order of the contract documents

1. **`irig106-time`** — next (owner, 2026-09-26): Chapter 11's time packets
   and the time attributes TMATS supplies; expected to be the simplest.
2. **`irig106-decode`** — Chapters 4, 7, 8, 12 (and 5, last), and Chapter
   11's data-type bodies; the largest consumer of the TMATS description.
3. **`irig106-core`** — Chapter 10 recording files and Chapter 11's packet
   structure.
4. **`irig106-write`** — writing Chapter 10 recordings.

`irig106-tmats`'s document exists. The tools that own no chapter
(`irig106-ch10-reader`, `irig106-studio`, `irig106-index`, `irig106-cli`)
consume the others; their contracts are in the owning crates' documents.

## The Telemetry Network Standard (Chapters 21–28)

Chapters 1–12 describe telemetry sent over a one-way link and recorded as
Chapter 10 files. Chapters 21–28 describe telemetry over IP networks: "The
TmNS approach leverages existing standardized Internet protocols"
(Chapter 21), adding two-way communication so that measurements can be
requested from the test article in real time, and it aims "to enhance,
rather than replace, today's telemetry systems". Its chapters: 22,
network protocols; 23, metadata configuration; 24, message formats; 25,
management resources; 26, data message transfer; 27 and 28, the RF network.

No crate of the ecosystem handles network telemetry, and no current need
calls for it, so the chapters are out of scope for now. Two notes keep the
door open:

- **Chapter 23 is TmNS's counterpart of TMATS.** It defines the Metadata
  Description Language (MDL), which describes "the configuration of the
  components in a telemetry system, as well as their logical and physical
  interrelationships". If the ecosystem takes up TmNS, an MDL crate would
  be a sibling of `irig106-tmats`.
- **MDL reuses TMATS's XML schema.** "The MDL schema requires the
  tmatsP:PCMFormatAttributesType to describe pulse code modulation … The
  TMATS schema files are included with the MDL schema" (Chapter 23
  §23.2.1.6).
  `irig106-tmats` has deferred XML TMATS (its ADR-0015); when that support
  is designed, it should be built so that an MDL crate could reuse it.

## Open points

- The draft `src/architecture/overview.md` names a crate `irig106-1553`
  for 1553 decoding; this map assigns bus data to `irig106-decode`. One of
  the two should change.
