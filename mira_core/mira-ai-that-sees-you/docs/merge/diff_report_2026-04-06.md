# Mira_Released_Version 与 Mira-AI-that-sees-you 对比报告

生成时间：2026-04-02  
比较对象：

- `Mira_Released_Version`
- `/Users/Zhuanz/Documents/Github/Mira-AI-that-sees-you`

排除项：

- `.git/**`
- `.DS_Store`

## 1. 结论摘要

结论：两个目录**不完全一致**，而且差异较大。

它们共享同一批基础骨架，但已经明显分叉：

- `Mira_Released_Version` 更像一个“发布版/迁移包导向”的仓库，最大的独有内容集中在 `migration-bundles/`
- `Mira-AI-that-sees-you` 更像一个“持续开发中的主仓库”，包含更多运行态、部署、导出包、适配器、额外文档与服务
- 共享路径上的很多文件也已经被修改，因此不能视为简单的重命名或轻微整理

## 2. 统计结果

| 指标 | 数值 |
| --- | ---: |
| `Mira_Released_Version` 文件数 | 347 |
| `Mira-AI-that-sees-you` 文件数 | 238 |
| 同路径文件数 | 122 |
| 同路径且内容完全相同 | 47 |
| 同路径但内容不同 | 75 |
| 仅 `Mira_Released_Version` 独有文件 | 225 |
| 仅 `Mira-AI-that-sees-you` 独有文件 | 116 |
| 仅 `Mira_Released_Version` 独有目录 | 131 |
| 仅 `Mira-AI-that-sees-you` 独有目录 | 39 |

## 3. 相似率口径

为避免“相似率”含义不清，这里给出 3 个口径：

| 口径 | 定义 | 结果 |
| --- | --- | ---: |
| 路径重合率 | `同路径文件数 / 文件路径并集数` | 26.35% |
| 完全一致文件率 | `内容完全相同的文件数 / 文件路径并集数` | 10.15% |
| 按字节加权的完全一致率 | `完全相同文件字节数 / 全部路径最大字节数总和` | 3.22% |

推荐解读：

- 如果你关心“结构上像不像”，看 `26.35%`
- 如果你关心“真正完全一样的内容有多少”，看 `10.15%`
- 如果你关心“按内容体量算有多少真正重合”，看 `3.22%`

## 4. 差异概览

### 4.1 仅在某一侧出现的文件分布

仅 `Mira_Released_Version` 独有文件分布：

| 路径前缀 | 文件数 |
| --- | ---: |
| `migration-bundles` | 224 |
| 根目录 `LICENSE.placeholder.md` | 1 |

仅 `Mira-AI-that-sees-you` 独有文件分布：

| 路径前缀 | 文件数 |
| --- | ---: |
| `exports` | 46 |
| `modules` | 22 |
| `scripts` | 9 |
| `services` | 9 |
| `docs` | 8 |
| `deploy` | 6 |
| `image` | 6 |
| `core` | 4 |
| 根目录文件 | 6 |

`Mira-AI-that-sees-you` 根目录独有文件：

```text
.dockerignore
Dockerfile
LICENSE
Procfile
compose.yaml
render.yaml
```

### 4.2 同名但内容不同的文件分布

| 路径前缀 | 文件数 |
| --- | ---: |
| `core` | 15 |
| `modules` | 13 |
| `readme` | 10 |
| `services` | 10 |
| `deploy` | 7 |
| `docs` | 7 |
| `examples` | 5 |
| `scripts` | 3 |
| 根目录文件 | 3 |
| `apps` | 1 |
| `hardware` | 1 |

根目录中同名但内容不同的文件：

```text
.gitignore
README.md
package.json
```

## 5. 目录级新增 / 删除差异

这一节**只列目录路径差异**，不列单个新增/删除文件。

### 5.1 顶层目录差异摘要

仅 `Mira_Released_Version` 独有的顶层目录：

```text
migration-bundles
```

仅 `Mira-AI-that-sees-you` 独有的关键目录分支：

```text
deploy/mira-openclaw
docs/plans
docs/superpowers
exports
image
modules/home-assistant/direct-adapters
modules/home-assistant/docs/ecosystems
services/lingzhu-live-adapter
```

