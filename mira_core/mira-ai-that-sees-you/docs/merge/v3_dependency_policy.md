# V3 Dependency Policy

Date: 2026-04-06  
Repo: `/Users/Zhuanz/Documents/Github/Mira-AI-that-sees-you`  
Branch: `feat/upgrade-from-release-v3`

## 1. Purpose

This document defines the dependency and manifest policy for the V3 upgrade merge.

It exists to prevent a common failure mode:

- a documentation or release-oriented merge accidentally downgrades the active development manifest/runtime surface

## 2. Policy Summary

The main rule is simple:

- dependency and manifest truth comes from the current GitHub development repo, not from `Mira_Released_Version`

Release-side manifest content can be used only when it is:

- additive
- compatible with the current development runtime
- clearly better than what already exists

## 3. Source-of-Truth Table

| File | Source of Truth | Merge Rule |
| --- | --- | --- |
| `package.json` | development repo | keep development version, additive-only changes |
| `core/plugins/lingzhu-bridge/package.json` | development repo | keep development version |
| `modules/home-assistant/plugin/package.json` | development repo | keep development version |
| `services/notification-router/package.json` | development repo | keep development version |
| `services/lingzhu-live-adapter/package.json` | development repo | keep and protect |
| `core/plugins/lingzhu-bridge/package-lock.json` | final generated state | regenerate, do not hand-merge |
| `services/notification-router/package-lock.json` | final generated state | regenerate, do not hand-merge |
| `LICENSE` | development repo | keep real license |
| `LICENSE.placeholder.md` | release repo | do not promote into root manifest path |

## 4. Root Manifest Policy

Current development root manifest contains critical invariants that must remain intact.

### 4.1 Protected Root Fields

These fields are protected:

- `license: AGPL-3.0-only`
- `type: module`
- `engines.node: >=20 <26`
- `workspaces`
- root `scripts`

### 4.2 Protected Workspaces

These workspaces must stay in the root manifest:

- `core/plugins/lingzhu-bridge`
- `modules/home-assistant/plugin`
- `services/notification-router`
- `services/lingzhu-live-adapter`

Rules:

- do not remove any current workspace
- do not rename a workspace package without repo-wide migration
- do not reintroduce release-side simpler workspace lists

### 4.3 Protected Root Scripts

The following script groups are protected and must not be removed:

Release/verification:

- `verify:release`
- `test:release`
- `export:repo`

Root deploy/runtime:

- `manifest:deploy`
- `bootstrap`
- `doctor`
- `start`
- `deploy`
- `status`
- `health`
- `self-check`
- `down`

Notification Router subcommands:

- `bootstrap:notification-router`
- `deploy:notification-router`
- `doctor:notification-router`
- `start:notification-router`
- `up:notification-router`
- `status:notification-router`
- `down:notification-router`
- `health:notification-router`
- `self-check:notification-router`

Mira OpenClaw subcommands:

- `bootstrap:mira-openclaw`
- `deploy:mira-openclaw`
- `doctor:mira-openclaw`
- `start:mira-openclaw`
- `up:mira-openclaw`
- `status:mira-openclaw`
- `down:mira-openclaw`
- `health:mira-openclaw`
- `self-check:mira-openclaw`

Lingzhu Live Adapter:

- `start:lingzhu-live-adapter`

### 4.4 Allowed Root Manifest Changes

Allowed changes:

- additive scripts that do not break existing names
- additive metadata fields
- documentation-aligned rewording where safe
- dependency additions required by a real feature merge

Forbidden changes:

- removing current scripts
- removing current workspaces
- lowering Node version support below current contract
- replacing the development root manifest with the release root manifest

## 5. Workspace Manifest Policy

### 5.1 `core/plugins/lingzhu-bridge/package.json`

Protected properties:

- current package identity
- current script surface
- `openclaw.extensions`

Special rule:

- `openclaw.extensions` must continue to point to `./src/index.ts`

Allowed changes:

- additive metadata
- dependency changes needed by current implementation
- test script updates only if they improve current behavior and remain compatible

Forbidden changes:

- removing `openclaw.extensions`
- replacing the manifest with the release version

