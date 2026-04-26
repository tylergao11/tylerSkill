# Agent Collaboration OS

这是一个可安装、可迁移、可版本化的 Agent 协作操作系统 Skill。

它的目标不是让用户手动调用各种脚本，而是让用户安装 Skill 之后，把项目协作、开发前设计、调试诊断、回归检查、发布风险判断交给 agent 按规范执行。

核心原则：agent 的“我完成了”不是证据。重要工作需要由审计流程检查证据链，区分已验证、推断成立、尚未验证，避免自然语言完成声明直接推动项目状态。

所有文本文件必须使用 UTF-8。

## 使用方式

普通用户只需要安装这个 Skill。

最短安装口令：

```text
装这个skill：https://github.com/tylergao11/tylerSkill.git
```

也可以说：

```text
安装这个skill：https://github.com/tylergao11/tylerSkill.git
```

安装后，在项目中告诉主 agent 使用 Agent Collaboration OS，它会按需读取 `SKILL.md` 和 `references/` 中的协议，并在需要时调用 `scripts/` 里的工具。

最短使用口令：

```text
使用协作OS
```

第一次使用时也可以说得更明确：

```text
使用 Agent Collaboration OS 管理这个项目
```

这些工具主要面向 agent：

- `scripts/design_packet_validator.py`：检查开发 agent 的工程设计说明是否完整。
- `scripts/impact_analyzer.py`：根据改动文件推断影响范围和回归检查。
- `scripts/diff_risk_reviewer.py`：在开发 agent 声称完成前检查 diff 风险。
- `scripts/debug_bisection.py`：在疑难问题中用二分诊断代替逐个猜测修改。

审计 agent 会检查完成声明、证据链、跳过的门禁和未验证风险。用户不需要单独记住它，只要要求使用协作 OS，主 agent 应在关键完成点自动触发审计。

用户不需要记住这些命令。它们是 Skill 的内部能力，主 agent 和责任 agent 会在合适的协议中调用。

强联网游戏建议拆分开发职责。麻将、MOBA、战术竞技、实时动作、排行榜、匹配、房间、重连、防作弊、强经济系统等项目，应使用：

- Client Development Agent：默认 TypeScript，负责客户端表现、输入、UI、渲染、资源、预测/插值。
- Server Development Agent：默认 Go，负责房间、匹配、权威规则、状态同步、持久化、并发安全、重连、安全边界、防作弊假设。

轻量小游戏仍可由普通 Development Agent 同时处理客户端和云开发/简单服务。

当责任 agent 输出复杂图、服务器计划、测试报告或审计报告时，主 agent 应负责翻译成用户能决策的语言：这是什么意思、你要拍板什么、风险在哪里、下一步谁验证。用户不需要直接读懂 Go 并发、状态同步、幂等、锁、通道或运维细节。

本仓库也内置 GitHub 门禁模板：Actions、CodeQL、Dependabot、CODEOWNERS、PR/Issue 模板、release workflow 和 ruleset 模板。分支保护、secret scanning、environment approval 仍需要在 GitHub 仓库设置中启用。

`skill-manifest.json` 记录当前 Skill 的版本、兼容性、协议和工具清单，便于 agent 在不同项目或不同 agent 平台中判断可用能力。

## 文档语言约定

- 给 agent 看的 Markdown 使用准确英文，例如 `SKILL.md`、`references/`、`templates/`、`profiles/`、`modules/`。
- 给用户看的 Markdown 尽量使用中文，例如 `README.md` 和面向用户的使用说明。
- 如果同一份文档同时服务用户和 agent，优先保持 agent 执行语义准确，再补充简短中文说明。

## 目录结构

```text
SKILL.md                           Skill 入口与协议索引
references/                        按需加载的详细协议
agents/                            Codex UI 元数据

scripts/                           小型、项目无关的 CLI 工具
tools/                             未来可扩展的大型工具包
examples/                          示例输入、诊断会话、工作流产物
templates/                         可复制的 Markdown/JSON 模板
profiles/                          游戏架构 profile
modules/                           可复用能力模块说明
tests/                             脚本与工具测试
```

## 加载模型

`SKILL.md` 是短入口，应该保持精简。

详细协议放在 `references/` 中，只有当前任务需要时才加载。这样主 agent 和责任 agent 不会背负无关上下文。

## 消费项目产物

这个仓库是 Skill 和工具母仓库，不承载具体游戏项目源码，也不保存具体项目的运行证据。

具体游戏项目使用该 Skill 时，应在消费者项目中创建自己的运行目录：

```text
game-project/
  docs/project-notes/
  docs/handoffs/
  docs/reviews/
  docs/decisions/
  docs/archive/
  evidence/screenshots/
  evidence/recordings/
  evidence/logs/
  evidence/test-results/
  evidence/performance/
  evidence/references/
```

临时讨论、缓存、Python 字节码、真机截图、录屏、大型日志不应该进入这个 Skill 仓库。大型 evidence 通常属于具体项目、构建产物或发布证据归档。

Skill 路径必须始终保持干净：agent 工作中生成的 `project-memory.md`、handoff、review、decision、截图说明、日志摘要等运行态 Markdown，都应该写入消费者项目，而不是写进已安装或 vendored 的 Skill 目录。

## 工具维护规则

小型单文件 CLI 放在 `scripts/`。

当工具成长为可复用模块时，移动到 `tools/<tool-name>/`，并配套 README、测试、示例和模块契约。
