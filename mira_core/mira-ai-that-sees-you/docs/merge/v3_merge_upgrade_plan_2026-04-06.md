# V3 Merge Upgrade Plan

版本：v3  
日期：2026-04-06  
文档目的：将 `Mira_Released_Version` 与当前 GitHub 开发版 `/Users/Zhuanz/Documents/Github/Mira-AI-that-sees-you` 进行有控制的合并，形成一个基于现有 GitHub 主线的升级版仓库。  
配套参考文档：`docs/diff_report.md`

## 1. 背景

根据前期对比结果：

- `Mira_Released_Version` 更偏向发布版、迁移包和整理包
- `Mira-AI-that-sees-you` 更偏向持续开发中的主仓库，拥有更多运行态、部署能力、服务能力和导出能力
- 两者不是简单的镜像关系，而是在同一骨架上演进出的两个分支
- 共享路径上存在大量同名但内容不同的文件，因此不能直接做整目录覆盖

本计划的核心目标，不是“把两个版本硬拼在一起”，而是：

- 以当前 GitHub 开发版为唯一主线
- 吸收 `Mira_Released_Version` 中真正有价值、且不会破坏现有运行能力的部分
- 最终形成一个“开发可运行、发布可交付、迁移可追踪”的升级版

## 2. 目标定义

本次合并完成后，目标仓库应满足以下条件：

- 继续以 GitHub 开发版的结构和运行方式为主
- 保留当前开发版已有的运行服务、部署脚本、workspace、导出包和适配器
- 引入 `Mira_Released_Version` 中的 `migration-bundles/` 及其发布资产
- 对公共路径文件进行人工合并，避免把当前开发版回退成旧版
- 形成一套可复现、可审查、可回滚的升级流程

### 2.1 成功标准

这次升级不是“文件更多了”就算成功，而是要同时满足以下 5 条：

- 成功标准 1：主仓库仍能以当前开发版方式运行
- 成功标准 2：主仓库吸收了发布版独有的迁移资产
- 成功标准 3：共享路径文件的合并结果不会让开发版功能倒退
- 成功标准 4：文档、脚本、目录、配置四者口径一致
- 成功标准 5：整个升级过程可以用 commit 历史清楚解释

### 2.2 非目标

这次升级明确**不追求**下面这些事情：

- 不追求把两个目录做成字面上的完全一致
- 不追求把所有差异文件都机械性合并
- 不追求在一次提交里完成所有改动
- 不追求让 `Mira_Released_Version` 成为新的主线仓库
- 不追求把 `migration-bundles/` 纳入现行 runtime 主路径

## 3. 主线与合并原则

### 3.1 主线仓库

唯一主线仓库：

- `/Users/Zhuanz/Documents/Github/Mira-AI-that-sees-you`

辅助来源仓库：

- `/Users/Zhuanz/Documents/Github/Javis-Hackathon/Mira_Released_Version`

结论：

- 所有最终代码、文档和提交都应落在 `Mira-AI-that-sees-you`
- `Mira_Released_Version` 仅作为内容来源，不作为覆盖基准

### 3.2 总体合并原则

- 原则 1：开发版优先于发布版
- 原则 2：运行能力优先于文档表达
- 原则 3：结构性新增优先于旧版说明
- 原则 4：同路径文件默认人工合并，不做整文件覆盖
- 原则 5：每一类改动独立提交，保持可回滚性
- 原则 6：任何会影响 runtime、workspace、deploy 的改动都必须经过验证

### 3.3 当前开发版基线快照

为了避免“合并过程中忘记主线当前长什么样”，这里把 GitHub 开发版的关键现状固定下来。

当前根级 `package.json` 已具备以下特征：

- `workspaces` 包含：
  - `core/plugins/lingzhu-bridge`
  - `modules/home-assistant/plugin`
  - `services/notification-router`
  - `services/lingzhu-live-adapter`
- `engines.node` 要求：`>=20 <26`
- 根级脚本除了 `verify:release`、`test:release`、`export:repo` 外，还包括：
  - `manifest:deploy`
  - `bootstrap`
  - `doctor`
  - `start`
  - `deploy`
  - `status`
  - `health`
  - `self-check`
  - `down`
  - 以及 `notification-router`、`mira-openclaw`、`lingzhu-live-adapter` 的子命令

当前开发版中几个关键 workspace 的现状：

- `core/plugins/lingzhu-bridge/package.json`
  - 已声明 `openclaw.extensions: ["./src/index.ts"]`
- `modules/home-assistant/plugin/package.json`
  - 已使用真实测试命令：`node --experimental-strip-types --test src/**/*.test.ts`
- `services/notification-router/package.json`
  - 已具备 `dev`、`start`、`test` 三类脚本
- `services/lingzhu-live-adapter/package.json`
  - 已作为独立 workspace 存在

这意味着：

- 根级 workspace 结构不能回退
- plugin/service 的 package manifest 不能简单被发布版覆盖
- 任何合并动作都必须保护这些当前能力

