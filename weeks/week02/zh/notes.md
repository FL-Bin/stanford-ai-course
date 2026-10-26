# 第 2 周｜进阶上下文工程（Advanced Context Engineering）

**中文** | [English](../en/notes.md)

## 官方材料 / Official materials

| 材料 Material | 链接 Link |
|---|---|
| 9/29 课件 Slides | [Google Slides](https://docs.google.com/presentation/d/17brqoQQZHF3K82WgYaV6urAV3Q7iIwyGUBYRvSuY8QY/edit?usp=sharing) |
| 9/29 文字稿 Transcript | [themodernsoftware.dev](https://themodernsoftware.dev/materials/9-29-26-transcript.txt) |
| 10/1 课件 Slides | [Google Slides](https://docs.google.com/presentation/d/1q2cB1a7P4XsR0UJqE0RmtZFeggNOLdPaSnOpbBVewHA/edit?usp=sharing) |
| 10/1 文字稿 Transcript | [themodernsoftware.dev](https://themodernsoftware.dev/materials/10-1-26-transcript.txt) |
| 10/1 Skills 文件夹 Skills folder | [Google Drive](https://drive.google.com/drive/folders/1aEHCXzZKkokuA4AYjD_2i6OrcM5iQosW?usp=drive_link) |
| 课堂视频 Video | 官网暂未发布 Not published yet |
| 阅读 Readings | [The Context Tax](https://langwatch.ai/blog/context-tax-when-to-compact) · [OpenSpec](https://openspec.dev) · [Superpowers](https://github.com/obra/superpowers) · [Enterprise MCP](https://blog.cloudflare.com/enterprise-mcp) |
| 全部链接 All links | [links.md](../links.md) |

按课件顺序整理；课堂上的补充说明来自官方文字稿。正文是课程内容的精译讲解，引用块是原文短引，蓝色「补充」框是我们自己加的内容。英文版：[../en/notes.md](../en/notes.md)。

---

## 第 3 讲｜9/29：复杂代码库里的进阶提示词与上下文工程

### 1. 课程事务（Logistics）
- Factory 工作坊：周四 6:20–6:45 pm。
- 公布开源合作伙伴计划（OSS partners program）：Anyscale（Ray）、Arize AI（Phoenix）、Browserbase、cmux、CopilotKit、CrewAI、HeyGen、Marimo、OpenHands、Pi、Unsloth AI、Vercel、Warp、Zilliz。

### 2. 目标（Objective）
- 从随手写提示词（ad-hoc prompting）升级到**稳健、可靠的同步 AI 开发流程**。
- 用 AI 快速上手陌生代码库，并系统地完成复杂的编码任务。

### 3. 本讲计划（Lesson Plan）
- 学会快速上手大型陌生代码库；
- 通过 **RePPIT 框架**学习规格驱动工程（spec-driven engineering）：Research 调研、Propose 提方案、Plan 计划、Implement 实现、Test 测试；
- 了解其他规格驱动的 AI 开发框架。

### 4. Vibe coding 会混淆预期
- Vibe coding 有不同定义，但最常见的那种——一路 YOLO、按 Tab 接受 AI 代码——不是本课的重点。
- 课件抛出问题：你会怎么做一个 Mint（记账应用）的克隆？讲师在课上说明：要在生产规模上扩展这样的应用，就得有方法地使用编程代理。

### 5. 写生产级 AI 代码需要有方法

> "You should have an active, functional mental model of how you would build your solution"
> 你应该对自己会怎么搭建这个方案，有一个活跃的、能运转的心智模型。
> —— 第 3 讲课件

**生产级 AI 代码的原则**：理解陌生代码库 → 提出几个方案 → 规划最有希望的方案 → 实现 → 测试。

如今的坏代码有两种：架构上做错了决定，以及（大模型幻觉导致的）功能上不正确的软件。

### 6. 使用 RePPIT
| 字母 | 阶段 | 做什么 | 产出物 |
|---|---|---|---|
| R | Research 调研 | 让代理把代码库整理成一份结构化调研文档：有哪些模块、怎么组织、关键代码在哪；不把原始代码全塞进上下文 | 调研文档 |
| P | Propose 提方案 | 基于调研给出约 2 个方案并对比取舍（讲师经验：超过 2 个收益递减） | 方案对比 |
| P | Plan 计划 | 把选中的方案写成详细计划：改哪些文件、测试怎么做、可观测性、明确写出不做什么（out of scope） | 计划文档 |
| I | Implement 实现 | 让代理按计划实现，这一步的提示词反而最简单 | 代码 |
| T | Test 测试 | 单元、集成、冒烟测试；还可让代理用审查 skill 检查架构、风格、一致性 | 测试与审查报告 |

课件说明：这套流程需要你自己迭代，找到适合自己的做法，但这几个高层要点是不错的起点。讲师在课上提到，调研文档有两个作用：给代理当后续步骤的种子上下文，也帮助他自己建立心智模型。

### 7. 演示（Demo）
功能需求：加一条趋势线，显示各类别随时间的消费。讲师按 RePPIT 一步步走，最后选了只改前端的轻量方案。

### 8. 最佳实践（Best practices）
- 上下文窗口里只有前 **½–¾ 是“聪明” token**；系统提示词、AGENTS.md/CLAUDE.md、任务相关上下文依次占用，再往后就是 **“dumb zone（变笨区）”**。
- **非常仔细地审查规格（spec）**。
- 特别大的功能，拆成任务清单。
- 每完成一项，就把代理做的事写成书面产物（artifact），作为继续下一项的上下文。
- 时刻留意上下文窗口。

课上补充（文字稿）：
- 已有文档维护得好就复用；过时的文档宁可不要，免得误导代理。
- 调研、方案、计划这些“想”的阶段用最强的模型；实现和测试可以用轻一点的模型。
- 没选中的方案留在上下文里会浪费 token，要适时清空或压缩。课上引用的一篇研究认为，大约在 25 万–45 万 token 之间压缩比较合适（因模型而异）。

### 9. 任务委派分类（Task delegation taxonomy）
方式：
1. 直接提示（Simple prompting）
2. 先做计划（Make a plan）
3. 先调研再计划（Research then plan）
4. 多轮“调研→计划”（(Research then plan) × N）

课件的问题：每种方式什么时候用？

> [!NOTE]
> **补充**
> 经验上可以按改动规模选：小改动直接提示，大功能用多轮调研→计划。

### 10. 其他流行框架（Other popular frameworks）
- **Superpowers**：有主见的、端到端引导式流程，用来解决复杂任务；基于 TDD；一组可用于写规格/计划、实现、测试的 agent skills；内置并行。
- **OpenSpec**：开发规格、实现计划等的轻量流程；在“唯一事实来源（source-of-truth）的规格”里追踪变更，并在产生 diff 之后合并，方法很巧妙。

### 11. 规格管理（Spec management）
- 规格放哪？Linear，或者放在本地/Git 里（OpenSpec 的做法）。
- 代码库各部分的设计取舍和决策点，可以放在 `.notes/` 里。

---

## 第 4 讲｜10/1：MCP、工具调用及更多（MCP, Tool-calling, and Beyond）

### 1. 课程事务（Logistics）
- 开源合作伙伴分配今晚公布；**AI slop 得 0 分**；
- 项目开题（proposal）今晚截止；
- Factory 的 Ashley Jepson 开工作坊。

### 2. 为什么（Why）
- 大模型拥有海量但**静态**的世界知识，只有重新训练才会更新；
- 要构建完全自主的系统，需要稳健的方式把**动态数据**送进来。

### 3. MCP（Model Context Protocol，模型上下文协议）
- 一个开放协议，让系统以一种可在各种集成间通用的方式，为 AI 模型提供上下文。

> "In English: standard format for exposing tools to LLMs"
> 说白了：向大模型暴露工具的标准格式。
> —— 第 4 讲课件

### 4. 基础（Basics）
- 不再需要从每个大模型宿主/代理到每个底层工具各建一个连接器（M × N）；
- 不必重新实现认证、错误处理、限流等；
- 用 JSON-RPC 强制统一输出格式；
- 接入工具从 **M × N → M + N** 个连接器。原来是每个大模型到每个 API 各一个连接器，现在通过 MCP 统一。

### 5. 深入一点：术语和流程（MCP A Bit Deeper）
| 术语 | 含义 |
|---|---|
| Host 宿主 | Cursor、Claude Desktop |
| MCP Client 客户端 | 嵌在宿主里的库（每个服务器一个有状态会话） |
| MCP Server 服务器 | 包在某个工具前面的轻量封装 |
| Tool 工具 | 可调用的函数（可以是数据源、API） |

流程：
1. 客户端向 MCP 服务器调用 `tools/list`（你能做什么？）；
2. 服务器返回描述每个工具的 JSON（名字、摘要、JSON schema）；
3. 宿主把这段 JSON 注入模型上下文；
4. 用户提示触发模型，模型输出结构化的工具调用；
5. MCP 服务器执行，对话继续。

MCP 提供 **stdio** 和 **streamable HTTP** 两种传输层。课件图示的例子是“总结 Jack 发来的邮件”：提问 → 获取工具 → 发送问题并选工具和参数 → 调用函数拿到结果 → 返回结果。

### 6. 怎么设计好的 MCP 服务器（方案一）
**MCP 不是 REST API 的包装。** 一对一映射会导致：小工具太多；上下文庞大复杂；代理把太多时间花在编排逻辑上。讲师在课上解释：API 端点是为人设计的，未必是大模型消费信息的最佳方式。

最佳实践：
- **面向结果，而不是面向操作（Design for outcomes not operations）**：`send_payment(user_email)`，而**不是** `get_users(user_id)` → `list_account(user_email)` → `send_payment(account_id)`。
- **参数明确**：不用嵌套字典作为输入。
- **说明就是上下文**：docstring、错误信息等都是提示词。
- **命名便于发现**：工具名加服务前缀。

### 7. 怎么设计好的 MCP 服务器（方案二）
- MCP 服务器数量爆炸时，只暴露两个工具：**search** 和 **execute**；
- 代理调用 search 找到相关工具和定义；
- execute 生成确定性的代码去执行操作；
- 上下文大幅减少，而且与 MCP 服务器的数量无关；**token 减少 90% 以上**。
- 按需加载工具，在数据到达模型前先过滤，用一个简单步骤执行复杂逻辑。课件示例：找到一张 Jira 工单，用 Google Drive 里的信息更新它。

### 8. 进阶 MCP 架构设计（Advanced MCP Architecture Design）
课件引用 Cloudflare 的企业做法（MCP 服务器门户 portal）：员工只需把 MCP 客户端连到门户，门户立刻列出他有权使用的所有内部和第三方 MCP 服务器；此外门户还提供集中日志、一致的策略执行和防数据泄露（DLP）护栏。

### 9. Agent Skills
- 一种**动态加载**代理能力的标准：面向特定领域；结合代码和提示词；代理按需加载。
- 用途：写文档、做 PowerPoint、数据分析……
- 标准见 <https://agentskills.io/home>；课上演示提供一个 skills.md，并展示了 Matt Pocock 的 skills 仓库。

### 10. API vs MCP vs Skills
| | API | MCP | Skills |
|---|---|---|---|
| 是什么 | 应用向开发者暴露的 HTTP/REST/GraphQL 服务接口 | 服务器暴露的工具定义，让大模型代理以标准方式调用 | 可复用的任务包/流程，教代理如何完成一项工作，常编排多个工具/端点 |
| 谁来用 | 你，或 SDK | 模型/代理运行时（作为“工具调用”），而不是每次都写定制集成的人类开发者 | 代理或代理框架，作为它可以调用的更高层能力 |
| 用法 | 认证、重试、分页、输入校验等由你决定 | 与外部资源、数据、服务交互的主要机制 | 工作流抽象：“完成 X 的可重复做法” |

---

## 本周阅读
- **The Context Tax: When to Compact**：什么时候压缩上下文、对成本的影响（课上引用了它的结论）。
- **OpenSpec**、**Superpowers**：上面介绍的两个规格驱动框架。
- **Enterprise MCP（Cloudflare）**：企业如何集中部署和管控 MCP。

> [!NOTE]
> **补充**
> 动手练习：
> - [ ] 用 RePPIT 给自己的一个项目加一个小功能，保存调研、方案、计划三份文档
> - [ ] 写一个只有 2–3 个“面向结果”工具的小 MCP 服务器
> - [ ] 试用 Superpowers 或 OpenSpec，对比和 RePPIT 的差异
