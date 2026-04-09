# V3 File Decision Matrix

Date: 2026-04-06  
Repo: `/Users/Zhuanz/Documents/Github/Mira-AI-that-sees-you`  
Branch: `feat/upgrade-from-release-v3`

## 1. Purpose

This document is the file-level decision register for the V3 upgrade merge.

It exists to answer the question:

- For each differing file or critical unique file, what exactly should we do with it?

This document should be used together with:

- `docs/merge/diff_report_2026-04-06.md`
- `docs/merge/v3_merge_upgrade_plan_2026-04-06.md`
- `docs/merge/v3_merge_backlog.md`
- `docs/merge/v3_dependency_policy.md`

## 2. Decision Legend

Decision codes:

- `KEEP_DEV`: keep the current GitHub development version as the source of truth
- `IMPORT_REL`: import the release-only asset as-is
- `MERGE_DOC`: manually merge wording, structure, and explanation; development repo remains factual base
- `MERGE_CFG`: manually merge config or contract content; do not break current runtime
- `PORT_SEMANTICS`: keep development implementation, selectively port release-side semantics/comments/tests
- `REGEN_LOCK`: do not hand-merge the lockfile; regenerate from the final manifest state
- `SKIP_REL`: do not import the release-side file into the main runtime path

Status codes:

- `done`: already completed
- `pending`: not executed yet
- `guarded`: no merge needed now, but the file must be protected from regression

Validation shorthand:

- `doc-links`: verify paths, scripts, and references mentioned in docs actually exist
- `doctor`: run `npm run doctor`
- `release-tests`: run `npm run test:release`
- `ws-lingzhu`: run `npm --workspace @mira-release/lingzhu run test`
- `ws-ha`: run `npm --workspace @mira-release/home-assistant-module-plugin run test`
- `ws-router`: run `npm --workspace @mira-release/notification-router run test`
- `manifest`: run `npm run manifest:deploy`
- `install`: run `npm install`

## 3. Protected Development-Only Assets

These are development-side assets that must not be overwritten or removed during the merge.

| Path | Decision | Why | Validation | Status |
| --- | --- | --- | --- | --- |
| `.dockerignore` | `KEEP_DEV` | active deployment support | doc-links | guarded |
| `Dockerfile` | `KEEP_DEV` | active deployment support | doctor | guarded |
| `Procfile` | `KEEP_DEV` | active process entry | doctor | guarded |
| `compose.yaml` | `KEEP_DEV` | active deployment support | doctor | guarded |
| `render.yaml` | `KEEP_DEV` | active deployment support | doctor | guarded |
| `LICENSE` | `KEEP_DEV` | real license replaces placeholder model | doc-links | guarded |
| `core/plugins/lingzhu-bridge/openclaw.plugin.json` | `KEEP_DEV` | current plugin registration asset | ws-lingzhu | guarded |
| `core/plugins/lingzhu-bridge/src/index.ts` | `KEEP_DEV` | current OpenClaw extension entrypoint | ws-lingzhu | guarded |
| `core/workspace/IDENTITY.md` | `KEEP_DEV` | development-only workspace knowledge asset | doc-links | guarded |
| `core/workspace/SOUL.md` | `KEEP_DEV` | development-only workspace knowledge asset | doc-links | guarded |
| `deploy/mira-openclaw/**` | `KEEP_DEV` | active development deployment capability | doctor | guarded |
| `deploy/module-home-assistant/hue-direct-adapter.md` | `KEEP_DEV` | development-only adapter guidance | doc-links | guarded |
| `deploy/repo-manifest.json` | `KEEP_DEV` | active deploy manifest | manifest | guarded |
| `deploy/repo.env.example` | `KEEP_DEV` | active deploy contract | doctor | guarded |
| `docs/plans/**` | `KEEP_DEV` | active planning assets | doc-links | guarded |
| `docs/superpowers/**` | `KEEP_DEV` | active design assets | doc-links | guarded |
| `exports/**` | `KEEP_DEV` | development-only export packs | doc-links | guarded |
| `image/**` | `KEEP_DEV` | development repository assets | doc-links | guarded |
| `modules/home-assistant/direct-adapters/**` | `KEEP_DEV` | active development-only capability | ws-ha | guarded |
| `modules/home-assistant/docs/ecosystems/**` | `KEEP_DEV` | active ecosystem docs | doc-links | guarded |
| `modules/home-assistant/docs/home-ecosystem-support-matrix.md` | `KEEP_DEV` | active support matrix | doc-links | guarded |
| `modules/home-assistant/plugin/src/registry/loadDevicesRegistry.test.ts` | `KEEP_DEV` | current development test asset | ws-ha | guarded |
| `scripts/mira-openclaw-runtime.mjs` | `KEEP_DEV` | active root runtime script | doctor | guarded |
| `scripts/notification-router-runtime.mjs` | `KEEP_DEV` | active root runtime script | doctor | guarded |
| `scripts/repo-deploy-runtime.mjs` | `KEEP_DEV` | active root deploy script | doctor | guarded |
| `scripts/runtime-utils.mjs` | `KEEP_DEV` | shared active runtime helper | doctor | guarded |
| `scripts/__tests__/home-ecosystem-hue-boundary.test.mjs` | `KEEP_DEV` | active root test asset | release-tests | guarded |
| `scripts/__tests__/home-ecosystem-wave2.test.mjs` | `KEEP_DEV` | active root test asset | release-tests | guarded |
| `scripts/__tests__/mira-openclaw-runtime.test.mjs` | `KEEP_DEV` | active root test asset | release-tests | guarded |
| `scripts/__tests__/notification-router-runtime.test.mjs` | `KEEP_DEV` | active root test asset | release-tests | guarded |
| `scripts/__tests__/repo-deploy-runtime.test.mjs` | `KEEP_DEV` | active root test asset | release-tests | guarded |
| `services/lingzhu-live-adapter/**` | `KEEP_DEV` | active development-only service | doctor | guarded |

