# 第 6 周｜代理代码审查（Agentic Code Review）

**中文** | [English](../en/notes.md)

## 官方材料 / Official materials

| 材料 Material | 链接 Link |
|---|---|
| 10/27 课件 Slides | [Google Slides](https://docs.google.com/presentation/d/1u8WYtFj0O9yc4H4JX9D4URYKhDzvrAGKLzn38DXSrak/edit) |
| 10/29 嘉宾 Guest (Silas Alberti, Cognition) | 未发课件 No slides published |
| 文字稿 / 视频 Transcripts / Video | 官网暂未发布 Not published yet |
| 阅读 Readings | [Layered Code Review (X)](https://x.com/addyosmani/status/2114604912520921136) · [Cloudflare：大规模编排审查代理](https://blog.cloudflare.com/ai-code-review) · [Greptile：怎么做审查代理](https://greptile.com/blog/how-to-build-a-code-review-agent) |
| 全部链接 All links | [links.md](../links.md) |

10/27 课件已发布，下面按课件顺序用我们自己的话整理；10/29 嘉宾讲座和文字稿官网暂未发布。英文版：[../en/notes.md](../en/notes.md)。

## 第 11 讲｜10/27：代理代码审查——最佳实践与架构

### 1. 课程事务（Logistics）
- 作业 5 周日截止；剩余的模型额度（Grok、Cognition）；周四嘉宾 Silas Alberti（Cognition 首席研究官），之后周四讲座都在 STLC 111。

### 2. 为什么要做代码审查
- 课件的说法：代码审查是提升个人水平和团队代码质量杠杆最高的活动之一。
- 两个作用：发现并修复 bug；让团队对系统形成共同的理解（shared mental model）。
- 课件引用 Blake Smith 的总结：帮团队跟上系统的变化、确认改动真的解决了问题、讨论设计的优缺点、在上线前拦住 bug、保持风格和组织一致。

### 3. 审查能发现什么
逻辑与正确性错误；可读性与可维护性；性能；安全；团队的最佳实践（口口相传的经验）。

### 4. AI 原生的代码审查：成熟度阶梯
- 问题：生成代码的速度上去了，审查没跟上，审查成了新的瓶颈。

| 阶段 | 做法 | 课件评价 |
|---|---|---|
| 0 | 人审查所有改动 | 无法扩展 |
| 1 | 单个代理审查 | 配合自动修复循环更好，但还有提升空间 |
| 2 | 多代理、按风险分级审查，并内置自我改进 | 很多公司正在收敛到的做法；工程规范存进 skill 知识库 |

- 课件引用了 Addy Osmani 的分层审查帖子和 Augment Code 的 Cosmos 文章（见 [links.md](../links.md)）。

### 5. 多代理审查架构
- 一个 PR 同时交给几个专门的审查代理：安全、架构、代码质量、性能，最后由一个汇总裁判（aggregate judge）合并结论。
- 课件以 Cloudflare 的内部工程栈为例，并单独展示了安全审查代理。

### 6. 怎么设计一个审查代理（参考 Greptile）
- **换模型**：审查用的模型和写代码的模型不同（模型反转，model inverter），避免同样的盲点。
- **给足上下文**：不只看 diff。
- **验证**：起一个开发容器，真的跑一遍不同的代码路径。
- **控制成本**：按任务难度选模型。读代码上下文用便宜快的模型；浏览器操作用中小模型、开高推理；深度找 bug 用最强模型。
- **评估**：用历史上含已知 bug 的 PR、以及引发过回滚的事故来测。

### 7. 可选工具
- 通用：Claude Code、Greptile、CodeRabbit、Devin。
- 安全：Vercel deepsec、Wiz、Semgrep。

教材对应章节：[第 6 章 代理代码审查](../../../book/zh/06-代理代码审查.md)。

## 本周主题（官网课程大纲）
- **10/27 周二**：代理代码审查的最佳实践与架构。
- **10/29 周四**：嘉宾 Silas Alberti（Cognition 首席研究官）。
- 大纲列出的三个问题：AI 审查擅长发现什么、会漏掉什么；审查架构和自定义规则；怎么把 AI 审查放进团队的 PR 流程。

## 本周阅读
- **Layered Code Review and Risk-Based Human Oversight（X 帖子）**：分层审查，按风险决定人要看多少。
- **Coordinating Specialist Review Agents at Scale（Cloudflare）**：一个协调代理调度多个专门审查代理，去重、判断严重程度后给出一条审查意见；按改动大小分风险等级，小改动只派少量代理。
- **Beyond the Diff（Greptile）**：从一个简单的审查代理出发，逐步加上提示词优化、模型反转、代码库上下文、自动测试和分任务选模型。

> [!NOTE]
> **补充**
> 和前几周的联系：第 5 周说过，代理就绪的仓库才能放心做自动审查；第 4 周的 AGENTS.md 和 skills 正是存放团队审查规范的地方。
>
> 下面是我们自己按阅读材料整理的要点（非官方）：
>
> | 做法 | 为什么 |
> |---|---|
> | 在提示词里写清「不要报什么」 | 减少吹毛求疵和臆测，让工程师愿意看 |
> | 按改动大小和敏感目录分级 | 改个错字不必派全套代理，省钱 |
> | 审查结果分严重等级 | 只有严重问题才阻止合并 |
> | 留一个人工「强制通过」的口子 | 紧急修复不被卡住 |
>
> 动手练习：
> - [ ] 读完三篇阅读材料
> - [ ] 给自己的一个 PR 用两个不同厂商的模型各审一次，比较它们发现的问题
