# 第 5 周｜让代码库适合代理协作（Agent-Ready Codebases）

**中文** | [English](../en/notes.md)

## 官方材料 / Official materials

| 材料 Material | 链接 Link |
|---|---|
| 10/20 课件 Slides | 官网暂未发布 Not published yet |
| 10/22 嘉宾 Guest (Eno Reyes, Factory) | 未发课件 No slides published |
| 文字稿 / 视频 Transcripts / Video | 官网暂未发布 Not published yet |
| 阅读 Readings | [Making Codebases Agent Ready (YouTube)](https://www.youtube.com/watch?v=ShuJ_CN6zr4) · [Making Ergonomic Repositories (X)](https://x.com/trybasis/status/2056881705269580023) |
| 全部链接 All links | [links.md](../links.md) |

截至 2026-10-26（北京时间），官网还没有发布本周两讲的课件和文字稿，这里只有官网大纲里的主题和阅读材料。材料发布后会按课程顺序补全。英文版：[../en/notes.md](../en/notes.md)。

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
