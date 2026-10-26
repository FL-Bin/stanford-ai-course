# Week 3 · Agent Skills and CLI

[中文](../zh/notes.md) | **English**

## 官方材料 / Official materials

| 材料 Material | 链接 Link |
|---|---|
| 10/6 课件 Slides | [Google Slides](https://docs.google.com/presentation/d/15bPu5c-i8D8McTh6l7SpUPk2n9M_Y-CdDQLfyzL8RD8/edit?usp=sharing) |
| 10/8 嘉宾课件 Guest slides (Lee Robinson) | [Google Drive](https://drive.google.com/file/d/1b8WiBk_lcB3ue-jZMLijSUMLj6SDiF6Z/view?usp=drive_link) |
| 文字稿 / 视频 Transcripts / Video | 官网暂未发布 Not published yet |
| 阅读 Readings | [pstack](https://github.com/cursor/plugins/tree/main/pstack) · [Matt Pocock's skills](https://github.com/mattpocock/skills) · [browse.sh](https://browse.sh) |
| 全部链接 All links | [links.md](../links.md) |

No transcripts were published this week; notes follow the public slides, in our own words. Chinese version: [../zh/notes.md](../zh/notes.md).

---

## Lecture 5 · 10/6: Agent Skills

### 1. Logistics
Assignment 3 due Friday; Claude Code and Cursor credits; a visit from Austin (Cmux); Lee Robinson guest lecture on Thursday.

### 2. Why
MCP covers third-party integrations; models are very good at following longer written procedures, and exposing that is a key part of any harness.

### 3. Agent skills
On-demand, domain-specific capabilities combining code and prompts — "like scripts for agents". Use cases: docs, slides, data analysis. Demo: a skills.md.

### 4. Skill categories
Code understanding and planning (RePPIT skills; Matt Pocock's grill-me / grill-with-docs, for building a mental model of a task) · verification (create-verification-skill) · code style (code-level best practices, useful for review agents) · miscellaneous (browser parsing with browse.sh).

### 5. Best practices, part 1
One skill, one clearly defined task. Keep a personal, portable collection. Mine your own chats for the places you stepped in or corrected the agent.

> "Chefs bring their own knives between kitchens"
> 厨师换厨房，也带着自己的刀。
> —— Lecture 5 slides (quoting poteto)

Don't reinvent the wheel: give the agent a CLI and wrap the boilerplate in a skill.

### 6. Best practices, part 2
State the situations and phrases that should trigger the skill; use progressive disclosure (reference files as needed); keep skills modular and composable; keep a verification skill so the agent checks its own work.

### 7. APIs vs MCP vs Skills
Same comparison as [week 2](../../week02/en/notes.md).

---

## Lecture 6 · 10/8: Guest Lee Robinson — "How always-on agents work"
The slides carry a forward-looking statement and a confidentiality mark, so this is only a high-level outline in slide order.

- The week-1 agent dies with the terminal; an always-on agent runs on a server with its own small VM (desktop, browser, files), keeps state, memory and skills, wakes on events, and can work for months.
- Collaboration has moved from copy-paste chat → terminal agents you approve step by step → parallel background agents → messaging an agent that keeps working after you leave. Approval gives way to steering; stronger models allow simpler interfaces.
- New model abilities: long-running work, delegating to fresh-context helpers, real tools, computer use, knowledge stored as files, learning a skill from a demonstration.
- Knowledge lives in plain files that people and agents can read and edit; skills load only when needed.
- Architecture: thin client, thick server; rebuildable VMs; sleep when idle; one turn per session at a time; durable workflows with idempotent steps.
- Harness: the agent talks through a dedicated message tool and can stay quiet when there is nothing new.

---

## Readings
pstack (Cursor plugins), Matt Pocock's skills, browse.sh.

> [!NOTE]
> **Supplement**
> Exercises: turn three of your own corrections to an agent into one skill; add trigger phrases and split out a reference file; write a verification skill.
