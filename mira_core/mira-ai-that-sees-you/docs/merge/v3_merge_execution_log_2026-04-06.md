# V3 Merge Execution Log

日期：2026-04-06  
执行仓库：`/Users/Zhuanz/Documents/Github/Mira-AI-that-sees-you`  
执行分支：`feat/upgrade-from-release-v3`

## 1. 本次已实际完成的动作

本次不是只写计划，而是已经完成了第一波低风险落地：

- 已从 `main` 切出升级分支 `feat/upgrade-from-release-v3`
- 已在主仓库创建 `docs/merge/`
- 已归档对比报告：
  - `docs/merge/diff_report_2026-04-06.md`
- 已归档升级执行计划：
  - `docs/merge/v3_merge_upgrade_plan_2026-04-06.md`
- 已把发布版的 `migration-bundles/` 整体导入主仓库

## 2. 已导入资产概况

`migration-bundles/` 导入结果：

- 文件数：`224`
- 目录数：`131`

导入方式：

- 先执行 `rsync --dry-run`
- 确认只会新增 `migration-bundles/`
- 再执行正式 `rsync`

这样做的目的：

- 先吸收发布版里最核心、最独有、且风险最低的资产
- 避免一开始就碰共享实现文件
- 给后续人工合并保留干净主线

## 3. 当前工作区状态

当前分支：

```text
feat/upgrade-from-release-v3
```

当前未提交变更：

```text
docs/merge/
migration-bundles/
```

说明：

- 这些变更已经落盘到主仓库
- 目前还**没有提交 commit**
- 保持未提交状态的目的是方便继续整理与检查

## 4. 这一步为什么合理

当前主仓库是开发版主线，真正不能乱动的是：

- 根 `package.json`
- runtime / deploy 脚本
- `services/lingzhu-live-adapter/**`
- `modules/home-assistant/direct-adapters/**`
- `exports/**`

相比之下，`migration-bundles/**` 是发布版的核心独有资产，而且并不直接接管现有 runtime，因此最适合作为第一波落地内容。

这一步完成后，升级工作已经具备两个基础条件：

- 有正式归档的比较与执行文档
- 有已经进入主仓库的发布版迁移资产

## 5. 当前还没有动的高风险区域

以下内容仍然**没有开始人工合并**：

- `README.md`
- `readme/**`
- `docs/migration/**`
- `core/openclaw-config/**`
- `core/workspace/**`
- `core/plugins/lingzhu-bridge/**`
- `modules/home-assistant/**`
- `services/notification-router/**`

这是有意为之。

原因：

- 它们是共享路径区域
- 它们包含同名但内容不同的文件
- 它们一旦动错，最容易把开发版回退成旧版

## 6. 下一步建议执行顺序

建议继续按下面的顺序推进，而不是跳着改：

1. 提交本次低风险导入结果
2. 合并顶层文档与迁移文档
3. 合并配置与契约层
4. 最后进入共享实现层

如果立刻继续，我建议先做第二波中的文档层：

- `README.md`
- `readme/**`
- `docs/migration/**`
- `examples/**`

原因：

- 它们能统一认知口径
- 风险低于 runtime 代码
- 可以为后续 `modules/` 与 `services/` 的合并减少歧义

## 7. 下一步推荐命令

如果要把本次已经落地的内容先保存成一个清晰阶段，可以执行：

```bash
cd /Users/Zhuanz/Documents/Github/Mira-AI-that-sees-you
git add docs/merge migration-bundles
git commit -m "chore: import release migration bundles and merge baseline docs"
```

如果要继续进入文档层人工合并，可以从下面几组比较开始：

```bash
diff -u /Users/Zhuanz/Documents/Github/Javis-Hackathon/Mira_Released_Version/README.md /Users/Zhuanz/Documents/Github/Mira-AI-that-sees-you/README.md
diff -u /Users/Zhuanz/Documents/Github/Javis-Hackathon/Mira_Released_Version/readme/README.md /Users/Zhuanz/Documents/Github/Mira-AI-that-sees-you/readme/README.md
diff -u /Users/Zhuanz/Documents/Github/Javis-Hackathon/Mira_Released_Version/docs/migration/repository-split-checklist.md /Users/Zhuanz/Documents/Github/Mira-AI-that-sees-you/docs/migration/repository-split-checklist.md
```

