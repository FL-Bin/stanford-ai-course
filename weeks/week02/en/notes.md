# Week 2 · Advanced Context Engineering

## 官方材料 / Official materials

| 材料 Material | 链接 Link |
|---|---|
| 9/29 课件 Slides | [Google Slides](https://docs.google.com/presentation/d/17brqoQQZHF3K82WgYaV6urAV3Q7iIwyGUBYRvSuY8QY/edit?usp=sharing) |
| 9/29 文字稿 Transcript | [themodernsoftware.dev](https://themodernsoftware.dev/materials/9-29-26-transcript.txt) |
| 10/1 课件 Slides | [Google Slides](https://docs.google.com/presentation/d/1q2cB1a7P4XsR0UJqE0RmtZFeggNOLdPaSnOpbBVewHA/edit?usp=sharing) |
| 10/1 文字稿 Transcript | [themodernsoftware.dev](https://themodernsoftware.dev/materials/10-1-26-transcript.txt) |
| 10/1 Skills 文件夹 Skills folder | [Google Drive](https://drive.google.com/drive/folders/1aEHCXzZKkokuA4AYjD_2i6OrcM5iQosW?usp=drive_link) |
| 课堂视频 Video | 官网暂未发布 Not published yet |
| 阅读 Readings | [The Context Tax](https://langwatch.ai/blog/context-tax-when-to-compact) · [OpenSpec](https://openspec.dev) · [Superpowers](https://github.com/obra/superpowers) · [Enterprise MCP](https://blog.cloudflare.com/enterprise-mcp) |
| 全部链接 All links | [links.md](../links.md) |

Notes follow the slide order, in our own words; extra detail comes from the official transcripts. Quotes are short and sourced; blue Supplement boxes are our own additions. Chinese version: [../zh/notes.md](../zh/notes.md).

---

## Lecture 3 · 9/29: Advanced Prompting and Context Engineering for Complex Codebases

### 1. Logistics
Factory workshop Thursday 6:20–6:45 pm. The OSS partners program is announced: Anyscale (Ray), Arize AI (Phoenix), Browserbase, cmux, CopilotKit, CrewAI, HeyGen, Marimo, OpenHands, Pi, Unsloth AI, Vercel, Warp, Zilliz.

### 2. Objective
Go from ad-hoc prompting to a dependable synchronous AI development workflow, and use AI to get up to speed on unfamiliar codebases and work through complex tasks systematically.

### 3. Lesson plan
Onboarding to large codebases; spec-driven engineering with **RePPIT** (Research, Propose, Plan, Implement, Test); a look at other spec-driven frameworks.

### 4. Vibe coding confuses expectations
The tab-accept-everything style of vibe coding is not what this lecture is about. Prompt on the slide: how would you build a Mint clone? Extending such an app at production scale calls for a methodical approach.

### 5. Production AI code needs method

> "You should have an active, functional mental model of how you would build your solution"
> 你应该对自己会怎么搭建这个方案，有一个活跃的、能运转的心智模型。
> —— Lecture 3 slides

Principles: understand the codebase → propose a few solutions → plan the best one → implement → test. Bad code today is either an architectural mistake or functionally wrong output from a hallucinating model.

### 6. Use RePPIT
- **Research:** the agent distills the codebase into a structured research doc instead of loading raw code.
- **Propose:** about two options with trade-offs (more than two gives diminishing returns, per the instructor).
- **Plan:** files to change, testing, observability, explicit out-of-scope items.
- **Implement:** the simplest prompt of the five.
- **Test:** unit, integration, smoke tests, plus an optional review skill.

The slide says to iterate on this until it fits you. In class, the research doc serves both as seed context for the agent and as the instructor's own mental model.

### 7. Demo
Feature: a trend line of spending by category over time. The instructor chose a frontend-only option.

### 8. Best practices
Only the first ½–¾ of the context window holds "smart" tokens; system prompt, AGENTS.md/CLAUDE.md and task context fill it before the "dumb zone". Review specs carefully; split very large features into task lists; after each item, write the agent's work into an artifact that becomes context for the next. From the transcript: reuse well-maintained docs and drop stale ones; use the strongest model for research/propose/plan; clear or compact rejected options (a cited study puts the sweet spot around 250k–450k tokens, model-dependent).

### 9. Task delegation taxonomy
Simple prompting · make a plan · research then plan · (research then plan) × N. The slide asks when to use each.

> [!NOTE]
> **Supplement**
> A practical rule of thumb: match the level to the size of the change.

### 10. Other popular frameworks
**Superpowers:** an opinionated, guided end-to-end workflow; TDD-based; skills for spec/plan, implementation and testing; built-in parallelism. **OpenSpec:** a lightweight flow that tracks changes against source-of-truth specs and merges them after the diff.

### 11. Spec management
Specs live in Linear or locally in Git (OpenSpec's approach); design trade-offs can go in `.notes/`.

---

## Lecture 4 · 10/1: MCP, Tool-calling, and Beyond

### 1. Logistics
OSS partner assignments out tonight; AI slop gets a 0; project proposals due tonight; workshop by Ashley Jepson (Factory).

### 2. Why
Model knowledge is vast but frozen at training time; autonomous systems need a reliable way to bring in live data.

### 3. MCP
An open protocol for supplying context to models in a way that generalizes across integrations.

> "In English: standard format for exposing tools to LLMs"
> 说白了：向大模型暴露工具的标准格式。
> —— Lecture 4 slides

### 4. Basics
Replaces M × N custom connectors with M + N; no need to rebuild auth, error handling or rate limiting; consistent output via JSON-RPC.

### 5. A bit deeper
Host (Cursor, Claude Desktop) · client (library in the host, one stateful session per server) · server (thin wrapper around a tool) · tool (callable function). Flow: `tools/list` → server returns name, summary, JSON schema → host injects it into context → model emits a structured call → server executes and the conversation resumes. Transports: stdio and streamable HTTP. Slide example: "Summarize my emails from Jack".

### 6. Designing a good server, option 1
Not a REST wrapper — that leads to many tiny tools, bloated context and agents busy orchestrating (endpoints were designed for humans, as the instructor put it). Design for outcomes (`send_payment(user_email)` rather than a three-call chain); explicit arguments, no nested dicts; docstrings and errors are prompts; service-prefixed names.

### 7. Option 2
With many servers, expose just `search` and `execute`: search finds tool definitions, execute generates deterministic code. Context shrinks regardless of server count — over 90% fewer tokens. Example: find a Jira ticket and update it from Google Drive.

### 8. Advanced architecture
Cloudflare's MCP server portal: one connection reveals every server an employee may use, with central logging, policy enforcement and DLP guardrails.

### 9. Agent Skills
A standard for on-demand, domain-specific capabilities combining code and prompts (docs, slides, data analysis). Spec at <https://agentskills.io/home>; demo with a skills.md and Matt Pocock's skills repo.

### 10. APIs vs MCP vs Skills
APIs: interfaces developers call, handling auth/retries/pagination themselves. MCP: standardized tool definitions invoked by the agent runtime; the main way to reach external resources. Skills: reusable procedures that teach an agent a job, often orchestrating several tools — "the repeatable way to do X".

---

## Readings
The Context Tax (when to compact); OpenSpec and Superpowers; Enterprise MCP (Cloudflare).

> [!NOTE]
> **Supplement**
> Exercises: add a small feature with RePPIT and keep the three docs; build an MCP server with 2–3 outcome-oriented tools; try Superpowers or OpenSpec and compare with RePPIT.
