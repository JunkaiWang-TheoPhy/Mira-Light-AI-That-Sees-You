# Open-Source Readiness Checklist

## Purpose

This checklist tracks whether the current release-ready package surface is clean enough to be copied or exported into a standalone public repository.

## Ready Items

- release-side documentation shell exists
- top-level `LICENSE` now exists and declares AGPL-3.0
- `core/`, `modules/`, `services/`, `examples/`, and `deploy/` all have public entrypoints
- source-to-release mapping is documented
- release-side example config files use `.example` naming
- outbound policy ownership is documented as a release-safe pattern

## Required Checks Before Split

- remove installed dependencies such as `node_modules/`
- remove local environment files
- confirm all runtime examples use placeholder credentials
- confirm the exported tree retains the top-level [LICENSE](../../LICENSE)
- confirm deploy docs do not rely on private devbox paths
- confirm all top-level docs prefer release-side links over prototype-tree links
- confirm package names and README language are public-facing
- confirm `migration-bundles/` is documented as copied context rather than an active runtime dependency
- run the shared release verification entrypoint from [../../package.json](../../package.json)

## Known Remaining Decisions

- release repository name and package namespace normalization
- whether to carry package lockfiles for all release-side packages
- which release-side tests must be copied versus referenced from the active repo

See also:

- [repository-split-readiness.md](./repository-split-readiness.md)
- [package-and-license-decisions.md](./package-and-license-decisions.md)

## Operator Rule

If a file would be unsafe or confusing in a public repository, do not move it into the standalone release package.