### 5.2 仅在 Mira_Released_Version 出现的目录清单

```text
migration-bundles
migration-bundles/mira-home-ecosystem-migration-pack
migration-bundles/mira-home-ecosystem-migration-pack/prototype-source
migration-bundles/mira-home-ecosystem-migration-pack/prototype-source/OpenClaw
migration-bundles/mira-home-ecosystem-migration-pack/prototype-source/OpenClaw/devbox
migration-bundles/mira-home-ecosystem-migration-pack/prototype-source/OpenClaw/devbox/project
migration-bundles/mira-home-ecosystem-migration-pack/prototype-source/OpenClaw/devbox/project/openclaw-ha-blueprint-memory
migration-bundles/mira-home-ecosystem-migration-pack/prototype-source/OpenClaw/devbox/project/openclaw-ha-blueprint-memory/plugins
migration-bundles/mira-home-ecosystem-migration-pack/prototype-source/OpenClaw/devbox/project/openclaw-ha-blueprint-memory/plugins/openclaw-plugin-alexa
migration-bundles/mira-home-ecosystem-migration-pack/prototype-source/OpenClaw/devbox/project/openclaw-ha-blueprint-memory/plugins/openclaw-plugin-alexa/skills
migration-bundles/mira-home-ecosystem-migration-pack/prototype-source/OpenClaw/devbox/project/openclaw-ha-blueprint-memory/plugins/openclaw-plugin-alexa/skills/alexa-readiness
migration-bundles/mira-home-ecosystem-migration-pack/prototype-source/OpenClaw/devbox/project/openclaw-ha-blueprint-memory/plugins/openclaw-plugin-alexa/src
migration-bundles/mira-home-ecosystem-migration-pack/prototype-source/OpenClaw/devbox/project/openclaw-ha-blueprint-memory/plugins/openclaw-plugin-alexa/src/__tests__
migration-bundles/mira-home-ecosystem-migration-pack/prototype-source/OpenClaw/devbox/project/openclaw-ha-blueprint-memory/plugins/openclaw-plugin-google-home
migration-bundles/mira-home-ecosystem-migration-pack/prototype-source/OpenClaw/devbox/project/openclaw-ha-blueprint-memory/plugins/openclaw-plugin-google-home/skills
migration-bundles/mira-home-ecosystem-migration-pack/prototype-source/OpenClaw/devbox/project/openclaw-ha-blueprint-memory/plugins/openclaw-plugin-google-home/skills/google-home-direct
migration-bundles/mira-home-ecosystem-migration-pack/prototype-source/OpenClaw/devbox/project/openclaw-ha-blueprint-memory/plugins/openclaw-plugin-google-home/src
migration-bundles/mira-home-ecosystem-migration-pack/prototype-source/OpenClaw/devbox/project/openclaw-ha-blueprint-memory/plugins/openclaw-plugin-google-home/src/__tests__
migration-bundles/mira-home-ecosystem-migration-pack/prototype-source/OpenClaw/devbox/project/openclaw-ha-blueprint-memory/plugins/openclaw-plugin-ha-control
migration-bundles/mira-home-ecosystem-migration-pack/prototype-source/OpenClaw/devbox/project/openclaw-ha-blueprint-memory/plugins/openclaw-plugin-ha-control/skills
migration-bundles/mira-home-ecosystem-migration-pack/prototype-source/OpenClaw/devbox/project/openclaw-ha-blueprint-memory/plugins/openclaw-plugin-ha-control/skills/home-assistant-control
migration-bundles/mira-home-ecosystem-migration-pack/prototype-source/OpenClaw/devbox/project/openclaw-ha-blueprint-memory/plugins/openclaw-plugin-ha-control/src
migration-bundles/mira-home-ecosystem-migration-pack/prototype-source/OpenClaw/devbox/project/openclaw-ha-blueprint-memory/plugins/openclaw-plugin-ha-control/src/__tests__
migration-bundles/mira-home-ecosystem-migration-pack/prototype-source/OpenClaw/devbox/project/openclaw-ha-blueprint-memory/plugins/openclaw-plugin-hue
migration-bundles/mira-home-ecosystem-migration-pack/prototype-source/OpenClaw/devbox/project/openclaw-ha-blueprint-memory/plugins/openclaw-plugin-hue/skills
migration-bundles/mira-home-ecosystem-migration-pack/prototype-source/OpenClaw/devbox/project/openclaw-ha-blueprint-memory/plugins/openclaw-plugin-hue/skills/hue-direct
migration-bundles/mira-home-ecosystem-migration-pack/prototype-source/OpenClaw/devbox/project/openclaw-ha-blueprint-memory/plugins/openclaw-plugin-hue/src
migration-bundles/mira-home-ecosystem-migration-pack/prototype-source/OpenClaw/devbox/project/openclaw-ha-blueprint-memory/plugins/openclaw-plugin-hue/src/__tests__
migration-bundles/mira-home-ecosystem-migration-pack/prototype-source/OpenClaw/devbox/project/openclaw-ha-blueprint-memory/plugins/openclaw-plugin-lutron
migration-bundles/mira-home-ecosystem-migration-pack/prototype-source/OpenClaw/devbox/project/openclaw-ha-blueprint-memory/plugins/openclaw-plugin-lutron/skills
migration-bundles/mira-home-ecosystem-migration-pack/prototype-source/OpenClaw/devbox/project/openclaw-ha-blueprint-memory/plugins/openclaw-plugin-lutron/skills/lutron-direct
migration-bundles/mira-home-ecosystem-migration-pack/prototype-source/OpenClaw/devbox/project/openclaw-ha-blueprint-memory/plugins/openclaw-plugin-lutron/src
migration-bundles/mira-home-ecosystem-migration-pack/prototype-source/OpenClaw/devbox/project/openclaw-ha-blueprint-memory/plugins/openclaw-plugin-lutron/src/__tests__
migration-bundles/mira-home-ecosystem-migration-pack/prototype-source/OpenClaw/devbox/project/openclaw-ha-blueprint-memory/plugins/openclaw-plugin-smartthings
migration-bundles/mira-home-ecosystem-migration-pack/prototype-source/OpenClaw/devbox/project/openclaw-ha-blueprint-memory/plugins/openclaw-plugin-smartthings/skills
migration-bundles/mira-home-ecosystem-migration-pack/prototype-source/OpenClaw/devbox/project/openclaw-ha-blueprint-memory/plugins/openclaw-plugin-smartthings/skills/smartthings-direct
migration-bundles/mira-home-ecosystem-migration-pack/prototype-source/OpenClaw/devbox/project/openclaw-ha-blueprint-memory/plugins/openclaw-plugin-smartthings/src
migration-bundles/mira-home-ecosystem-migration-pack/prototype-source/OpenClaw/devbox/project/openclaw-ha-blueprint-memory/plugins/openclaw-plugin-smartthings/src/__tests__
migration-bundles/mira-home-ecosystem-migration-pack/prototype-source/Readme
migration-bundles/mira-home-ecosystem-migration-pack/prototype-source/docs
migration-bundles/mira-home-ecosystem-migration-pack/release-source
migration-bundles/mira-home-ecosystem-migration-pack/release-source/Mira_Released_Version
migration-bundles/mira-home-ecosystem-migration-pack/release-source/Mira_Released_Version/core
migration-bundles/mira-home-ecosystem-migration-pack/release-source/Mira_Released_Version/core/openclaw-config
migration-bundles/mira-home-ecosystem-migration-pack/release-source/Mira_Released_Version/core/workspace
migration-bundles/mira-home-ecosystem-migration-pack/release-source/Mira_Released_Version/deploy
migration-bundles/mira-home-ecosystem-migration-pack/release-source/Mira_Released_Version/deploy/module-home-assistant
migration-bundles/mira-home-ecosystem-migration-pack/release-source/Mira_Released_Version/deploy/service-notification-router
migration-bundles/mira-home-ecosystem-migration-pack/release-source/Mira_Released_Version/docs
migration-bundles/mira-home-ecosystem-migration-pack/release-source/Mira_Released_Version/docs/migration
migration-bundles/mira-home-ecosystem-migration-pack/release-source/Mira_Released_Version/examples
migration-bundles/mira-home-ecosystem-migration-pack/release-source/Mira_Released_Version/examples/home-stack
migration-bundles/mira-home-ecosystem-migration-pack/release-source/Mira_Released_Version/examples/home-stack-with-notification-router
migration-bundles/mira-home-ecosystem-migration-pack/release-source/Mira_Released_Version/examples/service-notification-router
migration-bundles/mira-home-ecosystem-migration-pack/release-source/Mira_Released_Version/modules
migration-bundles/mira-home-ecosystem-migration-pack/release-source/Mira_Released_Version/modules/home-assistant
migration-bundles/mira-home-ecosystem-migration-pack/release-source/Mira_Released_Version/modules/home-assistant/config
migration-bundles/mira-home-ecosystem-migration-pack/release-source/Mira_Released_Version/modules/home-assistant/docs
migration-bundles/mira-home-ecosystem-migration-pack/release-source/Mira_Released_Version/modules/home-assistant/plugin
migration-bundles/mira-home-ecosystem-migration-pack/release-source/Mira_Released_Version/modules/home-assistant/plugin/src
migration-bundles/mira-home-ecosystem-migration-pack/release-source/Mira_Released_Version/modules/home-assistant/plugin/src/policies
migration-bundles/mira-home-ecosystem-migration-pack/release-source/Mira_Released_Version/modules/home-assistant/plugin/src/registry
migration-bundles/mira-home-ecosystem-migration-pack/release-source/Mira_Released_Version/modules/home-assistant/plugin/src/scenes
migration-bundles/mira-home-ecosystem-migration-pack/release-source/Mira_Released_Version/modules/home-assistant/registry
migration-bundles/mira-home-ecosystem-migration-pack/release-source/Mira_Released_Version/services
migration-bundles/mira-home-ecosystem-migration-pack/release-source/Mira_Released_Version/services/notification-router
migration-bundles/mira-home-ecosystem-migration-pack/release-source/Mira_Released_Version/services/notification-router/config
migration-bundles/mira-home-ecosystem-migration-pack/release-source/Mira_Released_Version/services/notification-router/docs
migration-bundles/mira-home-ecosystem-migration-pack/release-source/Mira_Released_Version/services/notification-router/src
migration-bundles/mira-home-ecosystem-migration-pack/release-source/Mira_Released_Version/services/notification-router/src/__tests__
migration-bundles/mira-home-ecosystem-migration-pack/release-source/Mira_Released_Version/services/notification-router/src/channels
migration-bundles/mira-home-ecosystem-migration-pack/release-source/Mira_Released_Version/services/notification-router/src/config
migration-bundles/mira-home-ecosystem-migration-pack/release-source/Mira_Released_Version/services/notification-router/src/dispatch
migration-bundles/mira-home-ecosystem-migration-pack/release-source/Mira_Released_Version/services/notification-router/src/policy
migration-bundles/mira-home-ecosystem-migration-pack/release-source/Mira_Released_Version/services/notification-router/src/routes
migration-bundles/mira-released-version-repo
migration-bundles/mira-released-version-repo/apps
migration-bundles/mira-released-version-repo/core
migration-bundles/mira-released-version-repo/core/examples
migration-bundles/mira-released-version-repo/core/openclaw-config
migration-bundles/mira-released-version-repo/core/persona
migration-bundles/mira-released-version-repo/core/plugins
migration-bundles/mira-released-version-repo/core/plugins/lingzhu-bridge
migration-bundles/mira-released-version-repo/core/plugins/lingzhu-bridge/src
migration-bundles/mira-released-version-repo/core/plugins/lingzhu-bridge/tests
migration-bundles/mira-released-version-repo/core/skills
migration-bundles/mira-released-version-repo/core/workspace
migration-bundles/mira-released-version-repo/deploy
migration-bundles/mira-released-version-repo/deploy/core
migration-bundles/mira-released-version-repo/deploy/minimal
migration-bundles/mira-released-version-repo/deploy/module-home-assistant
migration-bundles/mira-released-version-repo/deploy/service-notification-router
migration-bundles/mira-released-version-repo/docs
migration-bundles/mira-released-version-repo/docs/architecture
migration-bundles/mira-released-version-repo/docs/migration
migration-bundles/mira-released-version-repo/examples
migration-bundles/mira-released-version-repo/examples/home-stack
migration-bundles/mira-released-version-repo/examples/home-stack-with-notification-router
migration-bundles/mira-released-version-repo/examples/minimal-core
migration-bundles/mira-released-version-repo/examples/service-notification-router
migration-bundles/mira-released-version-repo/hardware
migration-bundles/mira-released-version-repo/modules
migration-bundles/mira-released-version-repo/modules/home-assistant
migration-bundles/mira-released-version-repo/modules/home-assistant/config
migration-bundles/mira-released-version-repo/modules/home-assistant/docs
migration-bundles/mira-released-version-repo/modules/home-assistant/plugin
migration-bundles/mira-released-version-repo/modules/home-assistant/plugin/src
migration-bundles/mira-released-version-repo/modules/home-assistant/plugin/src/policies
migration-bundles/mira-released-version-repo/modules/home-assistant/plugin/src/registry
migration-bundles/mira-released-version-repo/modules/home-assistant/plugin/src/scenes
migration-bundles/mira-released-version-repo/modules/home-assistant/registry
migration-bundles/mira-released-version-repo/readme
migration-bundles/mira-released-version-repo/readme/00-overview
migration-bundles/mira-released-version-repo/readme/10-core
migration-bundles/mira-released-version-repo/readme/20-modules
migration-bundles/mira-released-version-repo/readme/30-hardware
migration-bundles/mira-released-version-repo/readme/40-deploy
migration-bundles/mira-released-version-repo/readme/50-development
migration-bundles/mira-released-version-repo/scripts
migration-bundles/mira-released-version-repo/scripts/__tests__
migration-bundles/mira-released-version-repo/services
migration-bundles/mira-released-version-repo/services/notification-router
migration-bundles/mira-released-version-repo/services/notification-router/config
migration-bundles/mira-released-version-repo/services/notification-router/docs
migration-bundles/mira-released-version-repo/services/notification-router/src
migration-bundles/mira-released-version-repo/services/notification-router/src/__tests__
migration-bundles/mira-released-version-repo/services/notification-router/src/channels
migration-bundles/mira-released-version-repo/services/notification-router/src/config
migration-bundles/mira-released-version-repo/services/notification-router/src/dispatch
migration-bundles/mira-released-version-repo/services/notification-router/src/policy
migration-bundles/mira-released-version-repo/services/notification-router/src/routes
```

