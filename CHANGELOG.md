# Changelog

## 0.1.11 - 2026-04-26

### Added

- Completion trust protocol 新增 Main Agent Claims 规则，明确主 agent 的自检完成、workflow 完成、Git push/tag 完成、release readiness 也属于可审计完成声明。
- 新增 `main-agent-self-check-claim` eval，防止主 agent 用自检完成声明绕过审计报告。

### Changed

- Completion Audit Trigger 扩展到主 agent 自检、GitHub 推送/tag、发布准备和生产准备声明。

### Fixed

- 修复主 agent 可能用“项目自检已完成”这类最终总结绕过 Audit Agent 的制度漏洞。

### Deprecated

- N/A

## 0.1.10 - 2026-04-26

### Added

- Completion trust protocol 新增 `Constraint Ownership`，明确 response contract、completion trust、audit role、角色协议和工具协议的职责归属。
- 测试新增去重保护，防止 evidence class 规则被重新复制到 response contract 或 audit 角色文档中。

### Changed

- 收敛 `response-contract.md`、`role-audit.md`、`role-audit-prompt.md` 中重复的完成信任说明，改为引用 `completion-trust-boundary.md`。

### Fixed

- 修复审计 agent 加入后部分硬性约束重复展开、文档职责边界不够集中的问题。

### Deprecated

- N/A

## 0.1.9 - 2026-04-26

### Added

- 新增 Audit Agent，专门审计完成声明、证据链、跳过门禁、未验证风险和自检深度。
- 新增 `completion-trust-boundary.md`，规定 agent completion is not evidence，并要求区分 Verified / Inferred / Unverified。
- 新增 audit 角色 prompt 与完成声明缺少审计的 eval 场景。

### Changed

- 根级 `SKILL.md` 将审计门禁加入默认工作流和核心角色边界。
- response contract 要求高风险完成声明进入 completion trust boundary。

### Fixed

- 修复工作流过度依赖 agent 自称完成、缺少独立完成信任审计的问题。

### Deprecated

- N/A

## 0.1.8 - 2026-04-26

### Added

- 根级 `SKILL.md` 新增 Specialist Context Packet 最小格式，明确隔离模式、允许上下文和 withheld context。

### Changed

- 根级 `SKILL.md` 的 Task Brief 和 Agent Turn Result 与模板同步，补齐协议、门禁、影响层、权限、信任边界、工具证据字段。
- 开发工具门禁 eval 扩展为多层功能场景，覆盖开发、测试、权限、信任边界与多层预编码门禁。

### Fixed

- 修复根入口格式落后于模板和 response contract，导致新安装 Skill 的 agent 可能漏掉工具门禁的问题。

### Deprecated

- N/A

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
