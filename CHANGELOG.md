# Changelog

## 0.1.7 - 2026-04-26

### Added

- README 新增中文短安装口令和短使用口令，降低用户记忆成本。

### Changed

- 版本同步到当前 GitHub 推送状态，避免 `v0.1.6` 旧标签代表新内容。

### Fixed

- N/A

### Deprecated

- N/A

## 0.1.6 - 2026-04-26

### Added

- 安装包纳入 `.github/` GitHub 门禁模板，避免 installed Skill 缺少外部门禁资源。
- 通用 `Agent Turn Result` 与角色模板加入 `Tool Gate` / `Tool Evidence` 字段。

### Changed

- 强化开发、测试、美术角色模板对上下文隔离、层级校验、依赖素材审计、素材来源记录的触发。

### Fixed

- 修复 GitHub governance 文件只存在于母仓库、安装 Skill 后不可见的问题。

### Deprecated

- N/A

## 0.1.5 - 2026-04-26

### Added

- 新增 `skill-manifest.json`，记录 Skill 版本、兼容性、协议和工具清单。
- 新增兼容性/registry、上下文隔离、层级边界、依赖与素材审计协议。
- 新增 `layer_map_validator.py` 与 `dependency_asset_audit.py` 工具。

### Changed

- 将外部 GitHub skill/tool 经验收敛为可执行、可验证的 Agent Collaboration OS 能力。

### Fixed

- N/A

### Deprecated

- N/A

## 0.1.4 - 2026-04-26

### Added

- 新增 GitHub 外部门禁层：Actions、CodeQL、Dependabot、CODEOWNERS、PR/Issue 模板、release workflow、ruleset 模板。
- 新增 `github-governance.md` 协议和路由入口。
- 新增 GitHub 门禁 eval 与仓库自检要求。

### Changed

- 生产操作协议联动 GitHub governance，避免 agent 声称未启用的 GitHub 保护已经生效。

### Fixed

- N/A

### Deprecated

- N/A

## 0.1.3 - 2026-04-26

### Added

- 新增 Skill 路径清洁边界：运行态 Markdown 与 evidence 必须写入消费者项目。
- 新增自检规则，禁止 Skill 仓库根目录出现运行态 `docs/` 或 `evidence/`。
- 新增 Skill 路径污染 eval 场景。

### Changed

- 更新项目资产治理与安装协议，明确 vendored Skill 路径不能承载项目运行产物。

### Fixed

- N/A

### Deprecated

- N/A

## 0.1.2 - 2026-04-26

### Added

- 新增 Development Agent Tool Gate 机制，要求工具结果进入 `Tool Gate` 与 `Tool Evidence`。
- 新增开发工具门禁 eval，覆盖跳过工具直接完成的场景。

### Changed

- 强化开发 agent prompt，要求在设计、影响分析、完成声明前使用对应工具门禁。

### Fixed

- N/A

### Deprecated

- N/A

## 0.1.1 - 2026-04-26

### Added

- 新增开发日常工具：设计说明校验、影响范围分析、diff 风险审查。
- 新增 `development-daily-tools.md` 协议引用与路由入口。
- 新增开发 agent 支撑工具的单元测试。

### Changed

- README 改为面向用户的中文说明，并明确工具由 agent 调用。

### Fixed

- N/A

### Deprecated

- N/A

## 0.1.0 - 2026-04-26

### Added

- 初始 Agent Collaboration OS Skill 内核。
- 渐进式披露协议文档。
- Debug 二分诊断工具与测试。
- 消费项目初始化脚本。
- 角色提示模板、游戏 profile、可复用模块说明。

### Changed

- 仓库标准化为 Codex Skill 与可 vendoring 工具源的双形态结构。

### Fixed

- N/A

### Deprecated

- N/A
