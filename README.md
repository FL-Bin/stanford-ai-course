# 斯坦福 AI 课程（中英双语笔记）｜Stanford AI Course

> 斯坦福 CS146S《The Modern Software Developer》的**非官方**学习笔记，与斯坦福大学及课程团队**无任何关联**。课程官网：<https://themodernsoftware.dev/>
> Unofficial notes for Stanford CS146S — **not affiliated with Stanford University** or the course staff. [English below ↓](#english)

这是我一边学习斯坦福 CS146S（主讲 Mihail Eric）一边整理的笔记，每周两个版本：
- `zh/`：中文笔记，关键术语和提示词保留中英双语；
- `en/`：同一份笔记的英文版。

两版都是**我们自己写的转述和讲解**，不是课件、文字稿或论文的原文。所有原始材料都在每周的 `links.md` 里链接到官方地址。

## 阅读说明
笔记用三种样式区分内容来源（第 1 周已按此格式整理，其余各周陆续改版）：
- **正文**：课程内容。按原课件/课堂顺序做贴近原意的精译讲解，不是逐字翻译。
- **蓝色 `[!NOTE]` 框**：原文短引。一两句关键英文原话 + 中文翻译 + 出处（如「—— 第 1 讲课件」）。
- **绿色 `[!TIP]` 框，标题「补充」**：课程里没有、我们自己加的理解、练习和延伸。

每篇笔记开头都有「官方材料 / Official materials」表，列出课件、视频、文字稿、阅读的官方链接。

## 课程进度（跟随官网实时更新）
| 周 | 主题 | 日期（美西） | 状态 |
|---|---|---|---|
| 1 | 编程代理的内部原理 The Internals of Coding Agents | 9/22, 9/24 | ✅ 已更新 → [weeks/week01](weeks/week01/) |
| 2 | 进阶上下文工程 Advanced Context Engineering | 9/29, 10/1 | ✅ 已更新 → [weeks/week02](weeks/week02/) |
| 3 | Agent Skills 与命令行 Agent Skills and CLI | 10/6, 10/8 | ✅ 已更新 → [weeks/week03](weeks/week03/) |
| 4 | 定制代理和仓库 Customizing Your Agent and Repository | 10/13, 10/15 | ✅ 已更新（嘉宾讲座待官方材料）→ [weeks/week04](weeks/week04/) |
| 5 | 让代码库适合代理 Agent-Ready Codebases | 10/20, 10/22 | 🟡 部分更新（官网未发课件）→ [weeks/week05](weeks/week05/) |
| 6 | 代理代码审查 Agentic Code Review | 10/27, 10/29 | ⏳ 待更新 |
| 7 | 安全 Security | 11/3, 11/5 | ⏳ 待更新 |
| 8 | 后台代理 Background Agents | 11/10, 11/12 | ⏳ 待更新 |
| 9 | 打造 AI 原生团队 Building an AI-Native Team | 11/17, 11/19 | ⏳ 待更新 |
| 10 | 软件工厂与未来 The Software Factory + The Future | 12/1, 12/3 | ⏳ 待更新 |

预计 2026 年 12 月上旬随课程结束完成全部 10 周。更新记录见 [CHANGELOG.md](CHANGELOG.md)。

## 怎么用
1. 打开某一周的文件夹，先看 `links.md`，打开官方课件 / 阅读；
2. 再读 `zh/` 或 `en/` 笔记，自查和动手练习放在「补充」框里；
3. 第 1 周建议从 `00_本周索引.md`（英文 `00_index.md`）开始。

目录结构：
```
weeks/weekNN/
  links.md   官方材料链接
  zh/        中文笔记
  en/        English notes
```

## 版权与免责声明
- 本仓库是个人学习笔记，**非官方**，与斯坦福大学、CS146S 课程团队及嘉宾所在公司没有任何关联，也未经其审阅或认可。
- 课件、课堂文字稿、示例代码、提示词文件、论文和阅读材料的版权**归原作者所有**。本仓库**不转载**这些原始材料，只提供官方链接。
- 笔记中偶有为说明概念而引用的极短术语或短语，均注明来源。
- 如果权利人认为某处内容不妥，请提 issue，我会尽快修改或删除。
- 本仓库的笔记（仅限我们自己撰写的内容）采用 [CC BY-NC-SA 4.0](LICENSE) 许可，**该许可不适用于任何被链接的原始材料**。

---
<a id="english"></a>
## Stanford AI Course — bilingual notes for CS146S The Modern Software Developer

Bilingual (Chinese + English) study notes for Stanford **CS146S: The Modern Software Developer**, Fall 2026 (instructor Mihail Eric). Official site: <https://themodernsoftware.dev/>.

Each week has two versions of the same notes: `zh/` (Chinese, key terms and prompts kept bilingual) and `en/` (English). Both are **our own paraphrase and commentary**, not the slides, transcripts or papers. Every original material is linked to its official source in that week's `links.md`.

### How to read
Notes use three styles (week 1 already follows this; other weeks will be converted):
- **Body text** — course content, following the lecture order, in our own words.
- **Blue `[!NOTE]` boxes** — short quotes: one or two original sentences with a Chinese translation and the source.
- **Green `[!TIP]` boxes titled "Supplement"** — our own additions that are not in the course.

Each note starts with an "官方材料 / Official materials" table linking the official slides, video, transcript and readings.

### Progress
Weeks 1–4 are done (the week-4 guest lecture awaits official materials); week 5 is partial because its slides aren't published yet; weeks 6–10 will be added as the course releases them (expected to finish in early December 2026). See the table above and [CHANGELOG.md](CHANGELOG.md).

### How to use
Open a week, start with `links.md` for the official materials, then read the notes in `zh/` or `en/`. Self-checks and exercises sit in the Supplement boxes.

### Disclaimer
- Unofficial personal study notes. **Not affiliated with, reviewed or endorsed by Stanford University**, the CS146S staff, or guest speakers' companies.
- All original materials (slides, transcripts, sample code, prompt files, papers, readings) **belong to their authors**. This repo does not redistribute them; it only links to official sources.
- Rights holders who have concerns: please open an issue and I will fix or remove the content promptly.
- Our own notes are licensed under [CC BY-NC-SA 4.0](LICENSE). **The license covers only our notes, not any linked material.**