## 8. 当前阶段结论

V3 升级计划现在已经从“文档设计阶段”进入“实际执行阶段”，并且已经完成：

- 升级分支创建
- 基线文档归档
- 发布版迁移资产导入

下一阶段的重点，不再是搬运文件，而是开始对共享路径内容做有判断的人工合并。

## 9. 本轮补充文档

为了让后续执行不再停留在“总计划”层，这一轮又补充了 4 份执行级文档：

- `docs/merge/v3_file_decision_matrix.md`
- `docs/merge/v3_merge_backlog.md`
- `docs/merge/v3_validation_checklist.md`
- `docs/merge/v3_dependency_policy.md`

这 4 份文档分别解决的问题是：

- 决策矩阵：每个关键文件到底怎么处理
- backlog：下一步具体按什么顺序做
- 验证清单：每一波改动后怎么验
- 依赖策略：manifest 和 lockfile 哪些绝不能回退

## 10. 当前执行成熟度判断

到这一刻为止，V3 merge 相关资料已经覆盖了 5 层：

1. 差异事实层
2. 总体计划层
3. 执行记录层
4. 文件决策层
5. 验证与依赖策略层

这意味着后续继续推进时，已经不再需要“临时想规则”，而可以直接：

- 看 backlog 取任务
- 看 decision matrix 决定文件处理方式
- 看 dependency policy 保护 manifest
- 看 validation checklist 做验证

## 11. 建议的下一动作

从执行角度看，最值得继续推进的是：

1. 提交第一波低风险导入
2. 开始 `README.md`、`readme/**`、`docs/migration/**` 的人工合并
3. 每完成一波就更新本执行日志

## 12. 2026-04-07 文档合并波次进展

本轮继续推进了文档层的真实人工合并，已经完成：

- 顶层 [README.md](../../README.md) 的升级版口径改写
- [../../readme/README.md](../../readme/README.md) 的门户说明补充
- 以下 migration 文档的清理与统一：
  - [../../docs/migration/README.md](../../docs/migration/README.md)
  - [../../docs/migration/release-baseline.md](../../docs/migration/release-baseline.md)
  - [../../docs/migration/open-source-readiness-checklist.md](../../docs/migration/open-source-readiness-checklist.md)
  - [../../docs/migration/package-and-license-decisions.md](../../docs/migration/package-and-license-decisions.md)
  - [../../docs/migration/repository-split-readiness.md](../../docs/migration/repository-split-readiness.md)
  - [../../docs/migration/repository-split-checklist.md](../../docs/migration/repository-split-checklist.md)

本轮主要解决的具体问题：

- 去掉旧机器上的绝对路径引用
- 去掉把 `Mira_Released_Version/` 当作当前唯一主线的旧表述
- 明确当前仓库是“主仓库 mainline + release-safe docs + migration bundles”的升级版结构
- 重新定义 `migration-bundles/` 的角色：它是 copied context，不是 active runtime tree
- 把 repository split 相关文档改成“从当前主仓库导出 release-ready subset”的口径

## 13. 2026-04-07 文档验证结果

本轮做了两类验证：

1. 链接验证

- 检查文件：
  - `README.md`
  - `readme/README.md`
  - `docs/migration/README.md`
  - `docs/migration/release-baseline.md`
  - `docs/migration/open-source-readiness-checklist.md`
  - `docs/migration/package-and-license-decisions.md`
  - `docs/migration/repository-split-readiness.md`
  - `docs/migration/repository-split-checklist.md`
- 结果：
  - checked links: `127`
  - missing links: `0`

2. 根命令验证

- 检查 `README.md` 里引用的关键根命令
- 结果：
  - expected scripts checked: `15`
  - missing scripts: `0`

结论：

