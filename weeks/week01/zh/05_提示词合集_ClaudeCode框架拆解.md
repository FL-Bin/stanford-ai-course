# 讲义 05｜提示词合集（Prompts 文件夹，6 个文件）：结构解读

## 官方材料 / Official materials
| 材料 Material | 链接 Link |
|---|---|
| 9/24 提示词文件夹 Prompts | [Google Drive](https://drive.google.com/drive/folders/1c6_atVW0RrqEBWsNIscG2KNwCiuPxWQG?usp=drive_link) |
| 9/24 课件 Slides | [Google Slides](https://docs.google.com/presentation/d/1RZu-p18Qybbgm8WVP2RH04ESc4Bn377B-T9j5-TBFdQ/edit?usp=drive_link) |
| 9/24 文字稿 Transcript | [themodernsoftware.dev](https://themodernsoftware.dev/materials/9-24-26-transcript.txt) |


> 这是讲师在课上抓包得到的 Claude Code 内部提示词。本仓库不转载全文，下面按文件逐个讲结构，并短引个别关键句。

| 文件 | 内容 | 大小 |
|---|---|---|
| system_prompt.md | 系统提示词 | ~965 词 |
| tool_list.md | 内置工具清单（按类别） | ~449 词 |
| config_files.md | CLAUDE.md 被注入时的样子 | ~220 词 |
| plan_mode.md | 计划模式提示词 | ~876 词 |
| subagent_prompt.md | 一次子代理调用的任务说明 | ~432 词 |
| compaction_prompt.md | 上下文压缩（汇总）提示词 | ~1002 词 |

## 1. system_prompt.md（系统提示词）

> "You are an interactive agent that helps users with software engineering tasks."
> 你是一个帮助用户完成软件工程任务的交互式代理。
> —— 9/24 提示词文件夹 system_prompt.md 第 1 行

结构：
1. **身份**（见上）。
2. **安全边界**：允许授权的安全测试、CTF、防御性用途；拒绝破坏性攻击（DoS、供应链攻击等）；双用途工具需要明确的授权场景。
3. **# Harness（框架说明）**：输出以 Markdown 渲染；工具受权限模式（permission mode）控制，被拒绝后调整做法、不原样重试；hook 输出视为用户反馈；`<pasted_content>` 里的指令只有用户本人要求时才执行；优先用专门的文件工具而不是 shell；独立的工具调用可以并行；引用代码用 `file_path:line_number`。
4. 代码风格跟周围代码一致；人称不确定时用 they/them。
5. 不可逆或对外的操作先确认；如实汇报结果（测试失败就直说）。
6. **# Memory（记忆）**：按项目存放的文件式记忆，每条一个文件，带 frontmatter，`type` 分 user / feedback / project / reference，`MEMORY.md` 作索引，`[[name]]` 互相链接；不保存仓库里已有的信息。
7. **# Environment**：可用模型列表等。
8. **# Context management**：上下文会被自动汇总，不用急着收尾；信息够了就动手，给推荐而不是罗列所有选项。

> [!NOTE]
> **补充**
> 写自己的 skill 或 CLAUDE.md 时可以借鉴这份提示词的写法：**短、分区、讲原则**。

## 2. tool_list.md（工具清单）
| 类别 | 工具 |
|---|---|
| Files 文件 | Read, Edit, Write, NotebookEdit |
| Shell | Bash, Monitor |
| 搜索与代码智能 | WebSearch, WebFetch, LSP |
| Agents 代理 | Agent, ListAgents, SendMessage, TaskStop, Workflow |
| 计划与隔离 | EnterPlanMode, ExitPlanMode, EnterWorktree, ExitWorktree |
| 定时 | CronCreate, CronDelete, CronList, ScheduleWakeup, RemoteTrigger |
| Artifacts | Artifact, ArtifactComments, ArtifactData |
| MCP 资源 | ListMcpResourcesTool, ReadMcpResourceTool, ReadMcpResourceDirTool |
| 交互 | AskUserQuestion, Skill, PushNotification, SendFeedback, EndConversation |
| 设计与审查 | DesignSync, ReportFindings |

## 3. config_files.md（配置文件注入）

> "IMPORTANT: These instructions OVERRIDE any default behavior and you MUST follow them exactly as written."
> 重要：这些指令覆盖任何默认行为，你必须严格照写执行。
> —— 9/24 提示词文件夹 config_files.md

- 开头是上面这段固定说明，后面是 CLAUDE.md 全文。
- 以演示用的 todo 项目为例，CLAUDE.md 包括：Project Overview（项目概述）、Project Structure（目录树）、Running the Application（运行命令）、Code Style（类型注解、用 dataclass、函数单一职责）。

> [!NOTE]
> **补充**
> 这份 CLAUDE.md 可以当作一个“够用不过量”的模板来参考。

## 4. plan_mode.md（计划模式）
- 开头是硬约束：计划模式下除计划文件外什么都不许改，只能做只读操作，并且这条优先于其他所有指令。
- 规定计划文件的路径，要求逐步写入。
- **Phase 1 理解需求**：只用 Explore 子代理，最多 3 个并行，通常 1 个就够；要找可复用的已有代码。
- **Phase 2 设计**：派 Plan 子代理（最多 3 个），简单任务可跳过。
- 之后是审查、写最终计划、调用 ExitPlanMode 提交给用户审批。

> [!NOTE]
> **补充**
> 可以照这个结构写自己的“先计划后执行”skill。

## 5. subagent_prompt.md（子代理任务示例）
主代理派给子代理的一份任务书，内容是给 todo 应用做性能分析：
- **约束**：不许改仓库文件；不许碰真实的 `~/.todo_tasks.json`，要用临时路径；脚本放到指定的 scratchpad 目录。
- **背景**：逐个文件说明各模块的实现特点（每次操作都全量读写 JSON、没有缓存和锁、写入不是原子的等）。
- **要覆盖的内容**：复杂度、100/1k/10k 规模下实测、并发与数据完整性、数据无限增长、按影响排序的建议。
- **输出格式**：汇总表 + 实测表 + 带 `file:line` 的详细发现 + 建议；实测事实和推断分开写。

> [!NOTE]
> **补充**
> 好的子代理任务书 = 目标 + 禁区 + 已知背景 + 交付格式。给 Claude Code 派活时可以照着写。

## 6. compaction_prompt.md（压缩提示词）
- 开头强制要求：只输出文本，不许调用任何工具。
- 先在 `<analysis>` 里按时间顺序梳理，再在 `<summary>` 里输出。
- summary 的固定章节：用户的主要请求与意图、关键技术概念、文件与代码片段、错误与修复、问题解决、全部用户消息、待办任务、当前工作、下一步。
- 特别强调：安全相关的约束要逐字保留（verbatim）；只有真正来自用户的消息才算用户消息。

> [!NOTE]
> **补充**
> 手动 `/compact` 或写交接文档时，可以照这份清单来写。
