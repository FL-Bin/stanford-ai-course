# 9/24 lecture notes (transcript order)

[中文](../zh/04_文字稿笔记_9-24_现代编程代理解剖.md) | **English**

## 官方材料 / Official materials
| Material | Link |
|---|---|
| Slides (9/24) | [Google Slides](https://docs.google.com/presentation/d/1RZu-p18Qybbgm8WVP2RH04ESc4Bn377B-T9j5-TBFdQ/edit?usp=drive_link) |
| Transcript (9/24) | [themodernsoftware.dev](https://themodernsoftware.dev/materials/9-24-26-transcript.txt) |
| Prompts folder | [Google Drive](https://drive.google.com/drive/folders/1c6_atVW0RrqEBWsNIscG2KNwCiuPxWQG?usp=drive_link) |
| Video | not published yet |
| Readings | [Lessons from Building Claude Code](https://x.com/trq212/status/2027463795355095314) · [Dive into Claude Code](https://arxiv.org/pdf/2604.14228) |


Our own notes, following the order of the class.

1. **Logistics:** final project with ~4 milestones including a proposal; up to two humans per team; credits for Claude Code, Factory, xAI, Devin; OSS partners next week; waitlist deadline the 27th.
2. **From 200 lines to a modern harness:** everything except the model (the private intelligence layer) is visible. Demo uses Claude Code with Opus 5.5, released two days earlier. Harness design matters for agents in any domain — sales, legal, support.
3. **Method:** a proxy intercepts Claude Code's requests, like Wireshark; building this is the first assignment. Requests contain `model`, `messages` (user/assistant/system), `tools`, `system`; some messages are injected silently by the harness.
4. **Tool list:** ~40 native tools plus `mcp__`-prefixed MCP tools, all sent every request — too many MCP servers crowd the context. MCP tools are primitives; skills chain tools, scripts and prompts and use progressive disclosure. Claude Code's early popularity came partly from a minimalist harness; start with 3–5 versatile tools such as Bash and SQL. Agents talk in natural language because training data is text.
5. **System prompt:** static, harness-controlled, in every request; identity line, safety, harness and session info, a large memory section, environment, context management. Shorter than before (roughly 50–80 lines vs 200–250). Visibility is not a big attack surface — Codex's harness is on GitHub. Flat files often suffice for memory.
6. **CLAUDE.md / AGENTS.md:** the user-controlled counterpart to the system prompt, injected before the first user message with an override notice. Keep it short: run/test/serve commands.
7. **Plan mode:** enter/exit tools; injected plan prompt with phases (understand → design → review → final plan); output is a plan file. Demo: recurring tasks for the todo app.
8. **Skills:** a "check code quality" skill — a command message is injected, then SKILL.md is read into context.
9. **Subagents:** an orchestrator spawns fresh-context workers that report back without polluting the main context.
10. **Hooks and compaction:** hooks briefly; compaction summarizes and replaces context (e.g. 500k → 150k tokens).
11. **Wrap-up:** the trend is simplicity and reliance on the model; "dumb zone" is a joke term for degraded performance in long contexts; prompts are getting shorter.
