# irig106-docs

The TelemetryWorks IRIG 106 ecosystem book: chapter ownership, verified repository
state, proposed architecture, and usage boundaries. Start with
[src/introduction.md](src/introduction.md), the [coverage map](src/coverage.md),
and the [implementation snapshot](src/implementation.md).

The book distinguishes dated owner decisions and historical local checks from
pushed implementation. It does not claim all ecosystem libraries are working.

## Build and check

Use the official [mdBook 0.5.4 release](https://github.com/rust-lang/mdBook/releases/tag/v0.5.4)
binary for your OS and CPU architecture and Python 3.11 or newer (standard library
only). No Cargo workspace or sibling checkout is needed for this book.
With `mdbook` on PATH, run from this repository:

```sh
RAYON_NUM_THREADS=2 mdbook build
python3 scripts/check-book.py
git diff --check
```

The checker requires the populated `book/` output. It verifies SUMMARY membership,
nonempty chapters, rendered local links and anchors, README local links, and that
every chapter is in the search index, including the current coverage-map text.
It does not fetch external links or test sibling repositories. There are no Rust
API examples in this book to compile as doctests.

For a local preview, `RAYON_NUM_THREADS=2 mdbook serve --hostname 127.0.0.1` serves
the book at `http://127.0.0.1:3000`; stop it when finished. Building and previewing
do not publish or deploy. Generated `book/` output is ignored by Git.

## Contributing

Keep historical decisions dated. For implementation claims, link the inspected
repository commit and source, and state whether checks were executed or the
source was only read. Label unimplemented workflows as proposals; avoid invented
APIs, unsupported speed claims, and language-based performance comparisons.
Update the snapshot when new source evidence changes a claim. Add every chapter
to `src/SUMMARY.md`, then rebuild and check links before proposing a reviewed PR.
