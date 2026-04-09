# V3 Merge Backlog

Date: 2026-04-06  
Repo: `/Users/Zhuanz/Documents/Github/Mira-AI-that-sees-you`  
Branch: `feat/upgrade-from-release-v3`

## 1. Purpose

This document breaks the V3 upgrade merge into concrete executable tasks.

It answers:

- what to do next
- in what order
- with what validation
- at what risk level

## 2. Status Legend

- `done`: already executed
- `ready`: can be executed now
- `blocked`: should wait for another task
- `review`: implemented but awaiting validation or review

Risk legend:

- `low`: mostly additive, low regression chance
- `medium`: shared docs or shared config, moderate regression chance
- `high`: shared runtime or manifest surface, high regression chance

## 3. Current Completed Work

| ID | Task | Scope | Validation | Status |
| --- | --- | --- | --- | --- |
| `BL-000` | create upgrade branch | `feat/upgrade-from-release-v3` | branch check | done |
| `BL-001` | archive baseline docs | `docs/merge/diff_report_2026-04-06.md`, `docs/merge/v3_merge_upgrade_plan_2026-04-06.md` | file presence | done |
| `BL-002` | import release migration assets | `migration-bundles/**` | dry-run + file count | done |
| `BL-003` | record execution state | `docs/merge/v3_merge_execution_log_2026-04-06.md` | file presence | done |

## 4. Active Backlog

### Wave 1: Save the Low-Risk Base

| ID | Task | Scope | Action | Validation | Risk | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `BL-010` | commit baseline import wave | `docs/merge/**`, `migration-bundles/**` | create first merge commit | `git status`, diff review | low | ready |

Notes:

- This commit should happen before shared-path editing begins.
- It creates a rollback-safe checkpoint.

### Wave 2: Merge Documentation Surface

| ID | Task | Scope | Action | Validation | Risk | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `BL-020` | merge top-level repo docs | `README.md`, `readme/README.md` | unify repo positioning | `doc-links` | medium | review |
| `BL-021` | merge overview readme tree | `readme/00-overview/**` | align navigation and mental model | `doc-links` | medium | review |
| `BL-026` | merge remaining portal navigation docs | `readme/10-core/README.md`, `readme/20-modules/README.md`, `readme/30-hardware/README.md` | align portal boundaries after overview merge | `doc-links` | medium | review |
| `BL-022` | merge deploy readme tree | `readme/40-deploy/**`, `deploy/**` docs | align deploy language with current repo | `doc-links` | medium | review |
| `BL-023` | merge migration docs | `docs/migration/**`, `readme/50-development/contributing-and-migration.md` | align release and migration narrative | `doc-links` | medium | review |
| `BL-024` | merge example docs | `examples/**` | align examples with current runtime surface | `doc-links` | medium | review |
| `BL-025` | merge docs portal root readme | `docs/README.md` | align docs portal wording with upgraded repo | `doc-links` | medium | review |
| `BL-027` | merge module and hardware entry docs | `modules/README.md`, `hardware/README.md` | align portal entrypoints with updated examples and overview | `doc-links` | medium | review |
| `BL-028` | merge architecture docs portal root | `docs/architecture/README.md` | align architecture docs entrypoint with upgraded repo wording | `doc-links` | medium | ready |

### Wave 3: Contract and Config Surface

| ID | Task | Scope | Action | Validation | Risk | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `BL-030` | protect and review root manifest | `package.json` | freeze workspace and script invariants | `install`, `doctor`, `manifest` | high | ready |
| `BL-031` | merge OpenClaw config surface | `core/openclaw-config/**` | align examples, prompt contract, runtime contract | `doctor` | high | ready |
| `BL-032` | merge workspace guidance | `core/workspace/AGENTS.md`, `core/workspace/README.md` | align workspace instructions | `doc-links` | medium | ready |
| `BL-033` | merge deploy env contracts | `deploy/service-notification-router/env.example`, deploy docs | align env shape without losing current deploy features | `doctor` | high | ready |
| `BL-034` | merge Home Assistant config examples | `modules/home-assistant/config/**`, `modules/home-assistant/registry/devices.example.json` | align config examples with current module layout | `ws-ha` | high | ready |

### Wave 4: Shared Code Surface

