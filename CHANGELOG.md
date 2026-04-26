# Changelog

## 0.1.21 - 2026-04-27

### Added

- Consumer project initialization now creates `agent-os-runtime.md`, `skill-learning-log.md`, `docs/agent-os-upgrades/`, and `evidence/references/agent-os/`.
- Added `agent-os-upgrade-packet.md` template so reusable lessons can be staged before being brought back to the skill repository.
- Added `consumer-main-agent-misses-growth-path` eval to ensure a consumer project's Main Agent notices the growth path.

### Changed

- Project Memory now points Main Agent to runtime awareness, learning log, and upgrade packet locations.
- Installation and evolution protocols now describe startup awareness files for consumer projects.

### Fixed

- Fixed the gap where a new project's Main Agent could install the skill but fail to notice where reusable workflow lessons should be recorded.

### Deprecated

- N/A

## 0.1.20 - 2026-04-27

### Added

- 新增 Growth Loop，明确 skill 通过真实项目运行、失败记录、过滤、补规则、补 eval/test、版本化来成长。
- 新增 Project Learning Log Entry 与 Growth Review，用于把项目中的 agent 失败沉淀为可筛选的成长材料。
- 新增 `skill-growth-without-eval` eval，防止直接把一次性项目经验塞进核心 skill。

### Changed

- Evolution Filter 和 Evolution Decision 增加 `Required Eval or Test`，要求被推广的规则必须有评测或测试承接。

### Fixed

- 修复成长机制过于静态的问题，避免 skill 只靠预想扩张而缺少实战反馈闭环。

### Deprecated

- N/A

## 0.1.19 - 2026-04-27

### Added

- 新增 Specialist Agent Lifecycle 与 `Agent Reuse Decision`，要求主 agent 创建责任 agent 前先复用已有同职责 agent。
- 新增 `duplicate-specialist-agent-spawn` eval，防止同职责测试/审计 agent 被重复拉起导致审计链分裂。

### Changed

- Default Workflow 增加 agent reuse 决策步骤，重复创建同角色 agent 必须关闭重复实例并刷新上下文。

### Fixed

- 修复流程漏洞：已有同功能 agent 时，主 agent 仍重复创建新 agent，造成上下文分裂和证据链混乱。

### Deprecated

- N/A

## 0.1.18 - 2026-04-26

### Added

- 安装包纳入 `evals/`，确保 installed Skill 的 `scripts/run_evals.py` 有场景语料可运行。

### Changed

- 安装测试新增 eval corpus 覆盖，防止 eval runner 与安装内容脱节。

### Fixed

- 修复 Testing Agent 发现的安装后 eval runner 缺少 `evals/` 导致不可用的问题。

### Deprecated

- N/A

## 0.1.17 - 2026-04-26

### Added

- 新增 `main-agent-decision-review.md`，要求主 agent 将责任 agent 的复杂图、计划、报告翻译成用户决策语言。
- 新增 `specialist-output-needs-main-agent-review` eval，防止主 agent 把复杂服务器图原样甩给用户。

### Changed

- 当用户缺少专业背景时，Main Agent 必须提供 `Main Agent Specialist Review` 或 `User Decision Brief`。

### Fixed

- 修复复杂 specialist 输出缺少主 agent 翻译、质疑和建议层的问题。

### Deprecated

- N/A

## 0.1.16 - 2026-04-26

### Added

- 新增 `reconnect-session-governance.md`，将断线重连、会话、身份、房间保留、快照/事件回放、乱序/重复消息、结算安全做成独立服务器门禁。
- 新增 `reconnect-without-session-plan` eval，防止 Server Development Agent 直接实现 reconnect 而不提供会话和恢复计划。
- Server Agent 测试新增 Reconnect and Session Plan 覆盖。
- 新增 `strong-online-server-governance.md`，要求 Server Agent 主动覆盖身份、房间生命周期、状态同步、并发、数据一致性、反作弊、可观测、运维、扩容和故障恢复，不再等待用户逐项提醒。
- 新增 `strong-online-server-without-readiness-plan` eval，防止强联网服务器只讨论 reconnect 就开始实现。

