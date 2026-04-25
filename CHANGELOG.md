# Changelog

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
