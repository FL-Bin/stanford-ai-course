# 第 8 周｜后台代理（Background Agents）

**中文** | [English](../en/notes.md)

## 官方材料 / Official materials

| 材料 Material | 链接 Link |
|---|---|
| 课程大纲 Syllabus | [themodernsoftware.dev](https://themodernsoftware.dev)（第 8 周：异步、委派到云端的代理；管理并行代理群；从 issue 到 PR 的流水线和触发方式（Slack、Linear、GitHub）） |
| 11/10 课件 Slides | [Google Slides](https://docs.google.com/presentation/d/1R8Pr3RNAFQiw8mHKbXopOhxi_h9zuEeUKrJkxCZ5Fio/edit) |
| 11/12 嘉宾 Guest (Rajesh Bhatia, Cloudflare) | 未发课件 No slides published |
| 文字稿 / 视频 Transcripts / Video | 官网暂未发布 Not published yet |
| 阅读 Readings | [Spotify：从迁移脚本到代理群](https://engineering.atspotify.com/2025/11/spotifys-background-coding-agent-part-1) · [Stripe：从 Slack 消息到可审查的 PR](https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents) · [Ramp：让代理有工具证明自己的工作](https://builders.ramp.com/post/why-we-built-our-background-agent) · [LangChain：开源软件工厂 open-swe](https://github.com/langchain-ai/open-swe) |
| 全部链接 All links | [links.md](../links.md) |

11/10 课件已发布，下面按课件顺序用我们自己的话整理，再逐篇概括四篇阅读；11/12 嘉宾讲座官网暂未发布材料。完整讲解见 [教材第 8 章](../../../book/zh/08-后台代理.md)。英文版：[../en/notes.md](../en/notes.md)。

## 第 15 讲｜11/10：后台代理——异步启动任务

### 1. 课程事务（Logistics）
- OSS 贡献第 3 次周日截止；周四嘉宾 Rajesh Bhatia（Cloudflare 高级总监），之后周四讲座都在 STLC 111。

### 2. 回顾：编程代理能力的三个阶段

| 阶段 | 课件给的效率提升 |
|---|---|
| Tab 补全（2021） | 约 15% |
| 同步、一次一个任务（2024） | 约 25–35% |
| 后台、多任务并行（2026 起） | 2 倍以上 |

- 课件的意思：第三阶段的关键是在异步环境里同时派出多个任务，换来大规模并行。第 6 周的代理代码审查已经是这种形态。

### 3. 为什么要放到后台：本地开发环境的终结（End of Localhost）
- 不再有「在我电脑上能跑」的依赖问题；
- 环境可复现、可控制；
- 测试在专用实例上跑；
- 理论上可以无限并行。

### 4. 自建后台代理平台
- 定义：一个系统接到任务，拉起一个接近生产的开发环境，端到端跑完整个流程，最后交回一个 PR。
- 课件说这已经是很多公司的潮流，有的每周完全自主地交付上千个 PR。
- 组成部分：
  - 临时的、可复现的开发环境；
  - 能访问完整代码库、服务、构建系统、文档、代码搜索、日志、指标，常常还有从生产导出的只读数据；
  - 构建、lint、跑测试、推送都由平台隐式完成；
  - 这些是大规模并行的前提。
- 可以用 Coder 当沙箱底座，Gitpod 以前也是选项；开源参考实现是 LangChain 的 open-swe。

### 5. 沙箱提供方
Coder、Vercel Sandbox、Daytona、E2B、Modal 等（链接见 [links.md](../links.md)）。

### 6. Slack 机器人的架构
- 课件用一页架构图讲从 Slack 消息发起任务的流程（图未转载，见课件）。

### 7. 多代理模式
- **代理团队（Agent teams）**：课件引用 Claude Code 文档里的两个用法。一是让 5 个代理各自调查一个假设，互相反驳，最后把共识写进调查文档；二是开三个审查代理分别看安全、性能和测试覆盖。
- **生成者—验证者（Generator-verifier）**：一个代理写，另一个代理审。
- **主模型 + 聪明朋友（Primary model with smart friend）**：便宜快速的主模型在遇到难点时去问更强的模型。
- 后两种模式的出处是 Cognition 的 Walden Yan 的文章（见 [links.md](../links.md)）。

### 8. 编排多代理需要的「元技能」
- 委派和多线程；
- 规划、划定范围、做架构；
- 对任务保持控制，掌握上下文；
- 开工前先花时间判断任务的复杂度；
- 规划窗口和快速任务窗口分开；
- 读代码、读计划的能力，因为审查是新的瓶颈；
- 代理数量要一步步加上去，不要一开始就铺开。

## 第 16 讲｜11/12：嘉宾 Rajesh Bhatia（Cloudflare 高级总监）

讲座材料和录像官网暂未发布。讲者在 LinkedIn 预告里说，这场讲的是合上电脑之后编程代理在做什么：它跑在哪里、谁掌握密钥、等待时花多少钱、出了问题怎么通知人，并介绍 Cloudflare 的架构和真实用户用起来之后站得住的七条原则（七条的具体内容尚未公开）。他说会在讲座后分享课件，公开后补充。相关公开演讲：[Cloudflare's AI Engineering Stack: Assisted to Delegated](https://www.youtube.com/watch?v=MbLdrAZFQRs)（Ona，2026-05-06）。

## 本周阅读要点

### Spotify：从迁移脚本到代理群（Honk 第 1 部分）
- Spotify 原有的 Fleet Management 用代码改代码，把同一个变换批量应用到几千个组件并自动开 PR；2024 年年中起，大约一半的 PR 来自这套系统。
- 复杂变换很难写，比如 Maven 依赖更新脚本为了处理边角情况涨到两万多行。于是他们把「变换脚本」换成「给代理的提示词」，选仓库、开 PR、审查、合并这些外围设施保持不变。
- 已有 1,500 多个代理生成的 PR 被合并，迁移类任务比手写节省 60–90% 的时间。
- 同一个代理后来也通过 MCP 暴露到 Slack 和 GitHub，用来做临时任务。

### Stripe：从 Slack 消息到可审查的 PR（Minions）
- 每周有一千多个合并的 PR 完全由 minion 产出，人只审查，不写代码。
- 典型流程从一条 Slack 消息开始，到一个通过 CI、可以给人审的 PR 结束，中间没有交互。
- 运行在预热好的 devbox 上，约 10 秒拉起，与生产和互联网隔离，所以不需要人逐项批准权限。
- 代理循环和确定性代码交替执行，保证 lint、git 操作这些必需步骤一定会跑；CI 最多跑两轮。

### Ramp：让代理有工具证明自己的工作（Inspect）
- 每个会话跑在 Modal 的沙箱虚拟机里，带齐工程师本地有的一切；仓库镜像每 30 分钟重建一次，会话从快照启动。
- 后端改动能跑测试、查遥测和功能开关，前端改动能截图和给出实时预览。
- 支持 Slack、网页、Chrome 扩展、PR 评论、网页版 VS Code 等多个入口，并支持多人共用一个会话。
- 文章发布时，前后端仓库合并的 PR 中约 30% 由 Inspect 写成。

### LangChain：开源软件工厂（open-swe，现名 Robin）
- 基于 Deep Agents 和 LangGraph，流程是调查代码库、在隔离沙箱里实现、验证、交付 PR，之后继续处理审查、CI 和反馈。
- 入口包括控制台、GitHub issue 和 PR 对话、Slack、Linear。
- README 明确提醒：沙箱权限很大，要用最小权限的凭据，限制仓库和集成范围。

> [!NOTE]
> **补充**
> 四篇阅读可以对照着读：Spotify 讲「为什么要从脚本换成代理」，Stripe 讲「怎么让代理用上公司已有的工程基础设施」，Ramp 讲「怎么让环境快到不需要节省」，open-swe 是能直接看代码的参考实现。读完不妨用教材第 8 章的五个问题（在哪跑、从哪来、拿什么、怎么证明、交给谁）给每家打个表。