### 5.2 `modules/home-assistant/plugin/package.json`

Protected properties:

- current package identity
- current test command

Current protected test command:

```text
node --experimental-strip-types --test src/**/*.test.ts
```

Allowed changes:

- dependency changes required by merged implementation
- additive metadata

Forbidden changes:

- reverting to placeholder-style release-side test messaging
- replacing the current test command with a weaker placeholder

### 5.3 `services/notification-router/package.json`

Protected properties:

- current package identity
- `dev`
- `start`
- `test`

Current protected scripts:

- `dev: tsx watch src/server.ts`
- `start: tsx src/server.ts`
- `test: tsx --test src/__tests__/*.test.ts`

Allowed changes:

- additive dependencies
- additive metadata
- compatibility improvements

Forbidden changes:

- removing runtime scripts
- replacing current manifest with the release version

### 5.4 `services/lingzhu-live-adapter/package.json`

This file is development-only and must be preserved.

Protected properties:

- workspace presence
- `type: module`
- `engines.node: >=20 <26`
- `start: node src/server.js`

Special rule:

- this workspace has no release-side counterpart and therefore cannot be “merged away”

## 6. Lockfile Policy

Lockfiles are not hand-authored merge documents.

Rule:

- do not manually splice or hand-edit `package-lock.json` files line-by-line

Affected files:

- `core/plugins/lingzhu-bridge/package-lock.json`
- `services/notification-router/package-lock.json`

Policy:

- first finalize the corresponding `package.json`
- then regenerate the lockfile through the package manager
- then review the lockfile diff for unexpected churn

What counts as acceptable lockfile churn:

- dependency graph updates caused by intentional manifest changes
- integrity hash updates from regeneration
- version movement directly attributable to intended dependency changes

What counts as suspicious lockfile churn:

- large unrelated tree shifts after a docs-only change
- new dependencies not explained by manifest edits
- removed packages required by current runtime scripts

## 7. When to Run `npm install`

Run `npm install` after:

- changing root `package.json`
- changing any workspace `package.json`
- intentionally regenerating a workspace lockfile

Usually do not run `npm install` just because:

- a README changed
- a migration doc changed
- an example doc changed

If you changed both docs and manifests in one wave:

- treat it as a manifest wave
- run full install and validation

## 8. Manifest Change Workflow

When changing any protected manifest, use this exact order:

1. compare release and development versions
2. state the intended rule:
   - keep dev
   - additive merge
   - no change
3. edit the manifest
4. run `npm install`
5. inspect manifest and lockfile diff
6. run the relevant workspace/root tests
7. only then commit

## 9. Validation Requirements by Manifest

| File | Minimum Validation |
| --- | --- |
| `package.json` | `npm install`, `npm run test:release`, `npm run doctor`, `npm run manifest:deploy` |
| `core/plugins/lingzhu-bridge/package.json` | `npm install`, `npm --workspace @mira-release/lingzhu run test` |
| `modules/home-assistant/plugin/package.json` | `npm install`, `npm --workspace @mira-release/home-assistant-module-plugin run test` |
| `services/notification-router/package.json` | `npm install`, `npm --workspace @mira-release/notification-router run test` |
| `services/lingzhu-live-adapter/package.json` | `npm install`, `npm run start:lingzhu-live-adapter` when environment allows |

## 10. Forbidden Dependency Actions

These actions are explicitly disallowed in the V3 merge:

- replacing the current root manifest with the release root manifest
- dropping `services/lingzhu-live-adapter` from root workspaces
- removing current deploy/runtime scripts from root `package.json`
- replacing active workspace manifests with simpler release-side manifests
- hand-splicing lockfiles
- deleting a dependency solely because the release repo did not have it

## 11. Practical Review Questions

Before approving any manifest change, answer these questions:

- does this keep current development runtime behavior intact
- does this preserve all current workspaces
- does this preserve all current protected scripts
- is every dependency change explained by a real merged feature or runtime need
- was the lockfile regenerated instead of manually stitched
- were the relevant tests actually run

If any answer is "no" or "not sure", the manifest change should not be merged yet.
