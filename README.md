# Mira Light Released Version

**中文**

`Mira-Light-AI-That-Sees-You` 现在承载的是 `Mira_Light_Released_Version` 的当前发布内容。  
这个仓库的目标不是继续保存所有原型期上下文，而是提供一个更像独立可交付仓库的版本，把已经整理好的：

- 四关节台灯场景编排
- 本地 bridge
- 导演台 console
- 最简 receiver
- OpenClaw 插件接入
- 安全控制与回滚脚本
- release 文档、runbook、fixture、测试

统一放进一个可独立拆出、独立部署、独立维护的代码库里。

当前推荐的控制链是：

```text
browser
-> director console (127.0.0.1:8765)
-> local bridge (127.0.0.1:9783)
-> real lamp or dry-run runtime
```

并保留一个独立 receiver：

```text
device / camera sender
-> simple receiver (127.0.0.1:9784)
```

这意味着：

- console 只连接 bridge，不直接连灯
- 灯地址、dry-run、memoryContext 等配置都属于 bridge/runtime 配置
- 第一次启动时，优先使用本地一键安装和 preflight 路径

## 快速开始

```bash
cd Mira-Light-AI-That-Sees-You
bash scripts/one_click_install.sh
```

或者：

```bash
npm run bootstrap
```

之后建议按这个顺序：

1. 离线 preflight

```bash
bash scripts/run_preflight_release.sh offline
```

2. 如有真机，设置灯地址

```bash
export MIRA_LIGHT_LAMP_BASE_URL=http://172.20.10.3
```

3. 启动完整本地栈

```bash
bash scripts/start_local_stack.sh
```

4. 打开导演台

```text
http://127.0.0.1:8765/
```

## 与云端 Mira 的关系

这个仓库现在不仅是 release 版控制栈，也已经包含了第一版 **embodied memory producer**。

也就是说，`Mira-Light` 不再只是一个“被控制的设备桥”，它也可以把以下内容写入云端 `memory-context`：

- scene success / failure
- selected device status
- selected device warning / error events

关键文件：

- [tools/mira_light_bridge/embodied_memory_client.py](./tools/mira_light_bridge/embodied_memory_client.py)
- [tools/mira_light_bridge/bridge_server.py](./tools/mira_light_bridge/bridge_server.py)
- [scripts/mira_light_runtime.py](./scripts/mira_light_runtime.py)
- [tests/test_embodied_memory.py](./tests/test_embodied_memory.py)

相关说明文档：

- [docs/mira-context-proactivity-architecture.md](./docs/mira-context-proactivity-architecture.md)
- [docs/mira-light-embodied-memory-integration-2026-04-09.md](./docs/mira-light-embodied-memory-integration-2026-04-09.md)

如果你把它接到 `Mira_v3`，推荐的 shared embodied user id 是：

```text
mira-light-bridge
```

## 仓库内容

- `assets/`
  发布版静态素材
- `config/`
  profile、vision schema、release config
- `deploy/`
  本地和 release 部署说明
- `docs/`
  场景、架构、runbook、handoff、integration 文档
- `fixtures/`
  vision / audio / test fixture
- `scripts/`
  runtime、receiver、preflight、诊断、安装和测试脚本
- `tests/`
  Python 测试
- `tools/mira_light_bridge/`
  bridge 与 OpenClaw 插件
- `web/`
  导演台与 scene showcase 前端

## 一句话总结

这个仓库现在应该被理解成：

> `Mira-Light` 的独立 release 仓库，同时也是云端 Mira 的 embodied scene/device context producer。

## License

本仓库使用：

- `GNU Affero General Public License v3.0`
- SPDX: `AGPL-3.0-only`

---

**English**

`Mira-Light-AI-That-Sees-You` now carries the current contents of
`Mira_Light_Released_Version`.

This repository is meant to act like an independent release repository rather
than a prototype dump. It packages the current deliverable surface for:

- four-DOF lamp scene choreography
- the local bridge
- the director console
- the minimal receiver
- OpenClaw plugin integration
- safety / rollback scripts
- release documentation, fixtures, and tests

The current control path is:

```text
browser
-> director console (127.0.0.1:8765)
-> local bridge (127.0.0.1:9783)
-> real lamp or dry-run runtime
```

And the standalone receiver path is:

```text
device / camera sender
-> simple receiver (127.0.0.1:9784)
```

This means:

- the console talks only to the bridge
- lamp address, dry-run mode, and memoryContext behavior belong to bridge/runtime config
- the first-run path should prefer the local one-click install plus preflight flow

## Quick Start

```bash
cd Mira-Light-AI-That-Sees-You
bash scripts/one_click_install.sh
```

Or:

```bash
npm run bootstrap
```

Recommended first-run order:

1. Offline preflight

```bash
bash scripts/run_preflight_release.sh offline
```

2. If using a real lamp, set the lamp base URL

```bash
export MIRA_LIGHT_LAMP_BASE_URL=http://172.20.10.3
```

3. Start the local stack

```bash
bash scripts/start_local_stack.sh
```

4. Open the director console

```text
http://127.0.0.1:8765/
```

## Relationship To Cloud Mira

This repository is no longer only a release control stack. It now also
contains a first-pass **embodied memory producer**.

That means `Mira-Light` can now write selected outcomes into cloud Mira's
`memory-context`, including:

- scene success / failure
- selected device status
- selected warning / error events

Key files:

- [tools/mira_light_bridge/embodied_memory_client.py](./tools/mira_light_bridge/embodied_memory_client.py)
- [tools/mira_light_bridge/bridge_server.py](./tools/mira_light_bridge/bridge_server.py)
- [scripts/mira_light_runtime.py](./scripts/mira_light_runtime.py)
- [tests/test_embodied_memory.py](./tests/test_embodied_memory.py)

Companion docs:

- [docs/mira-context-proactivity-architecture.md](./docs/mira-context-proactivity-architecture.md)
- [docs/mira-light-embodied-memory-integration-2026-04-09.md](./docs/mira-light-embodied-memory-integration-2026-04-09.md)

If paired with `Mira_v3`, the recommended shared embodied writer id is:

```text
mira-light-bridge
```

## Repository Layout

- `assets/`
  release assets
- `config/`
  profiles, schemas, release config
- `deploy/`
  deployment and local-stack docs
- `docs/`
  architecture, scene, runbook, handoff, and integration docs
- `fixtures/`
  test fixtures
- `scripts/`
  runtime, receiver, diagnostics, install, and test scripts
- `tests/`
  Python tests
- `tools/mira_light_bridge/`
  bridge and OpenClaw plugin
- `web/`
  director console and scene showcase frontend

## One-Sentence Summary

This repository should now be read as:

> an independent release repository for Mira Light, and an embodied scene/device context producer for cloud Mira.

## License

This repository is licensed under:

- `GNU Affero General Public License v3.0`
- SPDX: `AGPL-3.0-only`
