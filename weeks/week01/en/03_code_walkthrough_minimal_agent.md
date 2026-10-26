# Code walkthrough · claude_code_200lines.py

## 官方材料 / Official materials
| Material | Link |
|---|---|
| Sample code | [Google Drive](https://drive.google.com/file/d/1DxKa_autBOu9s8DvItodgUAwH_pBg7aR/view?usp=drive_link) |
| Slides (9/22) | [Google Slides](https://docs.google.com/presentation/d/1uztIhjHAG6O_9QOD1N_3wdhwhABml1fANXEN2dGwdbg/edit?usp=drive_link) |
| Video | [YouTube](https://youtube.com/watch?v=s7ZzkdvCMDY) |


The sample code has no open license, so it is not reproduced here; this walks through its structure.

## Structure
- `SYSTEM_PROMPT` — a template with a `{tool_list_str}` slot.
- Three tools — `read_file_tool`, `list_files_tool`, `edit_file_tool`.
- `TOOL_REGISTRY` — tool descriptions generated from each function's name, docstring and signature.
- `extract_tool_invocations` — parses lines of the form `tool: name({json})`.
- `run_coding_agent_loop` — the agent loop.

Runs on Python 3.12+ with `openai` and `python-dotenv`, using the Responses API.

## Walkthrough
1. **System prompt:** tells the model it is a coding assistant, lists the tools, and asks for a single `tool: ...` line when it wants one. No native function calling — a text convention parsed by the program.
2. **Tools:** paths are resolved to absolute; `edit_file_tool` creates a file when `old_str` is empty, reports `old_str not found` back to the model instead of crashing, and otherwise replaces the first match.
3. **Tool descriptions:** built automatically, matching the 9/24 point that names, docstrings and signatures become prompt text.
4. **Parsing:** scan for `tool:` lines, split off the name, decode the JSON, skip malformed lines.
5. **Loop:** append user input; call the model; if no tool calls, print and wait; otherwise run each tool, append `tool_result(...)` as a user message, and call the model again.

> [!NOTE]
> **Supplement**
> - Tool calling here is plainly a text protocol, and `edit_file_tool` mirrors Claude Code's exact-string `Edit` tool.
> - The conversation only grows, which is why compaction matters later.
> - Exercises: add a whitelisted `run_bash` tool; switch to native tool calling and compare reliability.