## 4. 当前差异的战略解读

基于 `docs/diff_report.md`，本次合并应当这样理解：

- `Mira_Released_Version` 的最大独特价值集中在 `migration-bundles/`
- 当前 GitHub 开发版拥有明显更强的运行态能力，例如 `Dockerfile`、`compose.yaml`、`render.yaml`、`Procfile`
- 当前 GitHub 开发版拥有更多服务与模块，例如 `services/lingzhu-live-adapter/`、`modules/home-assistant/direct-adapters/`
- 当前 GitHub 开发版拥有更多导出包与设备桥接内容，例如 `exports/`
- 同名但内容不同的文件达到 75 个，说明真正困难的地方不是“拷贝目录”，而是“合并共享区域”

因此，升级版的正确方向是：

- 以 GitHub 开发版保留现有能力
- 让发布版补充迁移、整理和发布资产
- 不允许升级过程把开发版回退成较旧的发布状态

## 5. 合并分类与处理策略

### 5.1 A 类：直接导入到主仓库

这类内容在开发版中缺失，但整体价值明确、对现有运行逻辑影响低，可以整目录导入。

推荐直接导入：

- `migration-bundles/**`

处理方式：

- 整目录导入
- 独立提交
- 导入后仅做路径与说明检查，不立即改写内部内容

### 5.2 B 类：以开发版为准，禁止用发布版覆盖

这类内容代表当前 GitHub 开发版的真实运行能力，必须保留。

必须保留开发版版本：

- 根目录 `package.json`
- 根目录 `Dockerfile`
- 根目录 `compose.yaml`
- 根目录 `render.yaml`
- 根目录 `Procfile`
- 根目录 `LICENSE`
- `services/lingzhu-live-adapter/**`
- `modules/home-assistant/direct-adapters/**`
- `exports/**`
- 当前 deploy runtime 相关脚本
- 当前 workspace 与其脚本定义

处理方式：

- 不接受发布版整文件覆盖
- 如果发布版有更好的说明文本，只吸收说明，不回退实现

### 5.3 C 类：人工合并的共享区域

这类文件和目录两边都有，但内容不同，必须人工处理。

重点人工合并区域：

- `README.md`
- `readme/**`
- `docs/migration/**`
- `docs/architecture/**`
- `core/openclaw-config/**`
- `core/workspace/**`
- `core/plugins/lingzhu-bridge/**`
- `deploy/**`
- `examples/**`
- `modules/home-assistant/**`
- `services/notification-router/**`

处理方式：

- 逐文件 diff
- 逐文件判断“保留开发版”“吸收发布版表达”“局部拼接”
- 每完成一个模块就执行测试或最小验证

### 5.4 D 类：需要特别保护的关键文件

以下文件不建议直接替换：

- `package.json`
- `core/plugins/lingzhu-bridge/package.json`
- `modules/home-assistant/plugin/package.json`
- `services/notification-router/package.json`
- `scripts/verify-release.mjs`

原因：

- 这些文件已经体现了当前 GitHub 开发版的 workspace、license、runtime script、测试方式和部署逻辑
- 发布版在这些文件上多数更像旧版或简化版，直接替换会导致能力回退

### 5.5 文件级决策算法

当你面对任意一个差异路径时，按下面的顺序判断，不要凭感觉操作。

步骤 1：先判断这个路径属于哪一类。

- 只在开发版存在
- 只在发布版存在
- 两边都存在但内容不同
- 两边都存在且内容相同

步骤 2：再判断它属于哪种语义层。

- runtime 入口
- workspace / manifest
- service / module 实现
- config / contract
- docs / examples
- release artifact / migration asset

步骤 3：套用默认处理规则。

- 开发版独有 + runtime 或 workspace：保留
- 发布版独有 + release asset：导入
- 发布版独有 + 旧式 placeholder / 旧配置：谨慎，不默认导入
- 同路径不同内容 + 代码实现：开发版优先，发布版补语义
- 同路径不同内容 + 文档：人工合并
- 同路径不同内容 + config：人工合并，先保运行

步骤 4：判断是否需要验证。

以下类型必须在改后立即验证：

- `package.json`
- `scripts/**`
- `deploy/**`
- `core/plugins/**`
- `modules/home-assistant/plugin/**`
- `services/**`

步骤 5：判断是否立即提交。

- 低风险导入型改动可以成组提交
- 高风险运行型改动必须小步提交

### 5.6 模块级处理矩阵

