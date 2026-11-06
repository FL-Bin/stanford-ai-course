# Week 7 · Security

[中文](../zh/notes.md) | **English**

## 官方材料 / Official materials

| 材料 Material | 链接 Link |
|---|---|
| 课程大纲 Syllabus | [themodernsoftware.dev](https://themodernsoftware.dev) (Week 7: SAST / SCA, dependency and secret leaks; prompt injection and agent attack surfaces; agent-assisted triage and remediation) |
| 11/3 Tue | 校假停课 No class – University holiday |
| 11/5 嘉宾 Guest (Isaac Evans, Semgrep) | 未发课件 No slides published |
| 文字稿 / 视频 Transcripts / Video | 官网暂未发布 Not published yet |
| 阅读 Readings | None listed this week; supplementary reading in [links.md](../links.md) |
| 全部链接 All links | [links.md](../links.md) |

This week had a single guest lecture and the site published no slides or readings. Below are key points organized by the three syllabus topics; the full walkthrough is in [Chapter 7](../../../book/en/07-security-in-ai-codebases.md). Chinese version: [../zh/notes.md](../zh/notes.md).

## Lecture 13 · 11/3: no class

Stanford university holiday.

## Lecture 14 · 11/5: Guest Isaac Evans (CEO, Semgrep)

Materials and recording not yet published; will be added once available. Related public talk: [When AI Writes Code: Rethinking App Security](https://www.youtube.com/watch?v=TKJGul9TRws) (Lightspeed, 2025-11-19).

## Key points by topic

> [!NOTE]
> **Supplement**
> The points below are our own summary of the syllabus topics, not lecture content.

### 1. SAST / SCA, dependencies and secret leaks

- SAST checks your own code; its core is taint tracking from user input (source) to a dangerous sink without sanitization.
- SCA checks third-party dependencies. Agents install packages casually; versions may be stale and names may not exist or be squatted.
- Secret scanning pays off most in a pre-commit hook; once pushed, a secret must be revoked and reissued.

### 2. Prompt injection and agent-specific attack surfaces

- An LLM may treat any text it reads as instructions; web pages, issues and READMEs can all carry injections.
- The "lethal trifecta": private data + untrusted content + external communication. All three together is the danger zone; break at least one.
- MCP servers and skills are attack surface too; install only trusted ones.

### 3. Agent-assisted triage and remediation

- In Semgrep's tests, Claude Code and Codex hit roughly 14% and 18% true-positive rates, and three runs of the same prompt gave different results.
- A sturdier split: rule tools for deterministic coverage, agents to drop false positives and write fixes, humans for the final call.