## 4. Release-Only Assets

These are release-side assets that need explicit treatment.

| Path | Decision | Why | Validation | Status |
| --- | --- | --- | --- | --- |
| `migration-bundles/**` | `IMPORT_REL` | this is the main unique value of the release repo | doc-links | done |
| `LICENSE.placeholder.md` | `SKIP_REL` | do not replace real repo license with placeholder material | doc-links | pending |

## 5. Shared-Diff Matrix

The files below exist in both repositories, but their contents differ. These are the main manual-merge targets.

### 5.1 Root and App Surface

| Path | Type | Decision | Source of Truth | Validation | Status |
| --- | --- | --- | --- | --- | --- |
| `.gitignore` | repo config | `MERGE_CFG` | dev-led | doc-links | pending |
| `README.md` | repo docs | `MERGE_DOC` | dev-led | doc-links | done |
| `apps/README.md` | docs | `MERGE_DOC` | dev-led | doc-links | pending |
| `package.json` | root manifest | `KEEP_DEV` | dev | install, doctor, manifest | pending |

### 5.2 Core Surface

| Path | Type | Decision | Source of Truth | Validation | Status |
| --- | --- | --- | --- | --- | --- |
| `core/README.md` | docs | `MERGE_DOC` | dev-led | doc-links | pending |
| `core/examples/README.md` | docs | `MERGE_DOC` | dev-led | doc-links | pending |
| `core/openclaw-config/README.md` | contract docs | `MERGE_DOC` | dev-led | doc-links | pending |
| `core/openclaw-config/lingzhu-config-snippet.example.json5` | config example | `MERGE_CFG` | dev-led | doctor | pending |
| `core/openclaw-config/lingzhu-system-prompt.txt` | prompt contract | `MERGE_CFG` | dev-led | doctor | pending |
| `core/openclaw-config/minimal-runtime-contract.md` | contract docs | `MERGE_DOC` | dev-led | doc-links | pending |
| `core/openclaw-config/openclaw.example.json` | config example | `MERGE_CFG` | dev-led | doctor | pending |
| `core/persona/README.md` | docs | `MERGE_DOC` | dev-led | doc-links | pending |
| `core/plugins/README.md` | docs | `MERGE_DOC` | dev-led | doc-links | pending |
| `core/plugins/lingzhu-bridge/README.md` | plugin docs | `MERGE_DOC` | dev-led | ws-lingzhu | pending |
| `core/plugins/lingzhu-bridge/package-lock.json` | lockfile | `REGEN_LOCK` | final generated state | install, ws-lingzhu | pending |
| `core/plugins/lingzhu-bridge/package.json` | plugin manifest | `KEEP_DEV` | dev | install, ws-lingzhu | pending |
| `core/skills/README.md` | docs | `MERGE_DOC` | dev-led | doc-links | pending |
| `core/workspace/AGENTS.md` | workspace docs | `MERGE_DOC` | dev-led | doc-links | pending |
| `core/workspace/README.md` | workspace docs | `MERGE_DOC` | dev-led | doc-links | pending |

