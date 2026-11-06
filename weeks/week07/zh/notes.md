# 第 7 周｜安全（Security）

**中文** | [English](../en/notes.md)

## 官方材料 / Official materials

| 材料 Material | 链接 Link |
|---|---|
| 课程大纲 Syllabus | [themodernsoftware.dev](https://themodernsoftware.dev)（第 7 周：SAST / SCA 与依赖、密钥泄露；提示词注入与代理攻击面；代理辅助分诊与修复） |
| 11/3 周二 | 校假停课 No class – University holiday |
| 11/5 嘉宾 Guest (Isaac Evans, Semgrep) | 未发课件 No slides published |
| 文字稿 / 视频 Transcripts / Video | 官网暂未发布 Not published yet |
| 阅读 Readings | 官网本周未列；补充阅读见 [links.md](../links.md) |
| 全部链接 All links | [links.md](../links.md) |

本周只有一节嘉宾讲座，官网没有发布课件和阅读。下面按官网列出的三个主题整理要点，完整讲解见 [教材第 7 章](../../../book/zh/07-AI代码库的安全.md)。英文版：[../en/notes.md](../en/notes.md)。

## 第 13 讲｜11/3：停课

斯坦福校假，没有讲座。

## 第 14 讲｜11/5：嘉宾 Isaac Evans（Semgrep CEO）

讲座材料和录像官网暂未发布，公开后补充。相关公开演讲：[When AI Writes Code: Rethinking App Security](https://www.youtube.com/watch?v=TKJGul9TRws)（Lightspeed，2025-11-19）。

## 本周主题要点

> [!NOTE]
> **补充**
> 以下是我们按官网主题自己整理的要点，非课堂内容。

### 1. SAST / SCA、依赖与密钥泄露

- SAST 看自己写的代码，核心是污点追踪：用户输入（源）有没有不经清洗流到危险位置（汇）。
- SCA 看第三方依赖。代理爱顺手装包，版本可能过时，包名也可能根本不存在、被人抢注。
- 密钥扫描放在提交前钩子里最划算，推到远端后只能作废重发。

### 2. 提示词注入与代理特有的攻击面

- 大模型把读到的文字都可能当指令，网页、issue、README 都能夹带注入。
- 「致命三要素」：接触私有数据 + 读不受信任内容 + 能对外通信。三者齐备最危险，至少切断一项。
- MCP 服务器和 skills 本身也是攻击面，只装来源可信的。

### 3. 代理辅助的分诊与修复

- Semgrep 的测试里，Claude Code 和 Codex 找漏洞的真阳性率约 14% 和 18%，同一提示词跑三次结果各不相同。
- 比较稳的分工：规则工具做确定性覆盖，代理去误报、写修复，人做最后确认。
