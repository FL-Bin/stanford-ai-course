# Lecture 2 · 9/24: The Anatomy of a Modern Coding Agent

[中文](../zh/02_第2讲_9-24_现代编程代理解剖.md) | **English**

## 官方材料 / Official materials
| Material | Link |
|---|---|
| Slides (9/24) | [Google Slides](https://docs.google.com/presentation/d/1RZu-p18Qybbgm8WVP2RH04ESc4Bn377B-T9j5-TBFdQ/edit?usp=drive_link) |
| Transcript (9/24) | [themodernsoftware.dev](https://themodernsoftware.dev/materials/9-24-26-transcript.txt) |
| Prompts folder | [Google Drive](https://drive.google.com/drive/folders/1c6_atVW0RrqEBWsNIscG2KNwCiuPxWQG?usp=drive_link) |
| Video | not published yet |
| Readings | [Lessons from Building Claude Code](https://x.com/trq212/status/2027463795355095314) · [Dive into Claude Code](https://arxiv.org/pdf/2604.14228) |


Notes follow the slide order, in our own words. Demo details are in [04](04_lecture_notes_9-24.md).

## 1. Logistics
Final project spec released (one extra human teammate allowed, agents unlimited); credits from Claude, Factory, xAI and Devin; OSS details next week; course applications close 9/27.

## 2. Recap and a state-of-the-art agent
Back to the core loop, then the subject of the day: Claude Code.

## 3. Harnesses are more complex
The instructor frames harness design as one of the central problems in coding agents. Its parts: system prompt, configuration files (AGENTS.md etc.), tool list, plan mode, subagents, skills, hooks, compaction.

## 4. Tool list
A small set of strong capabilities (search, shell, agent tasks); about 40 built-in tools in Claude's case; MCP tools also load into context; every tool's name, description and signature is itself prompt text.

## 5. System prompt
The system-level blueprint: harness behavior, guardrails, and environment.

## 6. Agent configuration files
User-level customization (CLAUDE.md / AGENTS.md) that takes precedence over other instructions.

## 7. Plan mode
A dedicated tool that has the agent write a spec for a change and ask clarifying questions.

## 8. Skills
A written procedure — a prompt plus tool calls and/or local scripts — invoked by the agent or by the user.

## 9. Subagents
Started via a tool call; fresh context with its own system prompt; parallelizable at higher token cost; result returned to the parent.

## 10. Hooks
Prompts or code inserted at lifecycle points, useful for pre/post-processing; best practices come later.

## 11. Compaction
Near the context limit, summarize the run and replace history with the summary; manual or automatic; lossy, so you may want your own.

## 12. Principles of effective harnesses
Simplicity (fewer, more powerful tools such as SQL or bash); mind the context window and avoid the "dumb zone" caused by tool bloat; expect prompts to keep changing, so keep them easy to adjust.

> [!NOTE]
> **Supplement**
> Self-check: name the eight parts and say which ones sit in context permanently and which load on demand.
