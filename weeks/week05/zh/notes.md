# 第 5 周｜让代码库适合代理协作（Agent-Ready Codebases）

**中文** | [English](../en/notes.md)

## 官方材料 / Official materials

| 材料 Material | 链接 Link |
|---|---|
| 10/20 课件 Slides | [Google Slides](https://docs.google.com/presentation/d/1yCxocmUrGIN7IrC42WB6NW08PtYYFLe1ombDj3Ay6_8/edit) |
| 10/22 嘉宾 Guest (Eno Reyes, Factory) | 未发课件 No slides published |
| 文字稿 / 视频 Transcripts / Video | 官网暂未发布 Not published yet |
| 阅读 Readings | [Making Codebases Agent Ready (YouTube)](https://www.youtube.com/watch?v=ShuJ_CN6zr4) · [Making Ergonomic Repositories (X)](https://x.com/trybasis/status/2056881705269580023) |
| 全部链接 All links | [links.md](../links.md) |

10/20 课件已于 2026-10-26 前后发布，下面按课件顺序整理；10/22 嘉宾讲座和两讲的文字稿官网暂未发布。英文版：[../en/notes.md](../en/notes.md)。

## 第 9 讲｜10/20：打造适合代理的仓库 + 后台编程代理工作流

### 1. 课程事务（Logistics）
- 作业 4 周日截止；期中问卷；周四嘉宾 Eno Reyes（STLC 111）。

### 2. 为什么（Why）
- 如今大多数代码库并没有为代理的成功做好准备；模型的很多困惑，来自在凌乱或不完整的开发环境里完成任务。
- 目标：优化代码库和环境，让人和代理都能看懂发生了什么。

### 3. 人能绕过的 vs 让代理失败的
| 缺陷 | 人的办法 | 对代理的影响 |
|---|---|---|
| 测试不足 | 手动测试 | 无法验证正确性 |
| 文档过时 / 无规范 | 问同事 | 无法保证一致性 |
| 没有 linter | 自己看 | 风格漂移 |
| 构建不稳定 | 重试 | 无法验证改动 |
| 配置复杂 | 问同事 | 环境不可复现 |
| 缺少可观测性 | 翻日志 | 无法调试 |
| 没有安全扫描 | 先不管 | 引入漏洞 |
| 写法不统一 | 隐性经验 | 学到错误模式 |

课件备注：凌乱可以很简单，比如访问数据库有多种写法、变量命名不一、多个函数做同一件事。

### 4. 代理就绪环境清单
足够的测试覆盖；封闭（hermetic）构建；有文档且一致的设计模式；没有过时的 README；可验证的检查；写给代理的操作手册（AGENTS.md 等）。

### 5. 就绪之后能做什么
大任务（迁移等）；团队多人运行多个代理；自动代码审查；结果可验证的长时间任务；在老代码库上用代理。

### 6. 演示：代理就绪度
Factory Agent Readiness（见 [links.md](../links.md)）；开源替代 kodustech/agent-readiness。

### 7. 后台编程代理工作流
- 能力演进：Tab 补全（2021，约 15% 效率提升）→ 同步单任务（2024，约 25–35%）→ 后台多任务（2026+，有望 2 倍以上）。
- 后台代理的前提：和上面的就绪清单几乎相同，外加隔离的开发环境。
- 隔离方式：git worktree；多代理编排工具（Conductor、Cursor 并行代理、Claude Code 多代理、自己写），优点是省去底层配置，缺点是界面可能死板、数据库和端口等共享资源没完全隔离；云端代理，可从浏览器、代码审查平台、聊天工具、手机、任务系统里启动。

教材对应章节：[第 5 章 让代码库适合代理](../../../book/zh/05-让代码库适合代理.md)。

## 本周主题（官网课程大纲）
- **10/20 周二**：代码库的“代理就绪度（agent readiness）”。
- **10/22 周四**：嘉宾 Eno Reyes（Factory CTO）。

## 本周阅读
- **Making Codebases Agent Ready（视频）**：怎么让代码库适合代理工作。
- **Making Ergonomic Repositories（X 帖子）**：怎么把仓库做得顺手。

> [!NOTE]
> **补充**
> 和前几周的联系：第 2 周的调研文档和规格能帮代理快速上手陌生代码库，代码库本身越清晰，这一步越省事；第 4 周的 AGENTS.md、hooks、子代理是让仓库适合代理的直接手段。
> 
> 代理就绪度自查清单（我们自己整理，非官方）：
> 
> | 方面 | 检查项 |
> |---|---|
> | 文档 | 有 AGENTS.md/CLAUDE.md，写清项目地图、构建/测试命令、风格和注意事项；文档没有过时 |
> | 结构 | 目录和模块边界清楚；命名一致；大仓库有嵌套说明 |
> | 构建 | 一条命令装好依赖，一条命令跑起来 |
> | 测试 | 有能快速运行的测试；代理改完能自己验证 |
> | 检查 | lint、格式化、类型检查能自动跑（可接 hooks/CI） |
> | 反馈 | 错误信息清楚，代理能从报错里找到原因 |
> 
> 动手练习：
> - [ ] 看完视频，读完帖子
> - [ ] 用上面的清单给自己的一个仓库打分，挑最低的一项改进