- 本轮文档改动在链接层面是自洽的
- 顶层 README 引用的关键命令仍然与当前 `package.json` 一致

## 14. 当前剩余的文档层缺口

本轮还没有处理的文档层内容主要是：

- [../../docs/README.md](../../docs/README.md)
- `readme/00-overview/**`
- `readme/40-deploy/**`
- `examples/**`

从收益上看，下一步最值得做的是先补：

1. `docs/README.md`
2. `readme/00-overview/**`
3. `examples/**`

## 15. 2026-04-07 门户与 examples 波次进展

本轮继续完成了 portal-level 文档的一整波真实合并，已修改：

- [../../docs/README.md](../../docs/README.md)
- [../../readme/00-overview/README.md](../../readme/00-overview/README.md)
- [../../readme/00-overview/getting-started.md](../../readme/00-overview/getting-started.md)
- [../../readme/00-overview/quick-start.md](../../readme/00-overview/quick-start.md)
- [../../examples/README.md](../../examples/README.md)
- [../../examples/minimal-core/README.md](../../examples/minimal-core/README.md)
- [../../examples/home-stack/README.md](../../examples/home-stack/README.md)
- [../../examples/service-notification-router/README.md](../../examples/service-notification-router/README.md)
- [../../examples/home-stack-with-notification-router/README.md](../../examples/home-stack-with-notification-router/README.md)

这一波主要完成了 4 件事：

- 把 `docs/README.md` 从旧 release-tree 绝对路径改成当前主仓库相对导航
- 给 `readme/00-overview/**` 补上边界说明，并接入 `migration-bundles/` 的引导
- 把 `examples/**` 全部改成当前主仓库可直接点击的相对链接
- 在 examples 层补回 `Does Not Own`，让 example、runtime、deploy 三者边界更清楚

## 16. 2026-04-07 本轮附加验证结果

这一次在上一轮基础上又补了两类验证：

1. 旧路径残留扫描

- 检查范围：
  - `docs/README.md`
  - `readme/00-overview/**`
  - `examples/**`
- 检查目标：
  - `/Users/thomasjwang/Documents/GitHub`
  - `Mira_Released_Version/`
- 结果：
  - residual matches: `0`

2. 新改文档链接校验

- 检查文件数：`9`
- checked links: `98`
- missing links: `0`

结论：

- 本轮新增的 portal 和 example 文档已经切换到当前主仓库语境
- 没有残留旧 release-tree 绝对路径
- 新增相对链接全部可解析

## 17. 当前剩余的文档层缺口

文档层现在已经完成：

- 顶层 repo docs
- migration docs
- docs portal root
- overview onboarding docs
- examples docs

当前剩余的主要文档缺口是：

- `readme/10-core/README.md`
- `readme/20-modules/README.md`
- `readme/40-deploy/**`
- `deploy/**`
- [../../docs/architecture/README.md](../../docs/architecture/README.md)
- [../../hardware/README.md](../../hardware/README.md)
- [../../modules/README.md](../../modules/README.md)

如果继续往下推进，最合理的顺序是：

1. `readme/10-core/README.md` 和 `readme/20-modules/README.md`
2. `readme/40-deploy/**` 与 `deploy/**`
3. `hardware/README.md` 与 `modules/README.md`

## 18. 2026-04-07 core/modules/hardware 入口波次进展

这一轮继续完成了 portal 导航层剩余入口页的统一，已修改：

- [../../readme/10-core/README.md](../../readme/10-core/README.md)
- [../../readme/20-modules/README.md](../../readme/20-modules/README.md)
- [../../readme/30-hardware/README.md](../../readme/30-hardware/README.md)
- [../../modules/README.md](../../modules/README.md)
- [../../hardware/README.md](../../hardware/README.md)

这一波主要完成了 4 件事：

- 给 core、modules、hardware 三个 portal 入口全部补齐 `Does Not Own` 边界
- 修掉 [../../modules/README.md](../../modules/README.md) 中残留的旧 release-tree 绝对路径
- 明确 `modules/home-assistant/direct-adapters/` 目前仍属于 module-owned capability，而不是独立 public hardware root
- 把 portal-level 入口和真实目录入口重新连通，避免 overview、modules、hardware 三层描述脱节

