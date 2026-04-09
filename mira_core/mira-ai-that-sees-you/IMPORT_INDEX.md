## Mira-AI-that-sees-you Bulk Import

This directory is a namespaced import of material copied from:

- `/Users/Zhuanz/Documents/Github/Mira-AI-that-sees-you`

Import date:

- `2026-04-09`

Import rules used:

- Kept the original source directory structure under `mira_core/mira-ai-that-sees-you/`
- Excluded `README*` files
- Excluded `readme/`, `Readme/`, and other README-style source content
- Excluded the source repository `.git/` directory
- Avoided merging directly into the target repo's top-level `docs/`, `scripts/`, `deploy/`, and other active paths

Top-level imported groups:

- `apps/`
- `core/`
- `deploy/`
- `docs/`
- `examples/`
- `exports/`
- `hardware/`
- `image/`
- `migration-bundles/`
- `modules/`
- `scripts/`
- `services/`
- root metadata files such as `package.json`, `compose.yaml`, `Dockerfile`, and policy/config dotfiles

Why this layout:

- It keeps the source material searchable and reviewable without colliding with the target repository's existing structure.
- It gives later follow-up work a stable staging area for selective adoption into the main `Mira-Light-AI-That-Sees-You` code paths.

Suggested next step:

- Review `mira_core/mira-ai-that-sees-you/core/`, `modules/`, and `services/` first if the goal is to absorb reusable runtime capabilities into the active project.
