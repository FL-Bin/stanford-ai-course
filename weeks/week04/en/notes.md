# Week 4 · Customizing Your Agent and Repository

[中文](../zh/notes.md) | **English**

## 官方材料 / Official materials

| 材料 Material | 链接 Link |
|---|---|
| 10/13 课件 Slides | [Google Slides](https://docs.google.com/presentation/d/152VaUifBKH4T6hxd6fCKKM9kJTSAuBmkF8zSYwuTYAo/edit?usp=sharing) |
| 10/15 嘉宾 Guest (Boris Cherny) | 未发课件 No slides published |
| 文字稿 / 视频 Transcripts / Video | 官网暂未发布 Not published yet |
| 课上示例 Example | [Next.js AGENTS.md](https://github.com/vercel/next.js/blob/canary/AGENTS.md) |
| 阅读 Readings | [I Still Prefer MCP Over Skills](https://david.coffee/i-still-prefer-mcp-over-skills) · [AGENTS.md (Factory)](https://docs.factory.com/harness/agents-md) · [Steering Claude Code](https://claude.com/resources/articles/steering-claude-code-skills-hooks-rules-subagents-and-more) · [Writing a Good CLAUDE.md](https://hlyr.dev/blog/writing-a-good-claude-md) |
| 全部链接 All links | [links.md](../links.md) |

No transcripts were published; notes follow the public slides. The 10/15 guest lecture has no public slides yet. Chinese version: [../zh/notes.md](../zh/notes.md).

---

## Lecture 7 · 10/13: Customizing Your Agent Setup

### 1. Logistics
Project tech spec due Thursday; first OSS contribution due Sunday; Boris Cherny guest lecture; Thursday lectures move to STLC 111.

### 2. APIs vs MCP vs Skills (recap)
See [week 2](../../week02/en/notes.md).

### 3. Additional MCP perks
Seamless auth, easy versioning and updates, portability across clients, native sandboxing for remote MCP.

### 4. Why customize
Peak productivity with coding agents means owning your stack, and there are many levers.

### 5. Techniques
Agent behavior files (CLAUDE.md / AGENTS.md), hooks, skills, subagents — with real examples.

### 6. Designing an optimal AGENTS.md

> "README for agent"
> 写给代理看的 README。
> —— Lecture 7 slides

Sections: project overview (a map), build and test commands, code style, testing, security, stack-specific gotchas. Keep instructions broadly applicable, skip code snippets (they go stale), stay under ~300 lines, and in big repos use nested files with the root AGENTS.md as a router. Example: Next.js's AGENTS.md. CLAUDE.md loads from the root down to the nearest file, so the most specific instructions come last.

### 7. Hooks
Deterministic scripts on events such as `PreToolUse`, `PostToolUse`, `UserPromptSubmit`, `PreCompact`: sanitize prompts, block sensitive actions, run linters/formatters, run tests at the end. Supported in Claude Code and Cursor.

### 8. Skills
Frequently used prompts as files: run tests, plan, research, review, verify. Examples: Claude Code "ship-it", Cursor "deslop".

### 9. Subagents
Runtime delegation with separate contexts; only the final message returns; name, description and tools load at session start; implicit or explicit invocation. Good for exploring code, simplifying after a change, end-to-end testing — side tasks. CLAUDE.md, by contrast, anchors behavior.

### 10. MCP server use cases
Jira/Linear (issues), Notion/Confluence (issues from specs), Datadog/Sentry (production debugging), Redshift (data issues), Context7 (current library docs, fewer hallucinations), Arize (suggest new experiments from test runs).

### 11. The context story
System prompt → Memory.md → environment → MCP tools → skills → global AGENTS.md → local AGENTS.md.

> [!NOTE]
> **Supplement**
> Every layer spends context budget; compare week 2's ½–¾ smart-token rule.

---

## Lecture 8 · 10/15: Guest Boris Cherny (Anthropic, Claude Code)
No slides or transcript published yet.

---

## Readings
I Still Prefer MCP Over Skills; AGENTS.md (Factory); Steering Claude Code; Writing a Good CLAUDE.md.

> [!NOTE]
> **Supplement**
> Exercises: rewrite your AGENTS.md in the six-section shape under 300 lines; add a `PostToolUse` formatter/test hook; try a plan/implement/review subagent split.