## 19. 2026-04-07 本轮入口页验证结果

本轮对 5 个入口页又做了两类验证：

1. 旧路径残留扫描

- 检查文件数：`5`
- 检查目标：
  - `/Users/thomasjwang/Documents/GitHub`
  - `Mira_Released_Version/`
- 结果：
  - residual matches: `0`

2. 链接校验

- 检查文件数：`5`
- checked links: `29`
- missing links: `0`

结论：

- core/modules/hardware 入口页已经切换到当前主仓库语境
- 本轮新增导航链接全部可解析
- 当前 portal 层已经基本完成，只剩 deploy 和 architecture 两块主要缺口

## 20. 当前剩余的文档层缺口

文档层当前还没有处理的重点内容是：

- `readme/40-deploy/**`
- `deploy/**`
- [../../docs/architecture/README.md](../../docs/architecture/README.md)
- [../../readme/50-development/contributing-and-migration.md](../../readme/50-development/contributing-and-migration.md)

如果继续往下推进，最合理的顺序是：

1. `readme/40-deploy/**` 与 `deploy/**`
2. [../../docs/architecture/README.md](../../docs/architecture/README.md)
3. [../../readme/50-development/contributing-and-migration.md](../../readme/50-development/contributing-and-migration.md)

## 21. 2026-04-07 deploy 文档波次进展

这一轮继续完成了 deploy 文档层的真实合并，已修改：

- [../../readme/40-deploy/README.md](../../readme/40-deploy/README.md)
- [../../deploy/README.md](../../deploy/README.md)
- [../../deploy/deploy-paths-overview.md](../../deploy/deploy-paths-overview.md)
- [../../deploy/core/README.md](../../deploy/core/README.md)
- [../../deploy/minimal/README.md](../../deploy/minimal/README.md)
- [../../deploy/module-home-assistant/README.md](../../deploy/module-home-assistant/README.md)
- [../../deploy/service-notification-router/README.md](../../deploy/service-notification-router/README.md)

这一波主要完成了 4 件事：

- 给 deploy portal 和 profile docs 补齐 `Does Not Own` 边界
- 把 `deploy/minimal/README.md` 从纯占位页补成一个清晰的 reserved slot 说明
- 保留当前主仓库里已经存在的运行态信息，同时补回发布版中更清晰的导航和非目标说明
- 明确 deploy 文档描述的是当前升级后的主仓库，而不是一个独立的 release-only tree

## 22. 2026-04-07 deploy 文档验证结果

本轮对 7 个 deploy 相关文档做了两类验证：

1. 旧路径残留扫描

- 检查文件数：`7`
- 检查目标：
  - `/Users/thomasjwang/Documents/GitHub`
  - `Mira_Released_Version/`
- 结果：
  - residual matches: `0`

2. 链接校验

- 检查文件数：`7`
- checked links: `83`
- missing links: `0`

结论：

- deploy portal 和 profile docs 已经全部切到当前主仓库语境
- 本轮新增或保留的 deploy 导航链接全部可解析
- 文档层现在只剩 architecture 入口和少量开发迁移说明缺口

## 23. 当前剩余的文档层缺口

文档层当前还没有处理的重点内容是：

- [../../docs/architecture/README.md](../../docs/architecture/README.md)
- [../../readme/50-development/contributing-and-migration.md](../../readme/50-development/contributing-and-migration.md)

文档层之后紧接着最值得进入的是：

- `deploy/service-notification-router/env.example`
- `core/openclaw-config/**`
- `core/workspace/**`
- `modules/home-assistant/config/**`
- `modules/home-assistant/registry/devices.example.json`

如果继续往下推进，最合理的顺序是：

1. [../../docs/architecture/README.md](../../docs/architecture/README.md)
2. `deploy/service-notification-router/env.example`
3. `core/openclaw-config/**`