### 5.3 Deploy Surface

| Path | Type | Decision | Source of Truth | Validation | Status |
| --- | --- | --- | --- | --- | --- |
| `deploy/README.md` | deploy docs | `MERGE_DOC` | dev-led | doc-links | done |
| `deploy/core/README.md` | deploy docs | `MERGE_DOC` | dev-led | doc-links | done |
| `deploy/deploy-paths-overview.md` | deploy docs | `MERGE_DOC` | dev-led | doc-links | done |
| `deploy/minimal/README.md` | deploy docs | `MERGE_DOC` | dev-led | doc-links | done |
| `deploy/module-home-assistant/README.md` | deploy docs | `MERGE_DOC` | dev-led | doc-links | done |
| `deploy/service-notification-router/README.md` | deploy docs | `MERGE_DOC` | dev-led | doc-links | done |
| `deploy/service-notification-router/env.example` | env contract | `MERGE_CFG` | dev-led | doctor | pending |

### 5.4 Docs, Examples, Hardware

| Path | Type | Decision | Source of Truth | Validation | Status |
| --- | --- | --- | --- | --- | --- |
| `docs/README.md` | docs | `MERGE_DOC` | dev-led | doc-links | done |
| `docs/architecture/README.md` | docs | `MERGE_DOC` | dev-led | doc-links | pending |
| `docs/migration/README.md` | docs | `MERGE_DOC` | dev-led | doc-links | done |
| `docs/migration/release-baseline.md` | docs | `MERGE_DOC` | dev-led | doc-links | done |
| `docs/migration/open-source-readiness-checklist.md` | docs | `MERGE_DOC` | dev-led | doc-links | done |
| `docs/migration/package-and-license-decisions.md` | docs | `MERGE_DOC` | dev-led | doc-links | done |
| `docs/migration/repository-split-checklist.md` | docs | `MERGE_DOC` | dev-led | doc-links | done |
| `docs/migration/repository-split-readiness.md` | docs | `MERGE_DOC` | dev-led | doc-links | done |
| `examples/README.md` | docs | `MERGE_DOC` | dev-led | doc-links | done |
| `examples/home-stack-with-notification-router/README.md` | docs | `MERGE_DOC` | dev-led | doc-links | done |
| `examples/home-stack/README.md` | docs | `MERGE_DOC` | dev-led | doc-links | done |
| `examples/minimal-core/README.md` | docs | `MERGE_DOC` | dev-led | doc-links | done |
| `examples/service-notification-router/README.md` | docs | `MERGE_DOC` | dev-led | doc-links | done |
| `hardware/README.md` | docs | `MERGE_DOC` | dev-led | doc-links | done |

### 5.5 Modules and Home Assistant

| Path | Type | Decision | Source of Truth | Validation | Status |
| --- | --- | --- | --- | --- | --- |
| `modules/README.md` | docs | `MERGE_DOC` | dev-led | doc-links | done |
| `modules/home-assistant/README.md` | module docs | `MERGE_DOC` | dev-led | doc-links | pending |
| `modules/home-assistant/config/README.md` | config docs | `MERGE_DOC` | dev-led | doc-links | pending |
| `modules/home-assistant/config/home-assistant-module.example.json` | config example | `MERGE_CFG` | dev-led | ws-ha | pending |
| `modules/home-assistant/docs/README.md` | module docs | `MERGE_DOC` | dev-led | doc-links | pending |
| `modules/home-assistant/docs/module-runtime-contract.md` | contract docs | `MERGE_DOC` | dev-led | doc-links | pending |
| `modules/home-assistant/docs/package-assembly-checklist.md` | docs | `MERGE_DOC` | dev-led | doc-links | pending |
| `modules/home-assistant/plugin/README.md` | plugin docs | `MERGE_DOC` | dev-led | ws-ha | pending |
| `modules/home-assistant/plugin/package.json` | plugin manifest | `KEEP_DEV` | dev | install, ws-ha | pending |
| `modules/home-assistant/plugin/src/README.md` | plugin docs | `MERGE_DOC` | dev-led | ws-ha | pending |
| `modules/home-assistant/plugin/src/registry/loadDevicesRegistry.ts` | implementation | `PORT_SEMANTICS` | dev | ws-ha | pending |
| `modules/home-assistant/registry/README.md` | registry docs | `MERGE_DOC` | dev-led | doc-links | pending |
| `modules/home-assistant/registry/devices.example.json` | config example | `MERGE_CFG` | dev-led | ws-ha | pending |

