# Week 6 · Agentic Code Review

[中文](../zh/notes.md) | **English**

## 官方材料 / Official materials

| 材料 Material | 链接 Link |
|---|---|
| 10/27 课件 Slides | [Google Slides](https://docs.google.com/presentation/d/1u8WYtFj0O9yc4H4JX9D4URYKhDzvrAGKLzn38DXSrak/edit) |
| 10/29 嘉宾 Guest (Silas Alberti, Cognition) | 未发课件 No slides published |
| 文字稿 / 视频 Transcripts / Video | 官网暂未发布 Not published yet |
| 阅读 Readings | [Layered Code Review (X)](https://x.com/addyosmani/status/2114604912520921136) · [Cloudflare: review agents at scale](https://blog.cloudflare.com/ai-code-review) · [Greptile: building a review agent](https://greptile.com/blog/how-to-build-a-code-review-agent) |
| 全部链接 All links | [links.md](../links.md) |

The 10/27 slides are published and summarized below in slide order, in our own words; the 10/29 guest talk and transcripts are not yet published. Chinese version: [../zh/notes.md](../zh/notes.md).

## Lecture 11 · 10/27: Agentic code review — best practices and architectures

### 1. Logistics
- Assignment 5 due Sunday; remaining model credits (Grok, Cognition); Thursday guest Silas Alberti (Chief Research Officer, Cognition); all Thursday lectures now in STLC 111.

### 2. Why review code
- The slides call code review one of the highest-leverage things you can do to grow as an engineer and raise team code quality.
- Two jobs: find and fix bugs; build a shared mental model of the system across the team.
- A summary credited to Blake Smith: keeps the team's picture of the system current, confirms the change solves the problem, opens discussion of design trade-offs, stops bugs before production, keeps style consistent.

### 3. What review catches
Logic and correctness errors; readability and maintainability; performance; security; team best practices (tribal knowledge).

### 4. AI-native review: a maturity ladder
- Problem: code generation got fast, review didn't keep up, so review is the new bottleneck.

| Stage | Approach | Slide verdict |
|---|---|---|
| 0 | Humans review everything | Doesn't scale |
| 1 | A single review agent | Better with an auto-fix loop, still leaves gains on the table |
| 2 | Multi-agent, risk-tiered review with self-improvement | Where many companies are converging; engineering standards kept in a skill knowledge base |

- The slides cite Addy Osmani's post on layered review and Augment Code's Cosmos article (see [links.md](../links.md)).

### 5. Multi-agent review architecture
- One PR fans out to specialist reviewers — security, architecture, code quality, performance — and an aggregate judge merges the verdict.
- The example is Cloudflare's internal engineering stack, with a separate look at its security review agent.

### 6. Designing a review agent (after Greptile)
- **Switch models**: review with a different model than the one that wrote the code (a "model inverter"), so they don't share blind spots.
- **Thoughtful context**: look beyond the diff.
- **Verify**: spin up a dev container and actually exercise the code paths.
- **Cost**: pick models by task — cheap/fast for gathering code context, small/medium with higher reasoning for browser use, frontier for deep bug analysis.
- **Evaluate**: historical PRs with known bugs, and incidents that led to reverts.

### 7. Options
- General: Claude Code, Greptile, CodeRabbit, Devin.
- Security: Vercel deepsec, Wiz, Semgrep.

Textbook chapter: [Chapter 6 Agentic Code Review](../../../book/en/06-agentic-code-review.md).

## This week's topics (official syllabus)
- **Tue 10/27**: agentic code review best practices and architectures.
- **Thu 10/29**: guest Silas Alberti (Chief Research Officer, Cognition).
- Syllabus questions: what AI review catches well and what it misses; review architectures and custom rules; fitting AI review into a team's PR workflow.

## This week's readings
- **Layered Code Review and Risk-Based Human Oversight (X post)**: layer the review and let risk decide how much a human looks at.
- **Coordinating Specialist Review Agents at Scale (Cloudflare)**: a coordinator dispatches specialist reviewers, dedupes and grades findings, posts one review; changes are risk-tiered so small diffs get few agents.
- **Beyond the Diff (Greptile)**: start from a simple review agent and add prompt tuning, model inversion, codebase context, autonomous testing and per-subtask model choice.

> [!NOTE]
> **Supplement**
> Links to earlier weeks: Week 5 argued that only an agent-ready repo can safely rely on automated review; Week 4's AGENTS.md and skills are where a team's review standards live.
>
> Our own takeaways from the readings (unofficial):
>
> | Practice | Why |
> |---|---|
> | Tell the reviewer what *not* to flag | Cuts nitpicks and speculation so engineers keep reading |
> | Tier by diff size and sensitive paths | A typo fix doesn't need the full panel |
> | Grade findings by severity | Only serious issues block a merge |
> | Keep a human override | Hotfixes don't get stuck |
>
> Hands-on:
> - [ ] Read the three readings
> - [ ] Review one of your PRs with models from two different vendors and compare what each finds