| 区域 | 当前主判断 | 合并策略 | 默认动作 | 风险等级 |
| --- | --- | --- | --- | --- |
| 根目录运行文件 | 开发版强于发布版 | 保护主线 | 保留开发版 | 高 |
| `migration-bundles/**` | 发布版独有核心资产 | 直接吸收 | 整目录导入 | 低 |
| `docs/**` / `readme/**` | 双方各有价值 | 文档统一 | 人工合并 | 中 |
| `core/openclaw-config/**` | 有契约差异 | 以运行为准 | 人工合并 | 高 |
| `core/workspace/**` | 开发版新增材料更多 | 保主线吸说明 | 人工合并 | 中 |
| `core/plugins/lingzhu-bridge/**` | 开发版更贴近运行态 | 保主线补语义 | 人工合并 | 高 |
| `modules/home-assistant/**` | 开发版已扩展更多 | 保主线补文档与契约 | 人工合并 | 高 |
| `services/notification-router/**` | 开发版更接近现行实现 | 保主线补说明与边界 | 人工合并 | 高 |
| `services/lingzhu-live-adapter/**` | 开发版独有 | 绝不回退 | 保留开发版 | 高 |
| `exports/**` | 开发版独有 | 保留 | 保留开发版 | 中 |
| `examples/**` | 双方都有 | 统一说明和入口 | 人工合并 | 中 |

## 6. 分阶段执行方案

### 阶段 0：准备与基线冻结

目标：

- 在不污染主分支的前提下开始合并
- 固定一个可回退的基线

操作：

```bash
cd /Users/Zhuanz/Documents/Github/Mira-AI-that-sees-you
git checkout main
git pull origin main
git status --short --branch
git checkout -b feat/upgrade-from-release-v3
```

预检命令：

```bash
node -v
npm -v
git remote -v
git branch --show-current
```

要求：

- 分支必须从最新 `main` 拉出
- 工作区必须干净
- 本次升级不得直接在 `main` 上操作

进入下一阶段前必须确认：

- `git status` 没有未提交改动
- 当前分支不是 `main`
- Node 版本满足仓库要求
- 你知道主仓库和来源仓库的绝对路径

交付物：

- 升级分支 `feat/upgrade-from-release-v3`

### 阶段 1：引入基线文档

目标：

- 把差异报告纳入主仓库，作为后续所有合并动作的依据

操作：

```bash
mkdir -p docs/merge
cp /Users/Zhuanz/Documents/Github/Javis-Hackathon/docs/diff_report.md docs/merge/diff_report_2026-04-06.md
cp /Users/Zhuanz/Documents/Github/Javis-Hackathon/docs/v_3_merge_upgrade_plan.md docs/merge/v3_merge_upgrade_plan_2026-04-06.md
git add docs/merge
git commit -m "docs: add v3 merge baseline and upgrade plan"
```

建议附加动作：

```bash
mkdir -p tmp/merge-baseline
cp /Users/Zhuanz/Documents/Github/Javis-Hackathon/docs/diff_report.md tmp/merge-baseline/
cp /Users/Zhuanz/Documents/Github/Javis-Hackathon/docs/v_3_merge_upgrade_plan.md tmp/merge-baseline/
```

这样做的作用：

- `docs/merge/` 用于进入版本控制
- `tmp/merge-baseline/` 用于执行期快速查看和比对

交付物：

- 归档到主仓库的差异报告
- 归档到主仓库的升级执行计划

### 阶段 2：导入发布版独有资产

目标：

- 把 `Mira_Released_Version` 的独有发布/迁移资产引入主仓库

首批导入范围：

- `migration-bundles/**`

操作：

```bash
cd /Users/Zhuanz/Documents/Github/Mira-AI-that-sees-you
rsync -av --dry-run /Users/Zhuanz/Documents/Github/Javis-Hackathon/Mira_Released_Version/migration-bundles/ ./migration-bundles/
rsync -av /Users/Zhuanz/Documents/Github/Javis-Hackathon/Mira_Released_Version/migration-bundles/ ./migration-bundles/
git add migration-bundles
git commit -m "chore: import release migration bundles"
```

要求：

- 此阶段不改动 runtime 代码
- 只确认目录、文件和引用路径是否完整

验收标准：

- `migration-bundles/` 已进入主仓库
- 不影响现有 workspace 与启动逻辑

阶段结束时建议执行：

```bash
find migration-bundles -maxdepth 3 -type f | sed -n '1,120p'
git diff --stat HEAD~1 HEAD
```

### 阶段 3：文档层合并

目标：

- 用统一口径描述升级后的仓库结构、运行方式和发布方式

优先处理范围：

- `README.md`
- `readme/**`
- `docs/migration/**`
- `docs/architecture/**`
- `examples/**`

推荐方法：

```bash
diff -u /Users/Zhuanz/Documents/Github/Javis-Hackathon/Mira_Released_Version/README.md README.md
diff -u /Users/Zhuanz/Documents/Github/Javis-Hackathon/Mira_Released_Version/readme/README.md readme/README.md
diff -u /Users/Zhuanz/Documents/Github/Javis-Hackathon/Mira_Released_Version/docs/migration/repository-split-checklist.md docs/migration/repository-split-checklist.md
```

合并规则：

- 以开发版现状为事实基础
- 吸收发布版更清晰的术语、边界说明和交付描述
- 不允许文档把开发版已有功能写没
- 新增文档时，优先把发布版内容改写成“升级版现状”口径

推荐优先级：

- 第一优先级：顶层定位文档
  - `README.md`
  - `readme/README.md`
