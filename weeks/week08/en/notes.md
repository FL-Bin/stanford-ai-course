# Week 8 · Background Agents

[中文](../zh/notes.md) | **English**

## 官方材料 / Official materials

| 材料 Material | 链接 Link |
|---|---|
| 课程大纲 Syllabus | [themodernsoftware.dev](https://themodernsoftware.dev) (Week 8: async, cloud-delegated agents; managing fleets of parallel agents; issue-to-PR pipelines and triggers (Slack, Linear, GitHub)) |
| 11/10 Slides | [Google Slides](https://docs.google.com/presentation/d/1R8Pr3RNAFQiw8mHKbXopOhxi_h9zuEeUKrJkxCZ5Fio/edit) |
| 11/12 嘉宾 Guest (Rajesh Bhatia, Cloudflare) | 未发课件 No slides published |
| 文字稿 / 视频 Transcripts / Video | 官网暂未发布 Not published yet |
| 阅读 Readings | [Spotify: From Migration Scripts to Agent Fleets](https://engineering.atspotify.com/2025/11/spotifys-background-coding-agent-part-1) · [Stripe: From Slack Message to Review-Ready PR](https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents) · [Ramp: Giving Agents the Tools to Prove Their Work](https://builders.ramp.com/post/why-we-built-our-background-agent) · [LangChain: open-swe](https://github.com/langchain-ai/open-swe) |
| 全部链接 All links | [links.md](../links.md) |

The 11/10 slides are published; below they are summarized in slide order in our own words, followed by a short summary of each reading. The 11/12 guest lecture has no published materials yet. The full walkthrough is in [Chapter 8](../../../book/en/08-background-agents.md). Chinese version: [../zh/notes.md](../zh/notes.md).

## Lecture 15 · 11/10: Background agents — launching tasks asynchronously

### 1. Logistics
- OSS Contribution #3 due Sunday; Thursday guest Rajesh Bhatia (Senior Director, Cloudflare); all Thursday lectures from now on are in STLC 111.

### 2. Recap: three stages of coding-agent capability

| Stage | Efficiency gain given in the slides |
|---|---|
| Tab complete (2021) | ~15% |
| Synchronous single-task completion (2024) | ~25–35% |
| Background multi-task completion (2026+) | 2x+ |

- The point: stage three is about launching many tasks at once in asynchronous contexts, which buys massive parallelism. Week 6's agentic code review already works this way.

### 3. Why move to the background: the end of localhost
- No more "works on my machine" dependency mess;
- Reproducible, controllable environments;
- Tests run on dedicated instances;
- "Infinitely" parallelizable.

### 4. Rolling your own background agent platform
- Definition: a system that takes a task, spins up a production-like dev environment, runs the whole workflow end to end and returns a pull request.
- The slides call this a trend at many companies, some shipping 1000+ PRs a week fully autonomously.
- Components:
  - An ephemeral, reproducible dev environment;
  - Access to the full codebase, services, build system, docs, code search, logs, metrics, and often production-derived read-only data;
  - Building, linting, testing and pushing handled implicitly by the platform;
  - These are what make massive parallelism possible.
- Coder can serve as the sandbox foundation, Gitpod used to be an option, and LangChain's open-swe is an open-source reference.

### 5. Sandbox providers
Coder, Vercel Sandbox, Daytona, E2B, Modal and others (links in [links.md](../links.md)).

### 6. Architecture of a Slackbot
- One architecture slide shows the flow from a Slack message to a task (diagram not reproduced; see the slides).

### 7. Multi-agent patterns
- **Agent teams:** two examples from the Claude Code docs. Spawn 5 teammates to each investigate one hypothesis, argue against each other, and write the consensus into a findings doc; or spawn three reviewers for security, performance and test coverage.
- **Generator-verifier:** one agent writes, another checks.
- **Primary model with smart friend:** a cheap, fast primary model consults a stronger model when it hits something hard.
- The last two come from an article by Walden Yan of Cognition (see [links.md](../links.md)).

### 8. Meta skills for orchestrating many agents
- Delegation and multi-threading;
- Planning, scoping and architecting;
- Keeping control of and context on tasks;
- Spending time judging a task's complexity before starting;
- Separate planning windows from quick-task windows;
- Reading code and plans, since review is the new bottleneck;
- Growing your agent count step by step rather than all at once.

## Lecture 16 · 11/12: Guest Rajesh Bhatia (Senior Director, Cloudflare)

Materials and recording not yet published. In his LinkedIn preview the speaker said the talk covers what your coding agent does after you close your laptop: where it runs, who holds the keys, what it costs while it waits, and how it tells you something has gone wrong, plus Cloudflare's architecture and seven principles that held up once real people used it (the seven are not public yet). He said he would share the slides afterwards; we will add them once available. Related public talk: [Cloudflare's AI Engineering Stack: Assisted to Delegated](https://www.youtube.com/watch?v=MbLdrAZFQRs) (Ona, 2026-05-06).

## Key points from the readings

### Spotify: From migration scripts to agent fleets (Honk, part 1)
- Spotify's Fleet Management applies code-modifying code to thousands of components and opens PRs automatically; since mid-2024 about half of Spotify's PRs come from it.
- Complex transformations are hard to write: the Maven dependency updater grew past 20,000 lines handling corner cases. So they swapped the transformation script for a prompt to an agent and kept the surrounding infrastructure (targeting repos, opening PRs, review, merge) unchanged.
- More than 1,500 agent-generated PRs have been merged, with 60–90% time savings on migrations versus writing by hand.
- The same agent was later exposed via MCP to Slack and GitHub for ad hoc tasks.

### Stripe: From Slack message to review-ready PR (Minions)
- Over a thousand merged PRs a week are entirely minion-produced; humans review but write no code.
- A typical run starts with a Slack message and ends with a PR that passes CI and is ready for review, with no interaction in between.
- Runs happen on pre-warmed devboxes that start in about 10 seconds and are isolated from production and the internet, so no per-action human permission checks are needed.
- Agent loops are interleaved with deterministic code so required steps like linters and git operations always run; CI runs at most twice.

### Ramp: Giving agents the tools to prove their work (Inspect)
- Each session runs in a Modal sandbox VM with everything an engineer has locally; repo images are rebuilt every 30 minutes and sessions start from snapshots.
- Backend changes can run tests and check telemetry and feature flags; frontend changes come with screenshots and live previews.
- Entry points include Slack, web, a Chrome extension, PR comments and a web VS Code, and sessions are multiplayer.
- At the time of the post about 30% of merged PRs in Ramp's frontend and backend repos were written by Inspect.

### LangChain: An open-source software factory (open-swe, now named Robin)
- Built on Deep Agents and LangGraph: investigate the codebase, implement in an isolated sandbox, validate, deliver a PR, then keep handling review, CI and feedback.
- Entry points: a dashboard, GitHub issues and PR conversations, Slack, Linear.
- The README warns that sandboxes have powerful tools: use least-privilege credentials and restrict repositories and integrations.

> [!NOTE]
> **Supplement**
> Read the four together: Spotify explains why to move from scripts to agents, Stripe how to plug agents into existing engineering infrastructure, Ramp how to make environments fast enough that nobody rations them, and open-swe is a reference whose code you can read. Afterwards, try filling in Chapter 8's five questions (where it runs, where tasks come from, what it can access, how it proves its work, who it hands off to) for each company.