| ID | Task | Scope | Action | Validation | Risk | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `BL-040` | reconcile Lingzhu bridge docs and manifest | `core/plugins/lingzhu-bridge/README.md`, `package.json` | keep dev runtime, absorb release explanation | `ws-lingzhu` | high | ready |
| `BL-041` | reconcile Lingzhu bridge lockfile | `core/plugins/lingzhu-bridge/package-lock.json` | regenerate after final manifest state | `install`, `ws-lingzhu` | medium | blocked |
| `BL-042` | reconcile Home Assistant module docs | `modules/home-assistant/README.md`, `docs/**`, `plugin/README.md`, `registry/README.md` | merge docs and contracts | `doc-links`, `ws-ha` | high | ready |
| `BL-043` | reconcile Home Assistant plugin behavior | `modules/home-assistant/plugin/src/registry/loadDevicesRegistry.ts` | keep dev implementation, port selective semantics | `ws-ha` | high | ready |
| `BL-044` | reconcile Notification Router docs | `services/notification-router/**` README/docs/config docs | merge docs and service contract language | `doc-links`, `ws-router` | high | ready |
| `BL-045` | reconcile Notification Router manifest | `services/notification-router/package.json` | keep dev scripts and runtime behavior | `install`, `ws-router` | high | ready |
| `BL-046` | reconcile Notification Router implementation | `services/notification-router/src/server.ts`, `src/channels/openclawChannelDm.ts`, tests | keep dev implementation, port selective semantics | `ws-router` | high | ready |
| `BL-047` | reconcile Notification Router lockfile | `services/notification-router/package-lock.json` | regenerate after final manifest state | `install`, `ws-router` | medium | blocked |

### Wave 5: Root Script and Release Verification Layer

| ID | Task | Scope | Action | Validation | Risk | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `BL-050` | reconcile release verification scripts | `scripts/verify-release.mjs`, `scripts/__tests__/verify-release.test.mjs`, `scripts/__tests__/export-release-repo.test.mjs` | preserve current root runtime and port useful assertions | `release-tests` | high | ready |

### Wave 6: Final Verification and PR Packaging

| ID | Task | Scope | Action | Validation | Risk | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `BL-060` | full workspace install and verification | root + all workspaces | run install and primary verification set | `install`, `release-tests`, `ws-lingzhu`, `ws-ha`, `ws-router`, `doctor`, `manifest` | high | blocked |
| `BL-061` | final doc consistency pass | repo docs and examples | verify all paths, commands, roles | `doc-links` | medium | blocked |
| `BL-062` | PR preparation | PR text, summary, review notes | prepare reviewer-friendly final story | manual review | low | blocked |

## 5. Immediate Next Three Tasks

If execution continues now, the recommended next three tasks are:

1. `BL-010`: create the first checkpoint commit
2. `BL-028`: merge `docs/architecture/README.md`
3. `BL-033`: merge deploy env contracts

Why these three:

- they stabilize the baseline
- they finish the last high-level docs gap before contract/config work
- they prepare the handoff from documentation wave into env and config contracts

## 6. Blocking Rules

The following tasks must wait for prerequisites:

- `BL-041` waits for `BL-040`
- `BL-047` waits for `BL-045`
- `BL-060` waits for all major docs/config/code tasks
- `BL-061` waits for `BL-060`
- `BL-062` waits for `BL-061`

## 7. Recommended Commit Boundaries

Use these commit boundaries instead of giant mixed commits:

| Commit Group | Backlog IDs |
| --- | --- |
| baseline checkpoint | `BL-010` |
| top-level docs | `BL-020`, `BL-021`, `BL-025`, `BL-026`, `BL-027` |
| migration and deploy docs | `BL-022`, `BL-023`, `BL-024`, `BL-028` |
| contract and config | `BL-030` to `BL-034` |
| Lingzhu bridge | `BL-040`, `BL-041` |
| Home Assistant module | `BL-042`, `BL-043` |
| Notification Router | `BL-044` to `BL-047` |
| release verification layer | `BL-050` |
| final verification and PR | `BL-060` to `BL-062` |

## 8. Notes for Operators

When a backlog item is completed:

1. update its status here
2. append the result to `v3_merge_execution_log_2026-04-06.md`
3. record any unexpected decision in `v3_file_decision_matrix.md`

This backlog is not only a todo list.  
It is also the control surface for sequencing and review.