- 第二优先级：迁移与发布说明
  - `docs/migration/**`
  - `readme/50-development/contributing-and-migration.md`
- 第三优先级：结构与使用路径说明
  - `readme/00-overview/**`
  - `readme/40-deploy/**`
  - `examples/**`

文档合并时的检查问题：

- 文中提到的脚本今天还存在吗
- 文中提到的目录今天还存在吗
- 文中提到的服务是现役服务还是历史资产
- 文中是否把 `migration-bundles/` 错写成主运行路径
- 文中是否遗漏了 `services/lingzhu-live-adapter/`、`exports/`、`direct-adapters/`

建议提交拆分：

- `docs: reconcile top-level readme`
- `docs: merge migration and architecture guidance`
- `docs: align examples with upgraded repo structure`

验收标准：

- 顶层 README 与 readme 子文档不相互冲突
- 文档中出现的目录、脚本和服务在主仓库中真实存在

### 阶段 4：配置与契约层合并

目标：

- 对齐运行契约、配置契约、部署契约与工作区说明

优先处理范围：

- `core/openclaw-config/**`
- `core/workspace/**`
- `deploy/**`
- `modules/home-assistant/config/**`
- `modules/home-assistant/docs/**`

处理原则：

- 配置文件以开发版可运行性为最高优先级
- 发布版中的说明、注释和契约语义可以吸收
- 如果某项配置被开发版新增脚本依赖，则不能回退

建议按下面顺序处理：

1. 根级 `package.json`
2. `core/openclaw-config/**`
3. `core/workspace/**`
4. `deploy/**`
5. `modules/home-assistant/config/**`
6. `modules/home-assistant/docs/**`

为什么这个顺序更稳：

- 先锁定 manifest 和 workspace
- 再统一 core contract
- 再检查 deploy
- 最后再看 module 文档与配置

这里最重要的具体事实：

- 开发版根 `package.json` 比发布版多出 `services/lingzhu-live-adapter` workspace
- 开发版根 `package.json` 比发布版多出一整套 deploy / doctor / health / status 脚本
- 开发版 `modules/home-assistant/plugin/package.json` 已具备真实测试命令
- 开发版 `core/plugins/lingzhu-bridge/package.json` 已声明 OpenClaw 扩展入口

因此：

- 这些文件不做覆盖式合并
- 只能在保留现状的基础上吸收必要字段或说明

重点保护对象：

- `package.json`
- `deploy/repo-manifest.json`
- `deploy/repo.env.example`
- `core/plugins/lingzhu-bridge/package.json`
- `modules/home-assistant/plugin/package.json`
- `services/notification-router/package.json`

验收标准：

- 所有配置与脚本引用一致
- workspace 没有断裂
- 文档中描述的启动方式与脚本实际一致

### 阶段 5：共享代码区域合并

目标：

- 在不损坏当前开发版能力的前提下，吸收发布版中仍有价值的实现、说明或测试思路

重点处理模块：

- `core/plugins/lingzhu-bridge/**`
- `modules/home-assistant/**`
- `services/notification-router/**`

合并规则：

- 实现逻辑默认保留开发版
- 发布版只能补“缺失说明”“缺失约束”“缺失示例”“缺失兼容性语义”
- 不得为了追求文本一致而回退当前测试、脚本或目录结构

#### 阶段 5A：`core/plugins/lingzhu-bridge`

重点文件：

- `core/plugins/lingzhu-bridge/README.md`
- `core/plugins/lingzhu-bridge/package.json`
- `core/plugins/lingzhu-bridge/package-lock.json`
- `core/plugins/lingzhu-bridge/src/index.ts`

处理策略：

- `src/index.ts` 只在开发版存在，直接保留
- `package.json` 以开发版为准，尤其是 `openclaw.extensions`
- `README.md` 可吸收发布版的边界说明和责任定义
- `package-lock.json` 不单独手改，最终通过安装命令重建或校准

#### 阶段 5B：`modules/home-assistant`

重点差异分三层：

- 文档与契约层
  - `modules/home-assistant/README.md`
  - `modules/home-assistant/docs/**`
  - `modules/home-assistant/registry/README.md`
- 配置层
  - `modules/home-assistant/config/**`
  - `modules/home-assistant/registry/devices.example.json`
- 实现层
  - `modules/home-assistant/plugin/package.json`
  - `modules/home-assistant/plugin/src/registry/loadDevicesRegistry.ts`

开发版额外存在的内容必须保留：

- `modules/home-assistant/direct-adapters/**`
- `modules/home-assistant/docs/ecosystems/**`
- `modules/home-assistant/docs/home-ecosystem-support-matrix.md`
- `modules/home-assistant/plugin/src/registry/loadDevicesRegistry.test.ts`

处理策略：

- 文档与配置吸收发布版边界语义
- plugin 实现保留开发版
- direct-adapters 和 ecosystems 文档不允许被删除

#### 阶段 5C：`services/notification-router`

重点文件：

