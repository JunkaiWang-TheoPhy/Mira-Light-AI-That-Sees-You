# Repository Split Checklist

## Purpose

This checklist defines the concrete steps for exporting the current release-ready subset of the main repo into its own repository.

## Checklist

1. Review:
   - [release-baseline.md](./release-baseline.md)
   - [open-source-readiness-checklist.md](./open-source-readiness-checklist.md)
   - [package-and-license-decisions.md](./package-and-license-decisions.md)
2. From the repo root, run:
   - `npm run verify:release`
   - `npm run test:release`
3. Export the standalone directory package from the repo root:
   - `npm run export:repo`
4. Go to the exported directory package.
5. Confirm the exported package still contains a top-level `LICENSE`.
6. Confirm the exported package contains the intended release-safe directories, and explicitly decide whether `migration-bundles/` should ship with that split target.
7. Run the same verify and test commands again inside the exported package.
8. Initialize the new repository:
   - `git init`
   - `git add .`
   - `git commit -m "chore: initialize Mira release repository"`

## Default Export Location

The current export script writes to:

- `../exports/mira-released-version-repo`

relative to the repo root.

## Non-Goals

This checklist does not revisit the selected AGPL-3.0 license or create the remote repository for you.
