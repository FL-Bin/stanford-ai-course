# Code walkthrough · a ~200-line coding agent
> We explain the instructor's sample script in our own words; the code itself is not copied here. Get it from the official link in [links.md](../links.md).
> Runs on Python 3.12+ with `openai` and `python-dotenv`; the sample uses the OpenAI Responses API and a model name you may need to swap for one you have.

## Five building blocks
| Block | Role |
|---|---|
| System prompt template | Has a placeholder that gets filled with auto-generated tool descriptions |
| Three tool functions | read a file / list a directory / edit a file |
| Tool registry + description builder | Builds the tool text the model sees from each function's name, docstring and signature |
| Tool-call parser | Finds lines like `tool: NAME({json})` in the model's reply |
| Agent loop | input → model → run tools and feed results back → repeat until no tool call |

## 1. The system prompt (paraphrased)
It tells the model it is a coding assistant, lists the tools, and asks it to reply with **exactly one line** `tool: NAME({JSON})` when it wants a tool, then continue after it receives `tool_result(...)`; otherwise answer normally.
Key point: it does **not** use native function calling — tool calling here is just a **text protocol** the program parses. That makes the mechanics very visible.

## 2. The tools
- Paths are resolved to absolute paths (supports `~`).
- Read returns path + content; list marks each entry as file or dir.
- Edit takes `path, old_str, new_str`: empty `old_str` creates/overwrites the file; a missing `old_str` returns an error message **to the model** instead of crashing; otherwise it replaces only the **first** match. This is the seed of Claude Code's exact-string-replace Edit tool.

## 3. Auto-generated tool descriptions
Name + docstring + `inspect.signature` become the tool text. Lesson from lecture 2: **docstrings, parameter types and names are prompt text** — write them clearly.

## 4. Parsing
Scan lines starting with `tool:`, split off the name, decode the JSON; skip malformed lines.

## 5. The loop
```
conversation = [system prompt]
outer: read user input → append
  inner: reply = model(conversation); calls = parse(reply)
         no calls → print, append, break
         calls → run each, append "tool_result(...)" as a user message, call model again
```
- The conversation only grows — that is why context fills up and why compaction exists later.
- Tool results go back in the user role, matching what the lecture's traffic capture showed for Claude Code.

## Exercises
- [ ] Run it and ask it to create and explain `hello.py`
- [ ] Add a `run_bash` tool with an allow-list (`ls`, `python` …)
- [ ] Switch to native tool calling and compare reliability