- `services/notification-router/README.md`
- `services/notification-router/config/README.md`
- `services/notification-router/docs/README.md`
- `services/notification-router/package.json`
- `services/notification-router/package-lock.json`
- `services/notification-router/src/README.md`
- `services/notification-router/src/__tests__/notification-router.test.ts`
- `services/notification-router/src/channels/openclawChannelDm.ts`
- `services/notification-router/src/server.ts`

处理策略：

- `package.json` 保留开发版脚本能力
- `src/server.ts`、`openclawChannelDm.ts` 以开发版实现为主
- 发布版可用于补齐边界说明、错误语义、说明文档
- `package-lock.json` 与最终依赖状态一致，不做手工拼接

建议执行顺序：

1. `core/plugins/lingzhu-bridge`
2. `modules/home-assistant`
3. `services/notification-router`

原因：

- 先处理较小的插件层，建立合并节奏
- 再处理中型的模块层
- 最后处理部署和服务耦合更强的 router

建议提交拆分：

- `refactor: merge release semantics into lingzhu bridge`
- `feat: align home assistant module with release documentation`
- `refactor: reconcile notification router with release baseline`

验收标准：

- 每个模块合并完成后都能单独测试
- 合并后脚本名、workspace 名、启动方式不变

### 阶段 6：验证与回归检查

目标：

- 确认升级版依然可运行、可测试、可部署

环境要求：

- Node 版本满足 `>=20 <26`

验证命令：

```bash
cd /Users/Zhuanz/Documents/Github/Mira-AI-that-sees-you
npm install
npm run test:release
npm --workspace @mira-release/lingzhu run test
npm --workspace @mira-release/home-assistant-module-plugin run test
npm --workspace @mira-release/notification-router run test
npm run doctor
npm run manifest:deploy
```

如果环境和依赖允许，补充执行：

```bash
npm run health:notification-router
npm run start:lingzhu-live-adapter
```

建议再补 3 类人工检查：

- 目录检查
  - `find core modules services deploy docs migration-bundles -maxdepth 2 -type d | sed -n '1,200p'`
- 引用检查
  - `rg -n "migration-bundles|lingzhu-live-adapter|direct-adapters|repo-deploy-runtime|notification-router" README.md readme docs modules services deploy`
- 依赖检查
  - `npm ls --workspaces --depth=0`

验收标准：

- 根级脚本可执行
- workspace 测试通过
- deploy manifest 可生成
- 没有因为导入发布版内容而破坏当前运行入口

### 阶段 7：收口与发布准备

目标：

- 对升级版进行最后整理，使其具备进入 PR 和发布说明阶段的条件

收口动作：

- 更新 `README.md` 中的升级版定位说明
- 更新发布说明或 changelog
- 明确 `migration-bundles/` 在仓库中的角色
- 检查文档是否仍把旧版视为主线
- 整理本次升级提交历史，确保每次提交都有清晰目的

建议最终提交：

- `docs: finalize upgraded repository positioning`
- `chore: finalize v3 merge upgrade release notes`

发布前还应补做：

- PR 描述中明确“哪些目录是导入，哪些文件是人工合并”
- 在 README 或 docs 中明确 `migration-bundles/` 的角色不是主 runtime
- 明确说明升级版的最小运行入口、部署入口和测试入口

## 7. 冲突处理决策表

| 类型 | 默认决策 | 说明 |
| --- | --- | --- |
| 开发版独有 runtime 文件 | 保留开发版 | 防止能力回退 |
| 发布版独有迁移资产 | 导入主仓库 | 这是发布版的核心价值 |
| 同路径文档文件 | 人工合并 | 统一术语与现状描述 |
| 同路径配置文件 | 人工合并，开发版优先 | 以可运行性为最高优先级 |
| 同路径代码文件 | 开发版优先，发布版补语义 | 避免回退实现 |
| workspace manifest | 禁止整文件覆盖 | 这些文件定义了当前仓库结构 |
| LICENSE 类文件 | 以主仓库真实许可证为准 | 不回退为 placeholder |

## 8. 推荐提交策略

不要做一个超大的合并提交。推荐最少拆成以下几组：

1. `docs: add merge baseline and plan`
2. `chore: import release migration bundles`
3. `docs: reconcile release and main documentation`
4. `refactor: align config and workspace contracts`
5. `feat: merge selected release semantics into shared modules`
6. `docs: finalize upgraded repository positioning`

这样做的好处：

- 更容易 code review
- 更容易定位回归来源
- 更容易回滚某一阶段
- 更容易在 PR 中解释“哪些是导入、哪些是人工合并”

## 9. 风险与防护措施

### 风险 1：把开发版回退成旧版

表现：

- runtime 脚本消失
- workspace 丢失
- 新服务和新模块被覆盖

防护：

- 所有同路径关键文件禁止整文件覆盖
- 关键 manifest 文件必须人工审阅

### 风险 2：文档与代码再次失配

表现：

- README 写的结构与仓库不一致
- examples 指向不存在的脚本或目录

