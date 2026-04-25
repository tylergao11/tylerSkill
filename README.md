# Agent Collaboration OS

这是一个可安装、可迁移、可版本化的 Agent 协作操作系统 Skill。

它的目标不是让用户手动调用各种脚本，而是让用户安装 Skill 之后，把项目协作、开发前设计、调试诊断、回归检查、发布风险判断交给 agent 按规范执行。

所有文本文件必须使用 UTF-8。

## 使用方式

普通用户只需要安装这个 Skill。

安装后，在项目中告诉主 agent 使用 Agent Collaboration OS，它会按需读取 `SKILL.md` 和 `references/` 中的协议，并在需要时调用 `scripts/` 里的工具。

这些工具主要面向 agent：

- `scripts/design_packet_validator.py`：检查开发 agent 的工程设计说明是否完整。
- `scripts/impact_analyzer.py`：根据改动文件推断影响范围和回归检查。
- `scripts/diff_risk_reviewer.py`：在开发 agent 声称完成前检查 diff 风险。
- `scripts/debug_bisection.py`：在疑难问题中用二分诊断代替逐个猜测修改。

用户不需要记住这些命令。它们是 Skill 的内部能力，主 agent 和责任 agent 会在合适的协议中调用。

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

## 工具维护规则

小型单文件 CLI 放在 `scripts/`。

当工具成长为可复用模块时，移动到 `tools/<tool-name>/`，并配套 README、测试、示例和模块契约。