### 5.3 仅在 Mira-AI-that-sees-you 出现的目录清单

```text
deploy/mira-openclaw
docs/plans
docs/superpowers
docs/superpowers/plans
docs/superpowers/specs
exports
exports/mira-mi-band-gateway-pack
exports/mira-mi-band-gateway-pack/source
exports/mira-mi-band-gateway-pack/source/devices
exports/mira-mi-band-gateway-pack/source/devices/mi-band-9-pro
exports/mira-mi-band-gateway-pack/source/devices/mi-band-9-pro/gateway
exports/mira-mi-band-gateway-pack/source/devices/mi-band-9-pro/gateway/android-app
exports/mira-mi-band-gateway-pack/source/devices/mi-band-9-pro/gateway/android-app/app
exports/mira-mi-band-gateway-pack/source/devices/mi-band-9-pro/gateway/android-app/app/src
exports/mira-mi-band-gateway-pack/source/devices/mi-band-9-pro/gateway/android-app/app/src/main
exports/mira-mi-band-gateway-pack/source/devices/mi-band-9-pro/gateway/android-app/app/src/main/java
exports/mira-mi-band-gateway-pack/source/devices/mi-band-9-pro/gateway/android-app/app/src/main/java/com
exports/mira-mi-band-gateway-pack/source/devices/mi-band-9-pro/gateway/android-app/app/src/main/java/com/javis
exports/mira-mi-band-gateway-pack/source/devices/mi-band-9-pro/gateway/android-app/app/src/main/java/com/javis/wearable
exports/mira-mi-band-gateway-pack/source/devices/mi-band-9-pro/gateway/android-app/app/src/main/java/com/javis/wearable/gateway
exports/mira-mi-band-gateway-pack/source/devices/mi-band-9-pro/gateway/desktop
exports/mira-mi-band-gateway-pack/source/tools
exports/mira-mi-band-gateway-pack/source/tools/mi_band_desktop_bridge
exports/mira-mi-band-gateway-pack/source/tools/mi_band_desktop_bridge/openclaw_band_plugin
exports/mira-mi-printer-bridge-pack
exports/mira-mi-printer-bridge-pack/source
exports/mira-mi-printer-bridge-pack/source/docs
exports/mira-mi-printer-bridge-pack/source/docs/printer-bridge
exports/mira-mi-printer-bridge-pack/source/tools
exports/mira-mi-printer-bridge-pack/source/tools/printer_bridge
exports/mira-mi-printer-bridge-pack/source/tools/printer_bridge/openclaw_printer_plugin
image
image/README
modules/home-assistant/direct-adapters
modules/home-assistant/direct-adapters/hue
modules/home-assistant/direct-adapters/hue/src
modules/home-assistant/docs/ecosystems
services/lingzhu-live-adapter
services/lingzhu-live-adapter/src
```

