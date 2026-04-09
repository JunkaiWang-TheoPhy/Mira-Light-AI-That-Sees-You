# Release Baseline

## Purpose

This document defines the current Git-ready release baseline inside the main Mira repository.

It does not mean the repo is feature-complete.

It means the current structure is stable enough to be treated as the first public release assembly baseline from which a future standalone package can be exported.

## Baseline Scope

The current baseline includes:

- top-level release portal and documentation shell
- `core/` with release-safe persona, workspace, config, and the first core plugin package
- `modules/home-assistant/` with registry examples, scene planning skeletons, and module docs
- `services/notification-router/` with a runnable first-pass source package
- `examples/` with `minimal-core`, `home-stack`, `service-notification-router`, and combined path docs
- `deploy/` with matching operator-facing paths
- `docs/migration/source-to-release-mapping.md`
- imported `migration-bundles/` as copied context for later split and export work

## Baseline Exclusions

The current baseline explicitly excludes:

- live secrets and provider credentials
- installed `node_modules/`
- local `.env` files
- devbox runtime state
- session logs and dated working-memory logs
- transport-specific glue that is not yet release-safe

## Baseline Entry Documents

Start here:

- [../../README.md](../../README.md)
- [../../readme/00-overview/getting-started.md](../../readme/00-overview/getting-started.md)
- [source-to-release-mapping.md](./source-to-release-mapping.md)

## Git Baseline Rules

To keep this baseline stable:

- add release-safe files only
- update mapping docs when source boundaries change
- prefer `.example` and template files over live config
- keep `core`, `modules`, `services`, and `deploy` boundaries explicit
- keep `migration-bundles/` as copied reference material rather than a runtime dependency

## Next Stabilization Targets

The next pieces that still need more convergence are:

- top-level README, `readme/`, and migration-doc wording unification
- `modules/home-assistant/plugin/` packaging and runtime contract
- `services/notification-router/` production-facing packaging details
- final split/export checklist validation from the current mainline repo
