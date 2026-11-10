# Verified implementation snapshot

## Inspection basis: 2026-11-10

This is a read-only source inspection of the GitHub `main` commits below. The
repository trees, READMEs, listed manifests, and entry points were read; additional
contract and roadmap evidence is linked below. These are pinned observations,
not a live status dashboard or an inventory of unpublished local work. No sibling
repository was modified, built, tested, benchmarked, or run. Published-package
availability and current GitHub CI results were not verified.

The reader snapshot was refreshed to merged commit `f1a7474` after review.
Its manifest now declares Rust 1.85; its README and parser source are unchanged
from the earlier inspected reader commit. This refresh is source inspection only,
with no sibling build or test execution by this maintainer.

The [coverage map](coverage.md) preserves the owner's earlier scope and local
checks. Its declarations must not be read as proof that those changes reached
the pushed implementations inspected here.

| Repository and exact inspected head | Source evidence | Observation |
| --- | --- | --- |
| `irig106-types`<br>`8004a4364789b78f898000cf5bcea3d93a538fb2` | [manifest](https://github.com/TelemetryWorks/irig106-types/blob/8004a4364789b78f898000cf5bcea3d93a538fb2/Cargo.toml), [entry point](https://github.com/TelemetryWorks/irig106-types/blob/8004a4364789b78f898000cf5bcea3d93a538fb2/src/lib.rs), [README](https://github.com/TelemetryWorks/irig106-types/blob/8004a4364789b78f898000cf5bcea3d93a538fb2/README.md) | `0.0.1`, edition 2021; no `rust-version`, dependencies, or features. Entry point is only `add` and its template test. |
| `irig106-core`<br>`72923d3627ba9a0ad00b799d402a268e5c1d735f` | [manifest](https://github.com/TelemetryWorks/irig106-core/blob/72923d3627ba9a0ad00b799d402a268e5c1d735f/Cargo.toml), [entry point](https://github.com/TelemetryWorks/irig106-core/blob/72923d3627ba9a0ad00b799d402a268e5c1d735f/src/lib.rs), [README](https://github.com/TelemetryWorks/irig106-core/blob/72923d3627ba9a0ad00b799d402a268e5c1d735f/README.md) | `0.0.1`, edition 2024; no `rust-version` or dependencies. Entry point is only `add` and its template test. |
| `irig106-time`<br>`e315238b1729f7fd2a94a916311c8ee8063da4cf` | [manifest](https://github.com/TelemetryWorks/irig106-time/blob/e315238b1729f7fd2a94a916311c8ee8063da4cf/Cargo.toml), [entry point](https://github.com/TelemetryWorks/irig106-time/blob/e315238b1729f7fd2a94a916311c8ee8063da4cf/src/lib.rs), [README](https://github.com/TelemetryWorks/irig106-time/blob/e315238b1729f7fd2a94a916311c8ee8063da4cf/README.md) | `0.7.0`, edition 2024, Rust 1.85 declared. Prototype modules and rebuild contract exist; sibling types dependency is unresolved (details below). |
| `irig106-decode`<br>`b527b125c16c366afa729b8010c4b901c43a98db` | [manifest](https://github.com/TelemetryWorks/irig106-decode/blob/b527b125c16c366afa729b8010c4b901c43a98db/Cargo.toml), [entry point](https://github.com/TelemetryWorks/irig106-decode/blob/b527b125c16c366afa729b8010c4b901c43a98db/src/lib.rs), [README](https://github.com/TelemetryWorks/irig106-decode/blob/b527b125c16c366afa729b8010c4b901c43a98db/README.md) | `0.0.1`, edition 2024; no `rust-version` or dependencies. Entry point is only `add` and its template test. |
| `irig106-write`<br>`80adbee4d3935ffa9f00376fec68bf60927731d3` | [manifest](https://github.com/TelemetryWorks/irig106-write/blob/80adbee4d3935ffa9f00376fec68bf60927731d3/Cargo.toml), [entry point](https://github.com/TelemetryWorks/irig106-write/blob/80adbee4d3935ffa9f00376fec68bf60927731d3/src/lib.rs), [README](https://github.com/TelemetryWorks/irig106-write/blob/80adbee4d3935ffa9f00376fec68bf60927731d3/README.md) | `0.0.1`, edition 2024; no `rust-version` or dependencies. Entry point is only `add` and its template test. |
| `irig106-index`<br>`e53a9ff9a0ea985dc61232f808c6443db56152e0` | [manifest](https://github.com/TelemetryWorks/irig106-index/blob/e53a9ff9a0ea985dc61232f808c6443db56152e0/Cargo.toml), [entry point](https://github.com/TelemetryWorks/irig106-index/blob/e53a9ff9a0ea985dc61232f808c6443db56152e0/src/lib.rs), [README](https://github.com/TelemetryWorks/irig106-index/blob/e53a9ff9a0ea985dc61232f808c6443db56152e0/README.md) | `0.0.1`, edition 2024; no `rust-version` or dependencies. Entry point is only `add` and its template test. |
| `irig106-cli`<br>`b564797faf1f721aa8ef7b90fd62be0bd8f67450` | [manifest](https://github.com/TelemetryWorks/irig106-cli/blob/b564797faf1f721aa8ef7b90fd62be0bd8f67450/Cargo.toml), [entry point](https://github.com/TelemetryWorks/irig106-cli/blob/b564797faf1f721aa8ef7b90fd62be0bd8f67450/src/main.rs), [README](https://github.com/TelemetryWorks/irig106-cli/blob/b564797faf1f721aa8ef7b90fd62be0bd8f67450/README.md) | `0.0.1`, edition 2024; no `rust-version` or dependencies. Executable prints a development notice. |
| `irig106-ch10-reader`<br>`f1a747401c6ef005d52e863a0de281c036bb872e` | [manifest](https://github.com/TelemetryWorks/irig106-ch10-reader/blob/f1a747401c6ef005d52e863a0de281c036bb872e/Cargo.toml), [entry point](https://github.com/TelemetryWorks/irig106-ch10-reader/blob/f1a747401c6ef005d52e863a0de281c036bb872e/src/lib.rs), [README](https://github.com/TelemetryWorks/irig106-ch10-reader/blob/f1a747401c6ef005d52e863a0de281c036bb872e/README.md) | `0.1.2`, edition 2024, Rust 1.85 declared. Depends on `memmap2`; contains structural parsing and CLI code. README supports Windows only. |
| `irig106-tmats`<br>`54a086691502e206b30b613a06d39cf3760fc402` | [manifest](https://github.com/TelemetryWorks/irig106-tmats/blob/54a086691502e206b30b613a06d39cf3760fc402/Cargo.toml), [entry point](https://github.com/TelemetryWorks/irig106-tmats/blob/54a086691502e206b30b613a06d39cf3760fc402/src/lib.rs), [README](https://github.com/TelemetryWorks/irig106-tmats/blob/54a086691502e206b30b613a06d39cf3760fc402/README.md) | Workspace version `0.1.0`, edition 2024, Rust 1.85 declared. Prototype parser/validator and CLI code coexist with documentation-first rebuild plans. |
| `irig106-studio`<br>`d4d957a6a8a81ef971b75461974d624375de4aed` | [manifest](https://github.com/TelemetryWorks/irig106-studio/blob/d4d957a6a8a81ef971b75461974d624375de4aed/crates/irig106-studio-core/Cargo.toml), [entry point](https://github.com/TelemetryWorks/irig106-studio/blob/d4d957a6a8a81ef971b75461974d624375de4aed/crates/irig106-studio-core/src/lib.rs), [README](https://github.com/TelemetryWorks/irig106-studio/blob/d4d957a6a8a81ef971b75461974d624375de4aed/README.md) | Workspace with UI and internal core/WASM crates. Internal core is edition 2021; ecosystem dependency lines there are commented out. Implementation plan still waits for external core. |
| `rcc-106-standards`<br>`d0af2e9cc9ff0c3bb012465a46f55de6de88c682` | [README](https://github.com/TelemetryWorks/rcc-106-standards/blob/d0af2e9cc9ff0c3bb012465a46f55de6de88c682/README.md) | Manifest, fetch/validation scripts, provenance and audit documentation. Standards documents are release assets, not files in the Git tree. |

## Contracts, prototypes, and dependency gaps

- **Time:** its
  [README warning](https://github.com/TelemetryWorks/irig106-time/blob/e315238b1729f7fd2a94a916311c8ee8063da4cf/README.md)
  identifies known standard disagreements and a planned 0.8.0 rebuild. Its
  [time contract](https://github.com/TelemetryWorks/irig106-time/blob/e315238b1729f7fd2a94a916311c8ee8063da4cf/docs/TIME-IN-CHAPTER-10.md)
  is a design draft; the
  [roadmap](https://github.com/TelemetryWorks/irig106-time/blob/e315238b1729f7fd2a94a916311c8ee8063da4cf/docs/ROADMAP.md)
  distinguishes rebuild planning from prototype code. The manifest requires
  `irig106-types` version `0.1` at `../irig106-types`, forwarding `std` and `serde`.
  The inspected types manifest has version `0.0.1` and neither feature. This is a
  source-visible integration gap; no failing build was executed to rediscover it.
- **TMATS:** its
  [README warning](https://github.com/TelemetryWorks/irig106-tmats/blob/54a086691502e206b30b613a06d39cf3760fc402/README.md)
  marks the implementation as a retired prototype with correctness defects. The
  [setup-record contract](https://github.com/TelemetryWorks/irig106-tmats/blob/54a086691502e206b30b613a06d39cf3760fc402/docs/TMATS-IN-CHAPTER-10.md)
  and [roadmap](https://github.com/TelemetryWorks/irig106-tmats/blob/54a086691502e206b30b613a06d39cf3760fc402/docs/ROADMAP.md)
  describe the rebuild. The older
  [ecosystem integration specification](https://github.com/TelemetryWorks/irig106-tmats/blob/54a086691502e206b30b613a06d39cf3760fc402/docs/FOR_IRIG106_DOCS_REPO.md)
  proposes commands and interfaces that are not established as working integrations;
  it must not be copied into runnable book examples. The prototype still declares
  XML/WASM features, while
  [ADR-0015](https://github.com/TelemetryWorks/irig106-tmats/blob/54a086691502e206b30b613a06d39cf3760fc402/docs/adr/0015-remove-xml-wasm-and-unused-features.md)
  defers that work for the rebuild. Design intent and prototype feature flags differ.
- **Studio:** internal modules and a UI are present, but its
  [README](https://github.com/TelemetryWorks/irig106-studio/blob/d4d957a6a8a81ef971b75461974d624375de4aed/README.md)
  describes mock/stub integration and its
  [WASM implementation plan](https://github.com/TelemetryWorks/irig106-studio/blob/d4d957a6a8a81ef971b75461974d624375de4aed/docs/implementation/06-wasm-integration-and-external-core-pause.md)
  explicitly waits for external core. No full application integration is certified
  here. The historical Rust 1.88 dependency note in the coverage map is retained
  as earlier evidence; the dependency tree was not built or its MSRV retested.

## Review of the inherited coverage commits

All five coverage commits are part of this book PR, even though they predate the
completion work. They were inspected in Git history and their combined text was
reviewed against the source snapshot above. The draft-preservation commit
`43f79ee` was also reviewed; its unsupported architecture and performance claims
have been replaced with qualified proposals.

| Inherited commit | Material retained and review outcome |
| --- | --- |
| `5be80ec` | Owner-adopted chapter allocation, priorities, TmNS exclusion and MDL/XML design note, dated 2026-09-26. These record scope, not decoder availability. The old separate 1553-crate discrepancy is now explicitly resolved in the architecture. |
| `6b7088e` | Time contract drafted in eight sections on 2026-09-27. The contract exists at the inspected GitHub head; it remains a design draft. |
| `79c9fa7` | Time rebuild decision, Rust alignment policy, and RCC 200 archive note retained with their date. Time's README and contract support rebuild status; the archive README lists RCC 200. |
| `4ae9e51` | Rust 1.85 local checks and Studio exception retained as historical local evidence. Current manifests above do not establish uniform pushed declarations; no cloud rerun of these historical checks is claimed. |
| `f29b20a` | Retired-requirements ideas and targets retained as dated provenance. C FFI, UDP streaming, advanced PCM work, coverage and throughput targets are not advertised as shipped features or measurements. |

The inherited chapter quotations and local test claims were not independently
revalidated against standard PDFs or the unavailable local checkout. Their dates
and origin remain visible. Future implementation changes should update this
snapshot with new pinned sources and clearly distinguish executed checks from
inspection. No local work outside this cloud branch is covered by this review.