## 6. 同名但内容不同的文件清单

下面这些文件在两个目录中**路径相同**，但**内容不一致**：

```text
.gitignore
README.md
apps/README.md
core/README.md
core/examples/README.md
core/openclaw-config/README.md
core/openclaw-config/lingzhu-config-snippet.example.json5
core/openclaw-config/lingzhu-system-prompt.txt
core/openclaw-config/minimal-runtime-contract.md
core/openclaw-config/openclaw.example.json
core/persona/README.md
core/plugins/README.md
core/plugins/lingzhu-bridge/README.md
core/plugins/lingzhu-bridge/package-lock.json
core/plugins/lingzhu-bridge/package.json
core/skills/README.md
core/workspace/AGENTS.md
core/workspace/README.md
deploy/README.md
deploy/core/README.md
deploy/deploy-paths-overview.md
deploy/minimal/README.md
deploy/module-home-assistant/README.md
deploy/service-notification-router/README.md
deploy/service-notification-router/env.example
docs/README.md
docs/architecture/README.md
docs/migration/README.md
docs/migration/open-source-readiness-checklist.md
docs/migration/package-and-license-decisions.md
docs/migration/repository-split-checklist.md
docs/migration/repository-split-readiness.md
examples/README.md
examples/home-stack-with-notification-router/README.md
examples/home-stack/README.md
examples/minimal-core/README.md
examples/service-notification-router/README.md
hardware/README.md
modules/README.md
modules/home-assistant/README.md
modules/home-assistant/config/README.md
modules/home-assistant/config/home-assistant-module.example.json
modules/home-assistant/docs/README.md
modules/home-assistant/docs/module-runtime-contract.md
modules/home-assistant/docs/package-assembly-checklist.md
modules/home-assistant/plugin/README.md
modules/home-assistant/plugin/package.json
modules/home-assistant/plugin/src/README.md
modules/home-assistant/plugin/src/registry/loadDevicesRegistry.ts
modules/home-assistant/registry/README.md
modules/home-assistant/registry/devices.example.json
package.json
readme/00-overview/README.md
readme/00-overview/getting-started.md
readme/00-overview/quick-start.md
readme/10-core/README.md
readme/20-modules/README.md
readme/30-hardware/README.md
readme/40-deploy/README.md
readme/50-development/README.md
readme/50-development/contributing-and-migration.md
readme/README.md
scripts/__tests__/export-release-repo.test.mjs
scripts/__tests__/verify-release.test.mjs
scripts/verify-release.mjs
services/README.md
services/notification-router/README.md
services/notification-router/config/README.md
services/notification-router/docs/README.md
services/notification-router/package-lock.json
services/notification-router/package.json
services/notification-router/src/README.md
services/notification-router/src/__tests__/notification-router.test.ts
services/notification-router/src/channels/openclawChannelDm.ts
services/notification-router/src/server.ts
```

