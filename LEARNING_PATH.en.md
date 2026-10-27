# Learning Path

[中文](LEARNING_PATH.md) | **English**

Read from week 1 to week 10 in class order. Each lecture lists the date, topic, speaker, our notes (zh/en), and official slides and readings.

Want structured study? Read the [textbook](book/en/00-contents.md) or download its PDF: [English](https://github.com/gaibin/stanford-ai-course/releases/download/pdf-latest/CS146S-book-en.pdf) · [中文版](https://github.com/gaibin/stanford-ai-course/releases/download/pdf-latest/CS146S-book-zh.pdf). Weekly notes (appendix) PDF: [English](https://github.com/gaibin/stanford-ai-course/releases/download/pdf-latest/CS146S-notes-en.pdf) · [中文版](https://github.com/gaibin/stanford-ai-course/releases/download/pdf-latest/CS146S-notes-zh.pdf). All rebuilt automatically.

- Dates are US Pacific time.
- Original materials are linked to official sources only; copyright belongs to their authors. Some slides may require a Stanford account.
- Video: as of 2026-10-27 the course site has published no lecture recordings, so most lectures still say "No public video". Lee Robinson's 10/8 guest lecture has a public video he posted on X. Videos that are official readings are marked separately.

## Week 1 · The Internals of Coding Agents

### 9/22 (Tue) · Course intro + build Claude Code in 200 lines

- Speaker: Mihail Eric
- Textbook: [Chapter 1](book/en/01-how-coding-agents-work.md)
- Notes: [中文](weeks/week01/zh/01_第1讲_9-22_课程介绍与200行ClaudeCode.md) · [English](weeks/week01/en/01_lecture_9-22_intro_and_minimal_agent.md)
- Official materials: [Slides](https://docs.google.com/presentation/d/1uztIhjHAG6O_9QOD1N_3wdhwhABml1fANXEN2dGwdbg/edit) · [Code](https://drive.google.com/file/d/1DxKa_autBOu9s8DvItodgUAwH_pBg7aR/view)
- Video: No public video

### 9/24 (Thu) · How state-of-the-art coding agents are designed: system prompts deep dive

- Speaker: Mihail Eric
- Textbook: [Chapter 1](book/en/01-how-coding-agents-work.md)
- Notes: [中文](weeks/week01/zh/02_第2讲_9-24_现代编程代理解剖.md) · [English](weeks/week01/en/02_lecture_9-24_anatomy_of_a_coding_agent.md)
- Official materials: [Slides](https://docs.google.com/presentation/d/1RZu-p18Qybbgm8WVP2RH04ESc4Bn377B-T9j5-TBFdQ/edit) · [Prompts](https://drive.google.com/drive/folders/1c6_atVW0RrqEBWsNIscG2KNwCiuPxWQG) · [Transcript](https://themodernsoftware.dev/materials/9-24-26-transcript.txt)
- Video: No public video

**Readings:** [Building a Coding Agent (video)](https://youtube.com/watch?v=s7ZzkdvCMDY) · [Lessons from Building Claude Code](https://x.com/trq212/status/2027463795355095314) · [Dive into Claude Code](https://arxiv.org/pdf/2604.14228)

All links: [weeks/week01/links.md](weeks/week01/links.md)

## Week 2 · Advanced Context Engineering

### 9/29 (Tue) · Advanced prompting + agentic dev frameworks (RePPIT, spec-driven development)

- Speaker: Mihail Eric
- Textbook: [Chapter 2](book/en/02-context-engineering-and-spec-driven-development.md)
- Notes: [中文](weeks/week02/zh/notes.md) · [English](weeks/week02/en/notes.md)
- Official materials: [Slides](https://docs.google.com/presentation/d/17brqoQQZHF3K82WgYaV6urAV3Q7iIwyGUBYRvSuY8QY/edit) · [Transcript](https://themodernsoftware.dev/materials/9-29-26-transcript.txt)
- Video: No public video

### 10/1 (Thu) · Full introduction to MCP and tool-calling

- Speaker: Mihail Eric
- Textbook: [Chapter 3](book/en/03-tools-and-capabilities-mcp-and-skills.md)
- Notes: [中文](weeks/week02/zh/notes.md) · [English](weeks/week02/en/notes.md)
- Official materials: [Slides](https://docs.google.com/presentation/d/1q2cB1a7P4XsR0UJqE0RmtZFeggNOLdPaSnOpbBVewHA/edit) · [Skills](https://drive.google.com/drive/folders/1aEHCXzZKkokuA4AYjD_2i6OrcM5iQosW) · [Transcript](https://themodernsoftware.dev/materials/10-1-26-transcript.txt)
- Video: No public video

**Readings:** [The Context Tax: When to Compact](https://langwatch.ai/blog/context-tax-when-to-compact) · [OpenSpec](https://openspec.dev) · [Superpowers](https://github.com/obra/superpowers) · [Enterprise MCP (Cloudflare)](https://blog.cloudflare.com/enterprise-mcp)

All links: [weeks/week02/links.md](weeks/week02/links.md)

## Week 3 · Agent Skills and CLI

### 10/6 (Tue) · All about agent skills (including web skills)

- Speaker: Mihail Eric
- Textbook: [Chapter 3](book/en/03-tools-and-capabilities-mcp-and-skills.md)
- Notes: [中文](weeks/week03/zh/notes.md) · [English](weeks/week03/en/notes.md)
- Official materials: [Slides](https://docs.google.com/presentation/d/15bPu5c-i8D8McTh6l7SpUPk2n9M_Y-CdDQLfyzL8RD8/edit)
- Video: No public video

### 10/8 (Thu) · Guest lecture

- Speaker: Lee Robinson (guest)
- Textbook: [Chapter 3](book/en/03-tools-and-capabilities-mcp-and-skills.md)
- Notes: [中文](weeks/week03/zh/notes.md) · [English](weeks/week03/en/notes.md)
- Official materials: [Slides](https://drive.google.com/file/d/1b8WiBk_lcB3ue-jZMLijSUMLj6SDiF6Z/view)
- Video: [Public video (Lee Robinson on X)](https://x.com/leerob/status/2108650243365736855)

**Readings:** [pstack](https://github.com/cursor/plugins/tree/main/pstack) · [Matt Pocock's Skills](https://github.com/mattpocock/skills) · [browse.sh](https://browse.sh)

All links: [weeks/week03/links.md](weeks/week03/links.md)

## Week 4 · Customizing Your Agent and Repository

### 10/13 (Tue) · Customizing your agentic setup (CLAUDE.md, AGENTS.md, hooks)

- Speaker: Mihail Eric
- Textbook: [Chapter 4](book/en/04-customizing-your-agent.md)
- Notes: [中文](weeks/week04/zh/notes.md) · [English](weeks/week04/en/notes.md)
- Official materials: [Slides](https://docs.google.com/presentation/d/152VaUifBKH4T6hxd6fCKKM9kJTSAuBmkF8zSYwuTYAo/edit)
- Video: No public video

### 10/15 (Thu) · Guest lecture

- Speaker: Boris Cherny (guest)
- Textbook: [Chapter 4](book/en/04-customizing-your-agent.md)
- Notes: [中文](weeks/week04/zh/notes.md) · [English](weeks/week04/en/notes.md)
- Official materials: not published on the site yet
- Video: No public video

**Readings:** [I Still Prefer MCP Over Skills](https://david.coffee/i-still-prefer-mcp-over-skills) · [AGENTS.md (Factory Docs)](https://docs.factory.com/harness/agents-md) · [Steering Claude Code](https://claude.com/resources/articles/steering-claude-code-skills-hooks-rules-subagents-and-more) · [Writing a Good CLAUDE.md](https://hlyr.dev/blog/writing-a-good-claude-md)

All links: [weeks/week04/links.md](weeks/week04/links.md)

## Week 5 · Agent-Ready Codebases

### 10/20 (Tue) · Agent readiness in your repos (structure, docs, checks)

- Speaker: Mihail Eric
- Textbook: [Chapter 5](book/en/05-agent-ready-codebases.md)
- Notes: [中文](weeks/week05/zh/notes.md) · [English](weeks/week05/en/notes.md)
- Official materials: [Slides](https://docs.google.com/presentation/d/1yCxocmUrGIN7IrC42WB6NW08PtYYFLe1ombDj3Ay6_8/edit)
- Video: No public video

### 10/22 (Thu) · Guest lecture

- Speaker: Eno Reyes (guest)
- Textbook: [Chapter 5](book/en/05-agent-ready-codebases.md)
- Notes: [中文](weeks/week05/zh/notes.md) · [English](weeks/week05/en/notes.md)
- Official materials: not published on the site yet
- Video: No public video

**Readings:** [Making Codebases Agent Ready (video)](https://www.youtube.com/watch?v=ShuJ_CN6zr4) · [Making Ergonomic Repositories](https://x.com/trybasis/status/2056881705269580023)

All links: [weeks/week05/links.md](weeks/week05/links.md)

## Week 6 · Agentic Code Review · Pending

- 10/27 · Agentic code review: best practices and architectures · Mihail Eric · Pending · Textbook ch. 6 (coming)
- 10/29 · Guest lecture · Silas Alberti (guest) · Pending · Textbook ch. 6 (coming)

## Week 7 · Security · Pending

- 11/3 · Security in AI codebases · Mihail Eric · Pending · Textbook ch. 7 (coming)
- 11/5 · Guest lecture · Isaac Evans (guest) · Pending · Textbook ch. 7 (coming)

## Week 8 · Background Agents · Pending

- 11/10 · Background agents: launching tasks asynchronously · Mihail Eric · Pending · Textbook ch. 8 (coming)
- 11/12 · Guest lecture · Rajesh Bhatia (guest) · Pending · Textbook ch. 8 (coming)

## Week 9 · Building an AI-Native Team · Pending

- 11/17 · Guest lecture · Elad Gil (guest) · Pending · Textbook ch. 9 (coming)
- 11/19 · Guest lecture · Amjad Masad (guest) · Pending · Textbook ch. 9 (coming)

## Week 10 · The Software Factory + The Future · Pending

- 12/1 · Coding agents in big teams · Mihail Eric · Pending · Textbook ch. 10 (coming)
- 12/3 · The Software Factory: self-running, self-improving software systems · Mihail Eric · Pending · Textbook ch. 10 (coming)