防护：

- 文档合并完成后做目录和命令复核
- 所有命令必须在当前主仓库可找到对应脚本

### 风险 3：一次性改动过大，无法定位问题

表现：

- 合并后测试失败，不知道来自哪个阶段

防护：

- 分阶段提交
- 每个阶段结束都运行最小验证

### 风险 4：将迁移资产与活代码混为一体

表现：

- 后续维护时把 `migration-bundles/` 当成现行业务代码继续修改

防护：

- 在文档中明确 `migration-bundles/` 的定位是“发布/迁移资产层”
- 不把它作为 runtime 依赖主路径

## 10. 回滚策略

本方案的回滚以 Git 和分阶段提交为核心，不依赖破坏性命令。

回滚方式：

- 如果某一阶段提交后发现问题，优先使用 `git revert <commit>`
- 如果某个模块尚未提交，直接还原工作区即可
- 不使用 `git reset --hard` 破坏整体历史

推荐实践：

- 每一阶段至少一个独立 commit
- 每一阶段通过验证后再进入下一阶段

## 11. 完成标志

当以下条件全部满足时，可认定升级版已完成：

- 主仓库保留当前 GitHub 开发版的运行能力
- `migration-bundles/` 已成功引入
- 关键共享区域已完成人工合并
- 文档、目录和脚本口径一致
- 根级和 workspace 级验证通过
- 提交历史清楚反映每一阶段的操作目的

## 12. 最终建议

本次升级最重要的不是“尽快把文件搬完”，而是：

- 先保护当前 GitHub 主线能力
- 再有选择地吸收发布版价值
- 最后把结果整理成一个真正可维护的单一仓库

一句话总结：

**升级版 = 当前 GitHub 开发版主线 + 发布版迁移资产 + 共享区域人工合并，而不是两个目录的简单相加。**

## 13. 详细目录与文件处理矩阵

这一节给出更细的“落地操作表”，执行时优先参考本节。

### 13.1 根目录与仓库级文件

| 路径 | 现状判断 | 处理动作 | 理由 |
| --- | --- | --- | --- |
| `package.json` | 开发版明显更强 | 保留开发版，人工吸收必要信息 | 已包含更多 workspace、脚本和 engines |
| `README.md` | 双方都重要 | 人工合并 | 需要统一定位与结构说明 |
| `.gitignore` | 同路径不同内容 | 人工合并，倾向开发版 | 避免遗漏现行运行产物或临时目录 |
| `Dockerfile` | 开发版独有 | 保留 | 属于现行部署能力 |
| `compose.yaml` | 开发版独有 | 保留 | 属于现行部署能力 |
| `render.yaml` | 开发版独有 | 保留 | 属于现行部署能力 |
| `Procfile` | 开发版独有 | 保留 | 属于现行部署能力 |
| `LICENSE` | 开发版独有 | 保留 | 真实许可证优先 |
| `LICENSE.placeholder.md` | 发布版独有 | 默认不导入根目录 | 防止许可证语义回退 |

### 13.2 `core/` 区域

| 路径 | 现状判断 | 处理动作 | 理由 |
| --- | --- | --- | --- |
| `core/openclaw-config/**` | 契约差异明显 | 人工合并 | 影响 runtime contract |
| `core/workspace/AGENTS.md` | 同路径不同内容 | 人工合并 | 需要统一工作区约束 |
| `core/workspace/README.md` | 同路径不同内容 | 人工合并 | 需要反映当前结构 |
| `core/workspace/IDENTITY.md` | 开发版独有 | 保留 | 开发版新增认知层资产 |
| `core/workspace/SOUL.md` | 开发版独有 | 保留 | 开发版新增认知层资产 |
| `core/plugins/lingzhu-bridge/src/index.ts` | 开发版独有 | 保留 | OpenClaw 扩展入口 |
| `core/plugins/lingzhu-bridge/package.json` | 同路径不同内容 | 开发版优先 | 已声明扩展入口和更贴近现行使用 |

### 13.3 `modules/home-assistant/` 区域

| 路径 | 现状判断 | 处理动作 | 理由 |
| --- | --- | --- | --- |
| `modules/home-assistant/README.md` | 同路径不同内容 | 人工合并 | 统一模块定位 |
| `modules/home-assistant/config/**` | 同路径不同内容 | 人工合并 | 兼顾配置示例与现行实现 |
| `modules/home-assistant/docs/**` | 同路径不同内容 | 人工合并 | 保留开发版扩展文档 |
| `modules/home-assistant/direct-adapters/**` | 开发版独有 | 保留 | 当前开发版新增能力 |
| `modules/home-assistant/docs/ecosystems/**` | 开发版独有 | 保留 | 当前开发版新增能力 |
| `modules/home-assistant/plugin/package.json` | 同路径不同内容 | 开发版优先 | 已具备真实测试命令 |
| `modules/home-assistant/plugin/src/registry/loadDevicesRegistry.ts` | 同路径不同内容 | 开发版优先，人工吸语义 | 实现层高风险 |
| `modules/home-assistant/plugin/src/registry/loadDevicesRegistry.test.ts` | 开发版独有 | 保留 | 当前测试资产 |

