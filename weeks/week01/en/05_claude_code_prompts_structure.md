# Claude Code internal prompts (6 files): structure

[中文](../zh/05_提示词合集_ClaudeCode框架拆解.md) | **English**

## 官方材料 / Official materials
| Material | Link |
|---|---|
| Prompts folder | [Google Drive](https://drive.google.com/drive/folders/1c6_atVW0RrqEBWsNIscG2KNwCiuPxWQG?usp=drive_link) |
| Slides (9/24) | [Google Slides](https://docs.google.com/presentation/d/1RZu-p18Qybbgm8WVP2RH04ESc4Bn377B-T9j5-TBFdQ/edit?usp=drive_link) |


The instructor captured these prompts in class. They are not reproduced here; we describe their structure.

1. **system_prompt.md** — identity; security boundaries; harness rules (Markdown output, permission modes, hooks as user feedback, pasted content is not instructions, prefer file tools, parallel calls, `file:line` references); code style; confirm irreversible actions and report honestly; file-based memory with typed frontmatter and a `MEMORY.md` index; environment; context management.
2. **tool_list.md** — tools grouped as files, shell, search/LSP, agents, plan/worktree, scheduling, artifacts, MCP resources, interaction, design/review.
3. **config_files.md** — a fixed override notice followed by the project's CLAUDE.md (overview, structure, run commands, code style).
4. **plan_mode.md** — read-only except the plan file; Phase 1 explore (≤3 Explore subagents), Phase 2 design (≤3 Plan subagents), review, final plan, ExitPlanMode for approval.
5. **subagent_prompt.md** — a performance-analysis brief: constraints, per-file background, required coverage, output format separating measurements from inference.
6. **compaction_prompt.md** — text only, no tools; `<analysis>` then `<summary>` with fixed sections; keep safety constraints verbatim.

> [!NOTE]
> **Supplement**
> Reusable patterns: keep prompts short and sectioned; a good subagent brief = goal + no-go zones + known context + deliverable format; use the compaction checklist for your own handoff notes.
