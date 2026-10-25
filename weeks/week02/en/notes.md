# Week 2 · Advanced Context Engineering
> Our own study notes (paraphrase + commentary), not the slides or transcripts. Official materials: [links.md](../links.md). Chinese version: [../zh/notes.md](../zh/notes.md).

---
## Lecture 3 · 9/29: Advanced prompting and context engineering for complex codebases
### Goals
- Move from ad-hoc prompting to a **reliable synchronous AI development workflow**.
- Use AI to onboard quickly to unfamiliar codebases and finish complex tasks systematically.

### Why vibe coding is not enough
- **Vibe coding** — accepting AI code without much thought — is fun for toys but breaks down in production codebases with thousands of files.
- At scale you hit **context-window limits**; even million-token windows don't make every token equally "smart".
- The instructor's view: production AI code needs a method, and you need a **working mental model** of how the solution will be built.
- "Bad code" today means both wrong architecture decisions and functionally wrong code from hallucinations.

### The RePPIT framework
| Letter | Phase | What happens (our reading) | Artifact |
|---|---|---|---|
| R | Research | The agent distills the codebase into a structured research doc — modules, organization, where key code lives — **without dumping raw code into context** | Research doc |
| P | Propose | ~2 options with trade-offs, grounded in the research (more than 2 has diminishing returns, per the instructor) | Proposals |
| P | Plan | Detailed plan for the chosen option: files to change (like a diff preview), tests, observability, and **explicitly out-of-scope items** | Plan doc |
| I | Implement | The agent implements the plan; this prompt is the simplest | Code |
| T | Test | Unit, integration and smoke tests; optionally a review skill that checks architecture, style, consistency | Test/review report |

Demo: adding a "spending by category over time" trend line to a Mint-like budgeting app, step by step; the instructor picked the lighter frontend-only option.

### Practical advice (paraphrased)
- **Context budget**: only roughly the first ½–¾ of the window is "smart"; past that is the joking "dumb zone". System prompt and AGENTS.md/CLAUDE.md already use some of it.
- **Review specs carefully**; split big features into task lists; after each item, write up what the agent did as context for the next.
- Existing docs: reuse if well maintained; stale docs are worse than none.
- **Model choice**: strongest model for research/propose/plan, lighter models are fine for implement/test.
- Unused proposals still occupy context — clear or compact. A cited compaction study suggests compacting somewhere around 250k–450k tokens depending on the model.
- RePPIT is a starting point; adapt it to your domain.

### Task delegation taxonomy
1. Simple prompting — small changes
2. Make a plan, then implement
3. Research, then plan
4. (Research then plan) × N — large features

### Other spec-driven frameworks
- **Superpowers**: an opinionated end-to-end, TDD-based workflow; a set of skills for specs/plans, implementation and testing, with built-in parallelism.
- **OpenSpec**: a lighter spec/plan flow that tracks changes separately from the source-of-truth specs and merges them afterwards.
- **Where specs live**: a tool like Linear, or in the repo under Git; design trade-offs can go in `.notes/`.

---
## Lecture 4 · 10/1: MCP, tool calling, and beyond
### Why MCP
- Model knowledge is a **static snapshot** from training; autonomous systems need a robust way to bring in **dynamic data**.

### What MCP is
- **Model Context Protocol**: an open protocol for providing context/tools to models in a generalizable way — in short, **a standard format for exposing tools to LLMs**.
- It turns **M×N** model-to-service connectors into **M+N**, avoids reimplementing auth/error handling/rate limiting, and standardizes output via JSON-RPC.

### Terms and flow
| Term | Meaning |
|---|---|
| Host | The app, e.g. Cursor, Claude Desktop |
| MCP client | Library inside the host; one stateful session per server |
| MCP server | Lightweight wrapper in front of a tool/service |
| Tool | A callable function (data source, API …) |

Flow: client calls `tools/list` → server returns name, description and JSON schema per tool → host injects them into the model's context → the model emits a structured tool call → the server executes and the conversation resumes. Transports: **stdio** and **streamable HTTP**.

### Designing a good MCP server
**Option 1 — not a thin REST wrapper.** One tool per endpoint leads to too many tools, huge contexts, and agents spending their effort on orchestration (tried in 2024–early 2025, worked poorly).
- **Design for outcomes, not operations**: one "pay by email" tool instead of three chained lookups that must all succeed.
- **Explicit arguments**: avoid nested untyped dicts; use type annotations/Pydantic.
- **Instructions are context**: docstrings and error messages are prompts.
- **Name for discovery**: prefix tool names with the service.
- Consolidate as tools multiply, e.g. one `search_resource` with a resource parameter.

**Option 2 — only two tools, `search` and `execute`**, once MCP servers explode. The agent searches for relevant tools/definitions, then generates deterministic code that runs in a sandbox/VM (not in the model). Tools load on demand and data is filtered before reaching the model; the slides cite 90%+ token reduction.

**Advanced: MCP portals** (Cloudflare's enterprise approach): employees connect to one portal that exposes every internal and third-party server they're authorized for, with central logging, policy and DLP. Covered later in the course.

### Agent Skills preview and comparison
- Skills: a standard for dynamically loaded, domain-specific capabilities that combine code and prompts (docs, slides, data analysis …). Next week goes deeper.

| | APIs | MCP | Skills |
|---|---|---|---|
| What | HTTP/REST/GraphQL interfaces for developers | Tool definitions agents invoke in a standard way | Reusable procedures that teach an agent a job, often orchestrating tools |
| Who uses it | You or an SDK | The model/agent runtime | The agent or framework |
| Role | You handle auth, retries, pagination | Main way to reach external resources | Workflow abstraction: "the repeatable way to do X" |

---
## Readings (pointers)
- **The Context Tax: When to Compact** — when to compact and what it costs (cited in lecture).
- **OpenSpec**, **Superpowers** — the two spec-driven frameworks above; try one.
- **Enterprise MCP (Cloudflare)** — centrally deploying and governing MCP.

## Exercises
- [ ] Add a small feature with RePPIT and keep the research, proposal and plan docs
- [ ] Build a tiny MCP server with 2–3 outcome-oriented tools
- [ ] Try Superpowers or OpenSpec and compare with RePPIT

> 💡 **Gaibin's note**: (to be added)
