# 第 1 讲｜9/22：课程介绍 + 用约 200 行代码写一个 Claude Code

## 官方材料 / Official materials
| 材料 Material | 链接 Link |
|---|---|
| 9/22 课件 Slides | [Google Slides](https://docs.google.com/presentation/d/1uztIhjHAG6O_9QOD1N_3wdhwhABml1fANXEN2dGwdbg/edit?usp=drive_link) |
| 9/22 示例代码 Sample code | [Google Drive](https://drive.google.com/file/d/1DxKa_autBOu9s8DvItodgUAwH_pBg7aR/view?usp=drive_link) |
| 课堂视频 Video | 官网暂未发布 Not published yet |
| 文字稿 Transcript | 官网暂未发布 Not published yet |
| 相关阅读 Reading | [Building a Coding Agent (YouTube)](https://youtube.com/watch?v=s7ZzkdvCMDY) |
| 课程官网 Course site | [themodernsoftware.dev](https://themodernsoftware.dev/) |


> 下面按课件顺序整理。正文是课程内容的精译讲解，蓝色框是原文短引，绿色框是我们的补充。

## 1. 2026 年的现状（State of the World: 2026）
课件这一页是图表，没有文字要点，讲的是 AI 写代码在行业里的普及程度。

## 2. 这对你意味着什么（What That Means For You）
- 全行业更广泛地采用 AI，意味着公司需要你；成为 **“AI 原生（AI-native）”** 是新的目标。
- 但是……**门槛变高了（the floor is higher）**。
- 软件开发者的生产力达到历史最高，所以大家对开发者的期望也随之提高。
- 要专注于**整体的、系统级的思维，架构（architectures）和抽象（abstractions）**；再结合 **AI 优先（AI-first）** 的开发方式，你就不可替代。

## 3. 这门课讲原则，不讲工具

> [!NOTE]
> "This class is about principles not tools"
> 这门课讲的是原则，而不是工具。
> —— 第 1 讲课件

## 4. 一页看懂 10 周（10 weeks in 1 slide）
课件这一页是课程总览图，各周主题见仓库 [README](../../../README.md) 的进度表。

## 5. 核心收获（The Takeaway）
1. **人机协作工程（Human-agent engineering）**
   - 专注于还没被 AI 系统取代的技能；
   - 理解业务和产品；
   - 成为技术架构师，培养对软件系统的好品味（good taste）；
   - 沟通至关重要。
2. **大模型的水平取决于你（LLMs are only as good as you are）**
   - 好的上下文带来好的代码（good context leads to good code）；
   - 如果你自己都理解不了你的代码库，大模型也理解不了；
   - 防止 **AI slop**（AI 生成的低质量内容）。
3. **大胆实验（Experiment aggressively）**。

> [!NOTE]
> "If you can't understand your codebase, neither will an LLM"
> 如果你理解不了自己的代码库，大模型也理解不了。
> —— 第 1 讲课件「The Takeaway」

## 6. 课程安排（Course Logistics）
- **讲师** Mihail Eric：斯坦福本科/研究生；旧金山销售领域创业公司 Monaco 的 AI 负责人；给几十家从种子轮到上市公司做 AI 顾问；在 Amazon Alexa 做过最早的大模型；创办并卖掉过一家机器学习教育公司；创办过一家 YC 投资的 AI 编程公司。
- **助教**：Isaac Kan、Vijay Daita。
- **上课时间**：周二、周四 5:30–6:20 pm（美西时间）。
- **作业与考核**：
  - 6 次作业（每周 1 次），练习课上内容；
  - 给开源（OSS）仓库做 3–4 次贡献；
  - 1 个开放式期末项目，运用课上讲的 AI 编程原则；
  - 评分：项目 50% / 作业 15% / 开源贡献 30% / 课堂参与 5%。
- **开源合作伙伴**：15 个顶尖 AI 原生开源项目，包括 Vercel、Warp、Marimo、Milvus、Pi、CrewAI、Browserbase、HeyGen、CopilotKit、Semgrep、OpenHands、Cmux、Arize、Sloth、Anyscale。
- **嘉宾讲座**：如今领导顶尖 AI 开发团队的创始人和工程负责人（Claude Code、Devin、Replit、Factory 等的创造者）；讲师提醒不要错过。

## 7. 如何用 200 行代码写一个 Claude Code
课件标题页之后一页是 “It's that simple（就这么简单）”。步骤：
1. 在终端读取用户输入，不断追加到对话里；
2. 告诉大模型有哪些工具可用：
   - 模型会在合适的时候请求使用工具；
   - 你在本地（offline）执行工具，再把结果返回给模型；
   - 工具：`Read_file`（读文件）、`List_dir`（列目录）、`Edit_file`（改文件）。
3. 然后现场从零写一个编程代理（Let's build a coding agent from scratch!），代码逐段讲解见 [03_代码讲解](03_代码讲解_约200行的编程代理.md)。

> [!WARNING]
> **补充**
> 整讲可以压缩成一句：**代理 = 一个循环 + 一组工具**。模型不再请求工具时，就输出最终回答，等下一次用户输入。
>
> 自查：
> - [ ] 能用自己的话解释“好上下文 → 好代码”
> - [ ] 能画出 用户 → 代理框架（harness）→ 模型 → 工具 → 结果回填 的循环
