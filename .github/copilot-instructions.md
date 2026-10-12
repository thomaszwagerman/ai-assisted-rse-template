# Copilot instructions

Follow [AGENTS.md](../AGENTS.md) in the repository root: it is the single source of truth
for commands, conventions, scientific-integrity rules and what to ask before doing.

Copilot-specific notes:

- Scoped rules live in `.github/instructions/*.instructions.md` and apply by file pattern.
- Reusable workflows are prompt files in `.github/prompts/` (type `/` in chat).
  The template ships no skills; optional community skills are described in
  `docs/community-skills.md`.
- Specialised personas are in `.github/agents/` (planner, implementer, reviewer,
  docs-writer).
- When suggesting commands, use `make` targets and `uv run`, never bare `pip` or `python`.
- When you are unsure about a fact, API, or citation, say so instead of guessing.