## 7. 完全相同的文件清单

下面这些文件在两个目录中**路径相同且内容完全一致**：

```text
CHANGELOG.md
CONTRIBUTING.md
core/openclaw-config/agent-defaults-snippet.json5
core/openclaw-config/custom-right-codes-vision-snippet.example.json5
core/persona/IDENTITY.md
core/persona/SOUL.md
core/plugins/lingzhu-bridge/.gitignore
core/plugins/lingzhu-bridge/src/first-turn-opening.ts
core/plugins/lingzhu-bridge/src/memory-context.ts
core/plugins/lingzhu-bridge/src/types.ts
core/plugins/lingzhu-bridge/tests/first-turn-opening.test.mts
core/plugins/lingzhu-bridge/tests/memory-context.test.mts
core/workspace/MEMORY.md
core/workspace/OUTBOUND_POLICY.md
core/workspace/TOOLS.md
deploy/core/env.example
deploy/module-home-assistant/env.example
deploy/service-notification-router/.gitignore
deploy/service-notification-router/check-health.sh
deploy/service-notification-router/dispatch-self-checkin.sh
deploy/service-notification-router/start-local.sh
docs/migration/release-baseline.md
docs/migration/source-to-release-mapping.md
modules/home-assistant/docs/scene-resolver-policy-coordination-spec.md
modules/home-assistant/plugin/src/policies/confirmationPolicy.ts
modules/home-assistant/plugin/src/policies/outboundPolicyAdapter.ts
modules/home-assistant/plugin/src/policies/riskPolicy.ts
modules/home-assistant/plugin/src/scenes/sceneDefinitions.ts
modules/home-assistant/plugin/src/scenes/scenePlanExecutor.ts
modules/home-assistant/plugin/src/scenes/sceneResolver.ts
modules/home-assistant/plugin/tsconfig.json
scripts/export-release-repo.mjs
services/notification-router/.gitignore
services/notification-router/config/env.example
services/notification-router/config/outbound-policy.example.yaml
services/notification-router/docs/operator-checklist.md
services/notification-router/docs/runtime-contract.md
services/notification-router/src/channels/resendEmail.ts
services/notification-router/src/config/routerConfig.ts
services/notification-router/src/dispatch/dispatchMessageIntent.ts
services/notification-router/src/policy/defaultOutboundPolicy.ts
services/notification-router/src/policy/outboundPolicyEvaluator.ts
services/notification-router/src/policy/outboundPolicyLoader.ts
services/notification-router/src/policy/outboundPolicyTypes.ts
services/notification-router/src/routes/dispatchIntent.ts
services/notification-router/src/types.ts
services/notification-router/tsconfig.json
```

