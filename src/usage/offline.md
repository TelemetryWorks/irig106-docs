# Offline inspection

## Available source-backed workflow

`irig106-ch10-reader` contains a structural inspection CLI named `ch10r`. Its
[pinned README](https://github.com/TelemetryWorks/irig106-ch10-reader/blob/f1a747401c6ef005d52e863a0de281c036bb872e/README.md)
supports **Windows only** as an executable target for version 0.1.2; Linux and
macOS guides are future-support placeholders. Its
[CLI source](https://github.com/TelemetryWorks/irig106-ch10-reader/blob/f1a747401c6ef005d52e863a0de281c036bb872e/src/lib.rs)
implements the following invocation shapes. These commands are for an existing
reader checkout with its prerequisites installed, **not this documentation
repository**, and were not executed during the book's source review:

```powershell
cargo build --release --jobs 2
.\target\release\ch10r.exe --help
.\target\release\ch10r.exe C:\recordings\sample.ch10
.\target\release\ch10r.exe C:\recordings\sample.ch10 --packets --limit 100
```

Replace the sample path with a recording you may inspect. Keep a stable,
read-only input while the reader holds a file mapping. The reader summarizes
channels, data types, counts, and bytes, reports primary-header checksum and
sequence issues, and attempts sync recovery. A summary or presence check for
setup records is not full TMATS validation or payload decoding. A structurally
readable file is not thereby certified compliant.

## Proposed integrated workflow

A future offline application would scan packet structure, collect setup and time
context, select packets by channel/type, decode supported bodies, and retain
provenance with its results. Indexing could accelerate repeated queries; mapping
or buffered I/O would be an application choice. None of that establishes a
working `irig106-core`/`irig106-index` integration today.

Before adopting such a workflow, resolve the [dependency gaps](../architecture/crates.md),
choose explicit edition and time policies, and verify representative fixtures.
The time and TMATS prototypes have documented correctness defects; their old
examples should not be used as an authoritative analysis recipe. Studio includes
a UI and Rust code, but its README and plan describe mock/stub integration; a
visible panel is not proof that the final domain engine is connected.