### Changed

- Server Development Agent 在登录、会话、进房、匹配、重连、回放、结算、玩家返回流程前必须提供 `Reconnect and Session Plan`。
- 强联网 eval 增加 reconnect-session-governance 协议要求。
- 强联网 Server Development Agent 在进入具体实现前必须提供 `Strong Online Server Readiness Plan`。

### Fixed

- 补强强联网项目最常见的断线重连与会话恢复风险边界。
- 修复服务器规范依赖用户逐项指出风险的流程缺陷。

### Deprecated

- N/A

## 0.1.15 - 2026-04-26

### Added

- Server Development Agent 新增 Go 服务器默认语言、Go Concurrency Plan、Data Consistency Plan。
- Client Development Agent 新增 TypeScript 客户端默认语言，并要求 TS request/response/event types 与 Go server contract 对齐。
- 强联网 eval 增加 Go 并发计划与数据一致性计划要求。

### Changed

- Server Architecture Plan 扩展并发模型、数据模型、一致性模型、TypeScript Client Contract。
- Authoritative Gameplay Contract 扩展 TypeScript request/response/event type 字段。

### Fixed

- 补强 Server Agent 对并发、数据一致性、幂等、房间状态所有权和客户端契约的职责边界。

### Deprecated

- N/A

## 0.1.14 - 2026-04-26

### Added

- 新增 Client Development Agent 与 Server Development Agent，用于麻将、MOBA、战术竞技、实时动作等强联网游戏。
- 新增 `role-client-development.md`、`role-server-development.md` 与对应角色 prompt。
- 新增 `strong-online-game-requires-server-agent` eval，防止强联网项目被单一 Development Agent 吞掉。
- 新增 Development Role Split Decision，要求多人/强服务器项目先判断是否拆分客户端与服务器开发职责。

### Changed

- `SKILL.md`、protocol routing、context packets、README、OpenAI metadata 更新为支持 client/server role split。
- Development Agent 保留为轻量项目或通用工程入口；强联网项目转为 Client Development Agent + Server Development Agent。

### Fixed

- 修复强服务器游戏缺少独立服务器开发责任人的流程风险。

### Deprecated

- N/A

## 0.1.13 - 2026-04-26

### Added

- 新增 `scripts/run_evals.py`，可单独执行 eval scenario checks，避免 eval 只隐藏在仓库 validator 内部。
- `validate_skill_repo.py` 复用 eval runner，保证本地验证和独立 eval 命令一致。
- 新增 eval runner 单元测试，覆盖 main-agent self-check 与 release confidence 场景。

### Changed

- `skill-manifest.json` tools 加入 `scripts/run_evals.py`。

### Fixed

- 修复 Testing Agent 指出的 eval 只有结构检查、缺少独立执行入口的问题。

### Deprecated

- N/A

## 0.1.12 - 2026-04-26

### Added

- 新增 multi-layer gate 与 `design_packet_validator.py` 的 parity tests，覆盖缺少 `Multi-Layer Pre-Code Gate`、`Implementation Allowed`、测试证据的失败场景。
- 新增 `release-confidence-without-evidence` eval，防止 Testing Agent 用无证据的 `Release Confidence: Ready` 推动发布。
- 新增 manifest 协议覆盖测试，要求 `skill-manifest.json` 的 protocols 完整覆盖 `references/*.md`。

### Changed

- `design_packet_validator.py --require-multi-layer` 改为校验 `multi-layer-feature-gate.md` 中真实的 `Multi-Layer Pre-Code Gate` 字段。
- `skill-manifest.json` 的 protocols 扩展为完整 reference 协议索引。

### Fixed

- 修复 Testing Agent 回归发现的 multi-layer protocol 与 validator 字段不一致问题。
- 修复 manifest 漏报核心协议导致 agent 判断能力不完整的问题。

### Deprecated

- N/A

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
