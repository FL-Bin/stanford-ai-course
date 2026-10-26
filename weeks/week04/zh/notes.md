# 第 4 周｜定制你的代理和代码仓库（Customizing Your Agent and Repository）

**中文** | [English](../en/notes.md)

## 官方材料 / Official materials

| 材料 Material | 链接 Link |
|---|---|
| 10/13 课件 Slides | [Google Slides](https://docs.google.com/presentation/d/152VaUifBKH4T6hxd6fCKKM9kJTSAuBmkF8zSYwuTYAo/edit?usp=sharing) |
| 10/15 嘉宾 Guest (Boris Cherny) | 未发课件 No slides published |
| 文字稿 / 视频 Transcripts / Video | 官网暂未发布 Not published yet |
| 课上示例 Example | [Next.js AGENTS.md](https://github.com/vercel/next.js/blob/canary/AGENTS.md) |
| 阅读 Readings | [I Still Prefer MCP Over Skills](https://david.coffee/i-still-prefer-mcp-over-skills) · [AGENTS.md (Factory)](https://docs.factory.com/harness/agents-md) · [Steering Claude Code](https://claude.com/resources/articles/steering-claude-code-skills-hooks-rules-subagents-and-more) · [Writing a Good CLAUDE.md](https://hlyr.dev/blog/writing-a-good-claude-md) |
| 全部链接 All links | [links.md](../links.md) |

本周官网没有发布课堂文字稿，笔记按公开课件顺序整理；10/15 嘉宾讲座没有公开课件，暂无笔记。英文版：[../en/notes.md](../en/notes.md)。

---

## 第 7 讲｜10/13：定制你的代理环境（Customizing Your Agent Setup）

### 1. 课程事务（Logistics）
- 项目技术规格（tech spec）周四截止；
- 第一次开源贡献周日截止；
- 嘉宾讲座：Boris Cherny；之后所有周四的课都改在 STLC 111。

### 2. API vs MCP vs Skills（回顾）
三者对比同[第 2 周](../../week02/zh/notes.md)。

### 3. MCP 的额外好处（Additional MCP Perks）
认证无缝；版本和更新容易；跨客户端可移植；远程 MCP 天然把能力隔离在沙箱里。

### 4. 为什么要定制（Why）
- 想用编程代理达到最高效率，就得**掌控自己的技术栈**；
- 可用的定制机制有很多。

### 5. 定制代理的手段
代理行为文件（Claude.md / AGENTS.md）、Hooks、Skills、子代理（Subagents）；课上会看这些的真实例子。

### 6. 设计最优的 AGENTS.md

> "README for agent"
> 写给代理看的 README。
> —— 第 7 讲课件

结构：
1. 项目概览（代码库地图）
2. 构建与测试命令（例如：用 maven 而不是 gradle）
3. 代码风格指南
4. 测试说明
5. 安全注意事项
6. 语言或技术栈的特殊陷阱（例如：React 18 + TypeScript，用 Vite，不是 React）

原则：
- 指令尽量**普遍适用**；
- **避免代码片段**，它们很快过时；
- **注意长度**（少于 300 行）；
- 大仓库用**嵌套配置文件**，根目录的 AGENTS.md 当路由，例如：“API 网关设计的更多细节，见 docs/API-GATEWAY.md”；
- 同样的原则适用于 CLAUDE.md 等。

例子：Next.js 仓库的 AGENTS.md。加载顺序：CLAUDE.md 从根目录依次加载到最近的那份，所以最直接相关的指令最后被大模型处理；不同的服务或团队目录可以有不同的约定。

### 7. Hooks（钩子）
- 在预定义事件类型上运行的**确定性脚本**：`PreToolUse`、`PostToolUse`、`UserPromptSubmit`、`PreCompact` 等。
- 用途：清洗用户提示；拦截敏感操作；对生成的代码跑 linter/formatter；任务完成后跑测试。
- Claude Code 和 Cursor 都支持；课件附了 Boris Cherny 在 X 上分享的例子。

### 8. Skills
- 把常用提示词做成文件，让代理执行。
- 用途：跑测试、写计划、做调研、审查代码、验证产出。
- 课上示例：Claude Code 里的 “ship-it” 命令、Cursor 的 “deslop” 命令。

### 9. 子代理（Subagents）
- **运行时委派**。目的：把不同工作流的上下文干净地分开；只返回最终消息。
- 名字、描述、工具列表在会话开始时加载；可隐式或显式调用；把最常见的工作流自动化。
- 用途：探索/理解代码库；改完后简化代码；端到端测试你的应用；**非常适合旁支任务**。
- 对比 Claude.md：它更多是用来锚定行为。

### 10. MCP 服务器（用途）
| 类型 | 例子 | 用途 |
|---|---|---|
| 项目管理 | Jira / Linear | 创建和更新 issue；拉取 issue 信息并开始任务 |
| 文档 | Notion / Confluence | 从功能规格创建 issue |
| 可观测性 | Datadog / Sentry | 实时排查线上问题 |
| 数据库 | Redshift | 排查数据问题；了解数据如何组织 |
| 技术文档 | Context7 | 不再使用过时的库定义；降低幻觉概率 |
| 实验追踪 | Arize | 用测试运行的结果建议新的实验 |

### 11. 上下文的组成（The context story）
系统提示词 → Memory.md → 环境信息 → MCP 工具 → Skills → 全局 AGENTS.md → 本地 AGENTS.md。

> [!NOTE]
> **补充**
> 这些层都会占用上下文预算，叠得越多，留给任务本身的“聪明 token”越少（参见第 2 周的 ½–¾ 原则）。

---

## 第 8 讲｜10/15：嘉宾 Boris Cherny（Anthropic，Claude Code）
官网未发布课件和文字稿，暂无笔记，发布后补上。

---

## 本周阅读
- **I Still Prefer MCP Over Skills**：反方观点，讨论 MCP 与 skills 的取舍。
- **AGENTS.md（Factory 文档）**：AGENTS.md 的写法规范。
- **Steering Claude Code**：Anthropic 关于 skills、hooks、rules、子代理的定制指南。
- **Writing a Good CLAUDE.md**：怎么写好 CLAUDE.md。

> [!NOTE]
> **补充**
> 动手练习：
> - [ ] 按上面的 6 段结构重写自己项目的 AGENTS.md / CLAUDE.md，控制在 300 行内
> - [ ] 加一个 `PostToolUse` hook：改完代码自动跑 formatter 或测试
> - [ ] 试一次“规划 / 实现 / 审查”三个子代理分工
