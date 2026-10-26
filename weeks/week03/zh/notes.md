# 第 3 周｜Agent Skills 与命令行（Agent Skills and CLI）

## 官方材料 / Official materials

| 材料 Material | 链接 Link |
|---|---|
| 10/6 课件 Slides | [Google Slides](https://docs.google.com/presentation/d/15bPu5c-i8D8McTh6l7SpUPk2n9M_Y-CdDQLfyzL8RD8/edit?usp=sharing) |
| 10/8 嘉宾课件 Guest slides (Lee Robinson) | [Google Drive](https://drive.google.com/file/d/1b8WiBk_lcB3ue-jZMLijSUMLj6SDiF6Z/view?usp=drive_link) |
| 文字稿 / 视频 Transcripts / Video | 官网暂未发布 Not published yet |
| 阅读 Readings | [pstack](https://github.com/cursor/plugins/tree/main/pstack) · [Matt Pocock's skills](https://github.com/mattpocock/skills) · [browse.sh](https://browse.sh) |
| 全部链接 All links | [links.md](../links.md) |

本周官网没有发布课堂文字稿，笔记按公开课件顺序整理。英文版：[../en/notes.md](../en/notes.md)。

---

## 第 5 讲｜10/6：Agent Skills

### 1. 课程事务（Logistics）
- 作业 3 周五截止；
- 发放 Claude Code 额度和 Cursor 额度；
- Cmux 的 Austin 来访；
- 周四嘉宾讲座：Lee Robinson。

### 2. 为什么（Why）
- MCP 适合给编程代理接入第三方服务；
- 大模型非常擅长遵循较长的流程说明，把这种能力暴露出来，是任何代理框架的重要组成部分。

### 3. Agent skills
- 一种动态加载代理能力的标准：面向特定领域；结合代码和提示词；代理按需加载。
- 用途：写文档、做 PowerPoint、数据分析……
- 就像给代理用的脚本（like scripts for agents）。
- 演示：提供一个 skills.md。

### 4. Skill 的分类（Skill categories）
| 类别 | 课件举例 |
|---|---|
| 代码理解与规划 | RePPIT 系列 skill；Matt Pocock 的 grill-me / grill-with-docs；用来建立对任务的心智模型 |
| 验证（Verification） | create-verification-skill |
| 代码风格 | 定义代码层面的最佳实践；适合代码审查代理（有演示） |
| 其他 | 网页解析：<https://browse.sh/>（有演示） |

### 5. 最佳实践（一）
1. **范围聚焦**：一个 skill，只做一件定义清楚的任务。
2. **维护自己的 skill 合集**，方便在不同项目间移植。
3. **挖掘自己的对话记录**：skill 就是用 Markdown 写下的流程，翻翻自己的聊天，看你在哪里介入或纠正过代理。

> "Chefs bring their own knives between kitchens"
> 厨师换厨房，也带着自己的刀。
> —— 第 5 讲课件（引用 poteto）

4. **别花 token 和时间重复造轮子**：给代理配一个 CLI 工具，再用 skill 把样板操作包起来。

### 6. 最佳实践（二）
5. **写清触发场景**：写出应该触发这个 skill 的情境和请求说法。
6. **渐进式披露（progressive disclosure）**：需要时再引用具体文件，补充上下文。
7. **模块化、可组合**。
8. **保留一个验证 skill**，让代理检查自己的工作，形成改进闭环。

### 7. API vs MCP vs Skills
课件再次给出三者对比，内容同[第 2 周](../../week02/zh/notes.md)第 4 讲第 10 节。

---

## 第 6 讲｜10/8：嘉宾 Lee Robinson ——“常驻代理（always-on agents）是怎么工作的”
嘉宾课件标有前瞻性声明和保密标记，这里只按课件顺序概括核心思路，细节请看官方课件。

- **出发点**：第 1 周写的代理在你关掉终端时就停了。常驻代理运行在服务器上，有自己的云端电脑（带桌面、浏览器和文件的小型虚拟机），会保存状态、记忆和 skills，由事件触发（你的消息、定时任务、Slack、电话、后台任务完成等），可以连续工作几个月。
- **人与 AI 协作方式的演进**：复制粘贴聊天 → 终端里的代理（每步你来批准）→ 多个代理在后台/云端并行（你审最终改动）→ 你给一个有自己电脑、工具和记忆的代理发消息，它在你离开后继续干活。从“逐步批准”变成“随时纠偏（steering）”；模型越强，界面越简单。
- **模型的六项新能力**：长时间工作；把子任务交给有全新上下文的助手代理；使用真实工具（shell、文件、浏览器、MCP）；操作电脑屏幕；把知识存成文件（skills、记忆）；看人演示一遍就把步骤存成 skill。
- **知识放在文件里**：记忆和 skills 都是纯文本文件，人和代理都能读、搜、改；skill 只在需要时加载，所以多也不贵。
- **架构要点**：瘦客户端、厚服务器；所有状态存在服务器，虚拟机随时可重建；空闲时休眠、有事件时唤醒；每个会话一次只跑一轮；用**持久化工作流（durable workflow）**而不是简单任务队列，服务器崩了能从断点继续，每一步设计成**幂等（idempotent）**，重试安全。
- **框架设计**：代理的普通文本不直接展示给用户，而是用专门的“发消息”工具和你说话；没有新进展时可以保持安静。

---

## 本周阅读
- **pstack（Cursor plugins）**：Cursor 官方的插件/skills 示例。
- **Matt Pocock's skills**：公开的 skills 仓库（含 grill-me 等）。
- **browse.sh**：让代理浏览网页的工具。

> [!NOTE]
> **补充**
> pstack 和 Matt Pocock 的仓库适合对照学习 skill 的目录结构和写法。
> 
> 动手练习：
> - [ ] 翻自己最近的代理对话，找出 3 处你纠正过它的地方，写成 1 个 skill
> - [ ] 给这个 skill 加“触发场景”说明，并用渐进式披露拆出一个参考文件
> - [ ] 写一个验证 skill，让代理完成任务后自查
