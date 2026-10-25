# 第 4 周｜定制你的代理和代码仓库（Customizing Your Agent and Repository）
> 我们自己的学习笔记（转述 + 讲解），不是课件原文。官方材料见 [links.md](../links.md)。英文版：[../en/notes.md](../en/notes.md)。
> 本周官网没有发布课堂文字稿；10/15 嘉宾讲座（Boris Cherny）没有公开课件，暂无笔记。

---
## 第 7 讲｜10/13：定制你的代理环境
### 为什么要定制
- 想把编程代理的效率用到极致，就得**掌控自己的整套工具链**；可用的定制手段很多。
- 四种主要手段：**代理行为文件（CLAUDE.md / AGENTS.md）、Hooks、Skills、子代理（Subagents）**，再加上 MCP 服务器。

### MCP 的额外好处（补充第 2 周）
认证无缝；版本和更新容易；跨客户端可移植；远程 MCP 天然把能力隔离在沙箱里。

### 怎么写一个好的 AGENTS.md
把它当成**写给代理看的 README**。建议结构：
1. 项目概览（代码库地图）
2. 构建与测试命令（比如“用 maven，不用 gradle”）
3. 代码风格
4. 测试说明
5. 安全注意事项
6. 语言/技术栈的特殊坑（比如“React 18 + TypeScript，用 Vite”）

原则（转述）：
- 指令尽量**普遍适用**；**少放代码片段**，它们很快过时。
- **控制长度**（课件建议少于 300 行）。
- 大仓库用**嵌套配置**：根目录的 AGENTS.md 当“路由”，指向子目录文档（如“API 网关设计详见 docs/API-GATEWAY.md”）。不同服务或团队目录可以有各自的约定。
- 加载顺序：CLAUDE.md 从根目录一路加载到离当前文件最近的那份，**最相关的指令最后被模型读到**。
- 课上举的真实例子：Next.js 仓库的 AGENTS.md。
- 同样的原则也适用于 CLAUDE.md 等其他代理配置文件。

### Hooks（钩子）
- 在预定义事件上运行的**确定性脚本**：`PreToolUse`、`PostToolUse`、`UserPromptSubmit`、`PreCompact` 等。
- 用途：清洗用户输入；拦截敏感操作；对生成的代码自动跑 linter/formatter；任务完成后自动跑测试。
- Claude Code 和 Cursor 都支持。

### Skills / 常用命令
- 把常用提示词做成文件，让代理直接执行：跑测试、写计划、做调研、审代码、验证产出。
- 课上提到的例子：Claude Code 里的 “ship-it” 命令、Cursor 的 “deslop”（清理 AI 冗余代码）命令。

### 子代理（Subagents）
- **运行时委派**：把不同工作流的上下文干净地隔开，只返回最终结果。
- 名字、描述、工具列表在会话开始时加载；可以隐式或显式调用。
- 适合：探索/理解代码库、改完后简化代码、端到端测试——**特别适合旁支任务**。
- 和 CLAUDE.md 的区别：CLAUDE.md 偏向“锚定行为”，子代理偏向“分工执行”。

### 常用的 MCP 服务器类型
| 类型 | 例子 | 用途 |
|---|---|---|
| 项目管理 | Jira / Linear | 建/改 issue，拉取 issue 信息并开工 |
| 文档 | Notion / Confluence | 从功能规格生成 issue |
| 可观测性 | Datadog / Sentry | 实时排查线上问题 |
| 数据库 | Redshift | 排查数据问题、了解数据组织 |
| 技术文档 | Context7 | 避免用到过时的库定义，减少幻觉 |
| 实验追踪 | Arize | 根据测试结果建议新的实验 |

### “上下文的组成”
一次请求的上下文大致由这些层叠起来：系统提示词 → 记忆文件（Memory.md）→ 环境信息 → MCP 工具 → Skills → 全局 AGENTS.md → 本地 AGENTS.md。每一层都在花你的上下文预算。

---
## 第 8 讲｜10/15：嘉宾 Boris Cherny（Claude Code 作者，Anthropic）
官网未发布课件和文字稿，暂无笔记。发布后补上。

---
## 本周阅读（导读）
- **I Still Prefer MCP Over Skills**：反方观点，帮助思考 MCP 与 skills 的取舍。
- **AGENTS.md（Factory 文档）**：AGENTS.md 的写法规范。
- **Steering Claude Code**：Anthropic 官方关于 skills、hooks、rules、子代理的定制指南。
- **Writing a Good CLAUDE.md**：怎么写好 CLAUDE.md。

## 动手练习
- [ ] 按上面的 6 段结构重写自己项目的 AGENTS.md / CLAUDE.md，控制在 300 行内
- [ ] 加一个 `PostToolUse` hook：改完代码自动跑 formatter 或测试
- [ ] 试一次“规划 / 实现 / 审查”三个子代理分工