### 13.4 `services/` 区域

| 路径 | 现状判断 | 处理动作 | 理由 |
| --- | --- | --- | --- |
| `services/lingzhu-live-adapter/**` | 开发版独有 | 保留 | 现行服务能力 |
| `services/notification-router/README.md` | 同路径不同内容 | 人工合并 | 统一服务定位 |
| `services/notification-router/package.json` | 同路径不同内容 | 开发版优先 | 开发版脚本更完整 |
| `services/notification-router/src/server.ts` | 同路径不同内容 | 开发版优先 | 运行入口高风险 |
| `services/notification-router/src/channels/openclawChannelDm.ts` | 同路径不同内容 | 开发版优先，人工吸语义 | 通道层代码不能回退 |
| `services/notification-router/package-lock.json` | 同路径不同内容 | 不手工拼接 | 以最终安装结果为准 |

### 13.5 `docs/`、`readme/`、`examples/`

| 路径 | 现状判断 | 处理动作 | 理由 |
| --- | --- | --- | --- |
| `docs/migration/**` | 双方均重要 | 人工合并 | 是升级叙事核心 |
| `docs/architecture/**` | 双方均重要 | 人工合并 | 统一架构边界 |
| `readme/**` | 双方均重要 | 人工合并 | 这是仓库导航层 |
| `examples/**` | 双方均重要 | 人工合并 | 需要与现行运行入口一致 |

### 13.6 `migration-bundles/`

| 路径 | 现状判断 | 处理动作 | 理由 |
| --- | --- | --- | --- |
| `migration-bundles/**` | 发布版独有核心资产 | 整目录导入 | 这是发布版最大价值 |
| `migration-bundles/**/release-source/**` | 发布版内嵌样本 | 保留，但不作为主代码路径 | 用于追踪与归档 |
| `migration-bundles/**/prototype-source/**` | 发布版内嵌样本 | 保留，但不接入 runtime | 用于参考与迁移 |

## 14. 冲突处理 SOP

当你真正开始逐文件合并时，建议严格按下面 8 步执行。

### 步骤 1：先做只读比较

```bash
diff -u /Users/Zhuanz/Documents/Github/Javis-Hackathon/Mira_Released_Version/<path> /Users/Zhuanz/Documents/Github/Mira-AI-that-sees-you/<path>
```

不要一上来就复制文件。

### 步骤 2：判断冲突类型

把每个文件标记为以下类型之一：

- 文档冲突
- 配置冲突
- manifest 冲突
- 实现冲突
- 测试冲突
- 依赖锁冲突

### 步骤 3：写一句合并结论

在你动手之前，先明确一句话：

- 保留开发版，仅吸收说明
- 保留开发版，实现不动，补文档
- 保留开发版，局部引入发布版段落
- 导入发布版独有文件
- 跳过，不合并

### 步骤 4：编辑文件

编辑时遵循：

- 只改当前这个决策范围内的文件
- 不顺手做无关重构
- 不在同一提交里同时改 docs 和 runtime，除非它们强耦合

### 步骤 5：局部检查

文档文件检查：

- 路径是否真实存在
- 命令是否真实可运行

代码文件检查：

- 引用是否还在
- 脚本名是否没变
- workspace 名是否没变

### 步骤 6：最小验证

根据文件类型选择一个最小验证动作：

- 文档：`rg` 检查路径和命令
- 配置：检查引用链
- package 文件：`npm install` 或 `npm ls`
- 测试文件：执行对应 workspace 测试
- 运行入口：执行对应脚本的 `doctor` / `status` / `test`

### 步骤 7：立即提交

只要这个小块已经稳定，就立即提交，不要攒太久。

### 步骤 8：记录决策

建议在 commit message 或 PR 描述中留下这类说明：

- 保留了开发版 runtime，吸收了发布版边界说明
- 导入了发布版迁移资产，但没有接入主运行路径
- 合并了 Home Assistant 文档，不回退 direct-adapters

## 15. 详细验证矩阵

| 检查对象 | 命令 | 通过信号 | 失败含义 |
| --- | --- | --- | --- |
| 根级安装 | `npm install` | 安装完成，无 workspace 解析错误 | manifest 或依赖结构出问题 |
| 根级发布测试 | `npm run test:release` | 脚本退出码 0 | 根级脚本或测试契约出问题 |
| Lingzhu bridge | `npm --workspace @mira-release/lingzhu run test` | 测试通过 | plugin 合并影响行为 |
| Home Assistant plugin | `npm --workspace @mira-release/home-assistant-module-plugin run test` | 测试通过 | module 合并影响行为 |
| Notification router | `npm --workspace @mira-release/notification-router run test` | 测试通过 | service 合并影响行为 |
| Deploy doctor | `npm run doctor` | 无关键错误 | deploy/runtime contract 不一致 |
| Deploy manifest | `npm run manifest:deploy` | manifest 成功输出 | repo 部署配置不一致 |
| 引用一致性 | `rg -n "lingzhu-live-adapter|direct-adapters|migration-bundles|notification-router"` | 引用路径合理 | 文档与代码失配 |
| Workspace 解析 | `npm ls --workspaces --depth=0` | 所有 workspace 正常识别 | 根 manifest 被破坏 |

