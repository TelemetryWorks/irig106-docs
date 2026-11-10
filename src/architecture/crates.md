# Repository and crate boundaries

The ecosystem consists of separate repositories, not one implemented Cargo
workspace. Some repositories have internal workspaces. The
[verified snapshot](../implementation.md) links the exact manifests and entry
points inspected; the [coverage map](../coverage.md) records ownership decisions.

| Repository | Intended responsibility | Observed state on 2026-11-10 |
| --- | --- | --- |
| `irig106-types` | Shared format identifiers and wire values | Template library; shared types not exported |
| `irig106-core` | Packet structure and traversal | Template library |
| `irig106-decode` | Payload bodies, including MIL-STD-1553 and PCM | Template library |
| `irig106-tmats` | Setup metadata, validation, configuration context | Retired prototype plus rebuild design |
| `irig106-time` | Time decoding, correlation, interpretation basis | Prototype plus rebuild design; sibling dependency gap |
| `irig106-write` | Packet and recording serialization | Template library |
| `irig106-index` | Index construction and queries | Template library |
| `irig106-cli` | Future diagnostic and workflow commands | Development-notice executable |
| `irig106-ch10-reader` | Narrow structural file inspection | Parser and CLI source; Windows-only supported executable target |
| `irig106-studio` | Visualization and analysis application | UI and internal Rust modules; integration remains incomplete |

MIL-STD-1553 decoding belongs to `irig106-decode` in the adopted map. There is no
separate `irig106-1553` crate established by the inspected ecosystem sources.

## Dependency boundaries still to reconcile

- `irig106-time` asks for `irig106-types` version `0.1` at a sibling path and
  forwards its `std` and `serde` features. The pushed types crate is `0.0.1`,
  exports only the template function, and declares neither feature. A standalone
  time checkout is therefore not a reproducible integration setup.
- TMATS's shared-types dependency is commented out; its prototype keeps bridge
  types internally. Its rebuild contract, rather than the older integration
  specification's examples, should guide the next shared interface review.
- Studio's internal core manifest comments out ecosystem integrations. Its
  implementation plan explicitly waits for an external domain core. Existing
  module names and UI demonstrations do not prove that integration is complete.
- The reader depends on `memmap2`; its manifest does not wire in TMATS, time, or
  the future scanner. It is a separate inspection implementation today.

These are source observations, not fresh build failures. Resolve shared values,
version/feature compatibility, and contract ownership before documenting a
cross-crate Cargo example as runnable.
