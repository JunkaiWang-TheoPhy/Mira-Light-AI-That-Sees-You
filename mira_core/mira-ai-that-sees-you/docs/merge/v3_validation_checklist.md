# V3 Validation Checklist

Date: 2026-04-06  
Repo: `/Users/Zhuanz/Documents/Github/Mira-AI-that-sees-you`  
Branch: `feat/upgrade-from-release-v3`

## 1. How to Use This Checklist

Use this document as the execution-time checklist for validation.

Rules:

- check items only after actually running the command or review
- add notes next to failures
- do not skip root manifest and workspace checks after changing package files
- do not skip doc consistency checks after merging README or migration docs

## 2. Baseline Safety Checks

- [ ] Confirm current branch is `feat/upgrade-from-release-v3`
- [ ] Confirm working tree status is understood before editing
- [ ] Confirm `docs/merge/diff_report_2026-04-06.md` exists
- [ ] Confirm `docs/merge/v3_merge_upgrade_plan_2026-04-06.md` exists
- [ ] Confirm `migration-bundles/` exists

Suggested commands:

```bash
git branch --show-current
git status --short --branch
find docs/merge -maxdepth 1 -type f | sort
find migration-bundles -maxdepth 2 -type d | sed -n '1,120p'
```

Notes:

```text

```

## 3. Documentation Merge Validation

Run this section after changing:

- `README.md`
- `readme/**`
- `docs/**`
- `examples/**`
- `hardware/README.md`

Checklist:

- [ ] All referenced directories still exist
- [ ] All referenced commands still exist in package manifests
- [ ] `migration-bundles/` is described as a release/migration asset, not runtime core
- [ ] `services/lingzhu-live-adapter/` is not accidentally omitted from current repo narrative
- [ ] `modules/home-assistant/direct-adapters/` is not accidentally omitted from current repo narrative
- [ ] `exports/` is not described as release-only imported content

Suggested commands:

```bash
rg -n "migration-bundles|lingzhu-live-adapter|direct-adapters|exports|notification-router|repo-deploy-runtime" README.md readme docs examples modules services deploy
find README.md readme docs examples modules services deploy -type f | sed -n '1,200p'
```

Notes:

```text

```

## 4. Root Manifest Validation

Run this section after changing:

- `package.json`
- `scripts/**`
- any root-level docs that describe root scripts

Checklist:

- [ ] Root `package.json` still contains `services/lingzhu-live-adapter` in `workspaces`
- [ ] Root `package.json` still keeps deploy/runtime commands such as `doctor`, `manifest:deploy`, `status`, `health`
- [ ] Root `package.json` still keeps `verify:release`, `test:release`, `export:repo`
- [ ] Node engine remains `>=20 <26`
- [ ] No development-only script was accidentally removed

Suggested commands:

```bash
node -e "const fs=require('fs');const j=JSON.parse(fs.readFileSync('package.json','utf8'));console.log(JSON.stringify({engines:j.engines,workspaces:j.workspaces,scripts:Object.keys(j.scripts)},null,2));"
```

Notes:

```text

```

## 5. Install and Workspace Resolution

Run this section after changing:

- any `package.json`
- any `package-lock.json`

Checklist:

- [ ] `npm install` completes successfully
- [ ] workspace resolution succeeds
- [ ] no missing workspace packages are reported
- [ ] lockfile changes match intended manifest changes

Suggested commands:

```bash
npm install
npm ls --workspaces --depth=0
git diff -- package-lock.json */package-lock.json */*/package-lock.json
```

Notes:

```text

```

## 6. Lingzhu Bridge Validation

Run this section after changing:

- `core/plugins/lingzhu-bridge/**`

Checklist:

- [ ] `core/plugins/lingzhu-bridge/package.json` still exposes `openclaw.extensions`
- [ ] plugin tests pass
- [ ] documentation still matches plugin surface

Suggested commands:

```bash
node -e "const fs=require('fs');const j=JSON.parse(fs.readFileSync('core/plugins/lingzhu-bridge/package.json','utf8'));console.log(JSON.stringify({name:j.name,openclaw:j.openclaw,scripts:j.scripts},null,2));"
npm --workspace @mira-release/lingzhu run test
```

Notes:

```text

```

## 7. Home Assistant Module Validation

Run this section after changing:

- `modules/home-assistant/**`

Checklist:

- [ ] `modules/home-assistant/plugin/package.json` still uses the current dev-side test command
- [ ] `modules/home-assistant/direct-adapters/**` still exists
- [ ] `modules/home-assistant/docs/ecosystems/**` still exists
- [ ] plugin tests pass

Suggested commands:

```bash
node -e "const fs=require('fs');const j=JSON.parse(fs.readFileSync('modules/home-assistant/plugin/package.json','utf8'));console.log(JSON.stringify({name:j.name,scripts:j.scripts},null,2));"
find modules/home-assistant/direct-adapters -maxdepth 3 -type f | sed -n '1,120p'
find modules/home-assistant/docs/ecosystems -maxdepth 2 -type f | sed -n '1,120p'
npm --workspace @mira-release/home-assistant-module-plugin run test
```

Notes:

```text

```

## 8. Notification Router Validation

Run this section after changing:

- `services/notification-router/**`

Checklist:

- [ ] `services/notification-router/package.json` still keeps `dev`, `start`, and `test`
- [ ] notification router tests pass
- [ ] runtime docs still match actual command surface

Suggested commands:

```bash
node -e "const fs=require('fs');const j=JSON.parse(fs.readFileSync('services/notification-router/package.json','utf8'));console.log(JSON.stringify({name:j.name,scripts:j.scripts},null,2));"
npm --workspace @mira-release/notification-router run test
```

Notes:

```text

```

## 9. Release Verification Layer

Run this section after changing:

- `scripts/verify-release.mjs`
- `scripts/__tests__/*.test.mjs`
- release-related docs

Checklist:

- [ ] release verification tests pass
- [ ] export verification tests pass
- [ ] no release-side regression from imported migration assets

Suggested commands:

```bash
npm run test:release
```

Notes:

```text

```

## 10. Deploy and Runtime Validation

Run this section after changing:

- `deploy/**`
- `core/openclaw-config/**`
- root scripts

Checklist:

- [ ] deploy doctor passes
- [ ] deploy manifest generation succeeds
- [ ] no missing runtime config file is reported

Suggested commands:

```bash
npm run doctor
npm run manifest:deploy
```

If environment allows:

```bash
npm run health:notification-router
npm run start:lingzhu-live-adapter
```

Notes:

```text

```

## 11. Final PR Readiness Checks

- [ ] first low-risk baseline import is committed
- [ ] major doc merge tasks are committed separately from runtime tasks
- [ ] root manifest changes are isolated and explained
- [ ] lockfile changes were regenerated, not hand-spliced
- [ ] PR description explains imported assets vs manually merged files
- [ ] reviewers are pointed to the highest-risk files

Suggested commands:

```bash
git status --short
git log --oneline --decorate -n 20
```

Notes:

```text

```

## 12. Reviewer Hotspots

Before opening the PR, manually inspect at least these files:

- `package.json`
- `README.md`
- `core/plugins/lingzhu-bridge/package.json`
- `modules/home-assistant/plugin/package.json`
- `modules/home-assistant/plugin/src/registry/loadDevicesRegistry.ts`
- `services/notification-router/package.json`
- `services/notification-router/src/server.ts`
- `services/notification-router/src/channels/openclawChannelDm.ts`
- `docs/migration/repository-split-checklist.md`
- `migration-bundles/README.md`