## 16. 推荐的执行节奏

不要把整个升级看成一个动作，建议按“波次”执行。

### 波次 1：无争议资产并入

内容：

- `docs/merge/**`
- `migration-bundles/**`

目标：

- 先得到低风险可见进展

### 波次 2：文档统一

内容：

- `README.md`
- `readme/**`
- `docs/migration/**`
- `docs/architecture/**`
- `examples/**`

目标：

- 先统一认知层，给后续代码合并减少歧义

### 波次 3：契约层稳定

内容：

- `package.json`
- `core/openclaw-config/**`
- `core/workspace/**`
- `deploy/**`
- `modules/home-assistant/config/**`

目标：

- 锁住运行边界和配置边界

### 波次 4：共享实现层合并

内容：

- `core/plugins/lingzhu-bridge/**`
- `modules/home-assistant/**`
- `services/notification-router/**`

目标：

- 在已有契约和文档基础上做最难的部分

### 波次 5：全量验证与发布说明

内容：

- 全部测试
- 全部文档检查
- PR 和 release note 整理

目标：

- 把升级结果变成别人也能理解、也能接手的成果

## 17. 明确禁止事项

以下动作在本次升级中应视为禁区：

- 禁止把 `Mira_Released_Version` 整个目录覆盖到主仓库
- 禁止把发布版 `package.json` 直接替换开发版 `package.json`
- 禁止删除 `services/lingzhu-live-adapter/**`
- 禁止删除 `modules/home-assistant/direct-adapters/**`
- 禁止删除 `exports/**`
- 禁止把 `LICENSE.placeholder.md` 当成正式许可证替换 `LICENSE`
- 禁止为了“统一文本”而回退 runtime 脚本
- 禁止在一个提交里同时做大规模 docs、config、runtime 三类混改
- 禁止在没有验证的前提下连续堆叠多个高风险提交

## 18. PR 撰写与评审建议

### 18.1 PR 标题建议

建议使用类似标题：

- `feat: create v3 upgraded repo by merging release assets into active mainline`
- `chore: import release migration bundles and reconcile shared contracts`

### 18.2 PR 描述建议结构

建议 PR 描述包含这 6 块：

1. 背景
2. 本次目标
3. 导入了哪些发布版独有内容
4. 哪些共享区域做了人工合并
5. 哪些开发版能力被明确保留
6. 跑了哪些验证

### 18.3 评审重点

Reviewer 不应该平均看所有文件，而应优先看：

- 根 `package.json`
- `core/plugins/lingzhu-bridge/package.json`
- `modules/home-assistant/plugin/package.json`
- `services/notification-router/package.json`
- `README.md`
- `docs/migration/**`
- `migration-bundles/**`

## 19. 最终执行清单

在真正开始合并时，可以把下面这份清单当作最直接的执行板。

### 启动前

- [ ] 主仓库 `main` 已更新
- [ ] 新分支已创建
- [ ] 工作区干净
- [ ] `docs/diff_report.md` 已归档到主仓库
- [ ] 本计划文档已归档到主仓库

### 导入阶段

- [ ] `migration-bundles/**` 已 dry-run 检查
- [ ] `migration-bundles/**` 已正式导入
- [ ] 导入后未破坏现有目录结构

### 文档阶段

- [ ] `README.md` 已人工合并
- [ ] `readme/**` 已人工合并
- [ ] `docs/migration/**` 已人工合并
- [ ] `examples/**` 已人工合并

### 契约阶段

- [ ] 根 `package.json` 已确认保留开发版结构
- [ ] `core/openclaw-config/**` 已审阅
- [ ] `core/workspace/**` 已审阅
- [ ] `deploy/**` 已审阅
- [ ] `modules/home-assistant/config/**` 已审阅

### 共享实现阶段

- [ ] `core/plugins/lingzhu-bridge/**` 已完成合并
- [ ] `modules/home-assistant/**` 已完成合并
- [ ] `services/notification-router/**` 已完成合并
- [ ] 开发版独有目录未被误删

### 验证阶段

- [ ] `npm install` 通过
- [ ] `npm run test:release` 通过
- [ ] 3 个重点 workspace 测试通过
- [ ] `npm run doctor` 通过
- [ ] `npm run manifest:deploy` 通过
- [ ] 关键文档引用检查通过

### 收尾阶段

- [ ] PR 描述已写清“导入”和“人工合并”的边界
- [ ] `migration-bundles/` 角色已在文档中澄清
- [ ] 最终提交历史可解释
- [ ] 升级版定位已写入 README 或发布说明