## 8. 结构性观察

从目录与文件变化看，两个仓库的定位已经不同：

- `Mira_Released_Version` 重点集中在 `migration-bundles/`，明显偏向“迁移包、整理包、发布基线”
- `Mira-AI-that-sees-you` 多出完整运行与部署周边，例如 `Dockerfile`、`compose.yaml`、`render.yaml`、`Procfile`
- `Mira-AI-that-sees-you` 多出功能模块与运行服务，例如 `services/lingzhu-live-adapter/`、`modules/home-assistant/direct-adapters/hue/`
- `Mira-AI-that-sees-you` 多出导出包与设备桥接内容，例如 `exports/mira-mi-band-gateway-pack/` 与 `exports/mira-mi-printer-bridge-pack/`
- 大量共享路径文件被改写，说明它不是简单地从一个目录复制出来后只做了增删，而是共享骨架上持续演进出的另一条分支

## 9. 建议解读

如果你的目标是判断“是不是完全一样”，答案很明确：**不是**。

如果你的目标是判断“是否还能认为它们属于同一个项目谱系”，答案是：**是的，仍然能看出同一骨架来源，但演化方向已经明显不同**。

如果后续需要更细的比较，下一步最有价值的是：

1. 对 `75` 个同名但内容不同的文件再做逐文件 diff
2. 重点先看 `package.json`、`README.md`、`core/`、`modules/`、`services/` 这几组
3. 如果你想判断“能否合并”或“谁是另一个的超集”，还需要再做一版语义级别的对比