### 5.6 Readme Tree

| Path | Type | Decision | Source of Truth | Validation | Status |
| --- | --- | --- | --- | --- | --- |
| `readme/00-overview/README.md` | docs | `MERGE_DOC` | dev-led | doc-links | done |
| `readme/00-overview/getting-started.md` | docs | `MERGE_DOC` | dev-led | doc-links | done |
| `readme/00-overview/quick-start.md` | docs | `MERGE_DOC` | dev-led | doc-links | done |
| `readme/10-core/README.md` | docs | `MERGE_DOC` | dev-led | doc-links | done |
| `readme/20-modules/README.md` | docs | `MERGE_DOC` | dev-led | doc-links | done |
| `readme/30-hardware/README.md` | docs | `MERGE_DOC` | dev-led | doc-links | done |
| `readme/40-deploy/README.md` | docs | `MERGE_DOC` | dev-led | doc-links | done |
| `readme/50-development/README.md` | docs | `MERGE_DOC` | dev-led | doc-links | pending |
| `readme/50-development/contributing-and-migration.md` | docs | `MERGE_DOC` | dev-led | doc-links | pending |
| `readme/README.md` | docs | `MERGE_DOC` | dev-led | doc-links | done |

### 5.7 Scripts and Release Tests

| Path | Type | Decision | Source of Truth | Validation | Status |
| --- | --- | --- | --- | --- | --- |
| `scripts/__tests__/export-release-repo.test.mjs` | root test | `PORT_SEMANTICS` | dev | release-tests | pending |
| `scripts/__tests__/verify-release.test.mjs` | root test | `PORT_SEMANTICS` | dev | release-tests | pending |
| `scripts/verify-release.mjs` | root script | `KEEP_DEV` | dev | release-tests, manifest | pending |

### 5.8 Services and Notification Router

| Path | Type | Decision | Source of Truth | Validation | Status |
| --- | --- | --- | --- | --- | --- |
| `services/README.md` | docs | `MERGE_DOC` | dev-led | doc-links | pending |
| `services/notification-router/README.md` | service docs | `MERGE_DOC` | dev-led | doc-links | pending |
| `services/notification-router/config/README.md` | service docs | `MERGE_DOC` | dev-led | doc-links | pending |
| `services/notification-router/docs/README.md` | service docs | `MERGE_DOC` | dev-led | doc-links | pending |
| `services/notification-router/package-lock.json` | lockfile | `REGEN_LOCK` | final generated state | install, ws-router | pending |
| `services/notification-router/package.json` | service manifest | `KEEP_DEV` | dev | install, ws-router | pending |
| `services/notification-router/src/README.md` | service docs | `MERGE_DOC` | dev-led | doc-links | pending |
| `services/notification-router/src/__tests__/notification-router.test.ts` | service test | `PORT_SEMANTICS` | dev | ws-router | pending |
| `services/notification-router/src/channels/openclawChannelDm.ts` | service implementation | `PORT_SEMANTICS` | dev | ws-router | pending |
| `services/notification-router/src/server.ts` | service implementation | `PORT_SEMANTICS` | dev | ws-router | pending |

## 6. Immediate Priority Set

The highest-value next manual merge targets are:

1. `README.md`
2. `readme/README.md`
3. `docs/migration/README.md`
4. `docs/migration/repository-split-checklist.md`
5. `package.json`
6. `core/openclaw-config/openclaw.example.json`
7. `core/plugins/lingzhu-bridge/package.json`
8. `modules/home-assistant/plugin/package.json`
9. `modules/home-assistant/plugin/src/registry/loadDevicesRegistry.ts`
10. `services/notification-router/package.json`
11. `services/notification-router/src/server.ts`
12. `services/notification-router/src/channels/openclawChannelDm.ts`

These files cover the merge-critical surface:

- repo positioning
- workspace / runtime contract
- Home Assistant module behavior
- Notification Router behavior

## 7. Usage Notes

How to use this matrix during execution:

1. Pick a backlog item from `v3_merge_backlog.md`
2. Open the matching files in this matrix
3. Follow the listed decision code exactly
4. Run the listed validation command before moving on
5. Mark progress in the execution log

Do not use this file as a changelog.  
Use it as the authoritative decision map for merge behavior.
