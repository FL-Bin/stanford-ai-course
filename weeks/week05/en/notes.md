# Week 5 · Agent-Ready Codebases

[中文](../zh/notes.md) | **English**

## 官方材料 / Official materials

| 材料 Material | 链接 Link |
|---|---|
| 10/20 课件 Slides | [Google Slides](https://docs.google.com/presentation/d/1yCxocmUrGIN7IrC42WB6NW08PtYYFLe1ombDj3Ay6_8/edit) |
| 10/22 嘉宾 Guest (Eno Reyes, Factory) | 未发课件 No slides published |
| 文字稿 / 视频 Transcripts / Video | 官网暂未发布 Not published yet |
| 阅读 Readings | [Making Codebases Agent Ready (YouTube)](https://www.youtube.com/watch?v=ShuJ_CN6zr4) · [Making Ergonomic Repositories (X)](https://x.com/trybasis/status/2056881705269580023) |
| 全部链接 All links | [links.md](../links.md) |

The 10/20 slides are now published and summarized below in slide order; the 10/22 guest talk and transcripts are not yet published. Chinese version: [../zh/notes.md](../zh/notes.md).

## Lecture 9 · 10/20: Creating agent-ready repositories + background coding agent workflows

### 1. Logistics
- Assignment 4 due Sunday; mid-quarter survey; Thursday guest Eno Reyes (STLC 111).

### 2. Why
- Most codebases aren't set up for agent success; much LLM confusion comes from messy or incomplete developer environments.
- Goal: optimize the codebase and environment so both a human and an agent can understand what's going on.

### 3. What humans work around vs. what breaks agents
| Defect | Human workaround | Effect on agents |
|---|---|---|
| Insufficient tests | Manual testing | Can't verify correctness |
| Outdated docs / no standards | Ask teammates | Can't ensure consistency |
| No linter | Eyeball it | Style drift |
| Flaky build | Retry | Can't verify changes |
| Complex setup | Ask teammates | No reproducible environment |
| Poor observability | Check logs | Can't debug |
| No security scanning | Ignore for now | Introduces vulnerabilities |
| Inconsistent patterns | Tribal knowledge | Learns wrong patterns |

Slide note: mess can be as simple as several DB access patterns, inconsistent naming, or multiple functions doing the same thing.

### 4. Agent-ready environment checklist
Sufficient test coverage; hermetic build; documented, consistent design patterns; no outdated READMEs; verifiable checks; an agent-specific playbook (AGENTS.md etc.).

### 5. What this enables
Large tasks (migrations); multiple agents across a team; automated code review; long-running tasks with verifiable outcomes; agents on brownfield codebases.

### 6. Demo: agent readiness
Factory Agent Readiness (see [links.md](../links.md)); open-source alternative kodustech/agent-readiness.

### 7. Background coding agent workflows
- Progression: tab complete (2021, ~15% gains) → synchronous single task (2024, ~25–35%) → background multi-task (2026+, 2x+).
- Requirements: nearly the same as the readiness checklist, plus isolated development environments.
- Isolation: git worktrees; multi-agent orchestrators (Conductor, Cursor parallel agents, Claude Code swarms, roll your own), which hide setup but can be rigid and don't fully isolate shared resources like databases and ports; cloud agents, launchable from browser, code review tools, chat, mobile, or a ticket.

Textbook chapter: [Chapter 5 · Agent-Ready Codebases](../../../book/en/05-agent-ready-codebases.md).

## Topics (course syllabus)
- **Tue 10/20:** agent readiness of a codebase.
- **Thu 10/22:** guest Eno Reyes (Factory CTO).

## Readings
Making Codebases Agent Ready (video); Making Ergonomic Repositories (X post).

> [!NOTE]
> **Supplement**
> Links to earlier weeks: research docs and specs (week 2) are easier on a clear codebase; AGENTS.md, hooks and subagents (week 4) are direct levers.
> 
> Unofficial readiness checklist: up-to-date AGENTS.md/CLAUDE.md · clear module boundaries · one-command setup and run · fast tests the agent can run · automated lint/format/type checks · error messages that point to the cause.
