Now let me create the two files:

Here are both files, plus a guide on saving tokens.

---

## How the two files work together

**`copilot-instructions.md`** is your *static* project bible — stack, conventions, what NOT to do, and prompt shortcuts. It rarely changes. Copilot reads it automatically from `.github/copilot-instructions.md`.

**`agent.md`** is your *living session memory* — active context, blockers, decisions, and file index. You rewrite the top section each session. Keep it under ~150 lines by pruning completed work to a "Done" section.

---

## Top strategies to save tokens & context

### 1. Reference files by path, never paste content
Instead of pasting 200 lines of Java into chat, say:
> "Read `src/main/java/.../UserService.java`. What EJB annotations need replacing?"

This is the single biggest saving — a file reference costs ~10 tokens; pasting it costs 600+.

### 2. Keep `agent.md` lean and current
The file is designed to be your "session handshake" — load it at the start, update it at the end. If it grows past 150 lines, prune it. Stale context is worse than no context; it wastes tokens on irrelevant information.

### 3. One task per session
Multi-topic sessions accumulate a huge conversation history. Start a fresh chat for each distinct task (datasource migration, security, test generation). The prompt templates in `agent.md` make this fast.

### 4. Use the prompt shortcuts
The `[DATASOURCE]`, `[REFACTOR]`, `[TEST]` prefixes in `copilot-instructions.md` tell the agent exactly what domain to focus on, cutting down clarification back-and-forth.

### 5. Ask for diffs, not rewrites
> "Show only the changed lines" costs 3× fewer tokens than "rewrite the whole class."

### 6. Update `agent.md` instead of re-explaining
Every session that starts with "So as I mentioned before, we're migrating from JBoss…" is wasted context. That paragraph belongs in `agent.md` once, permanently.

### 7. Archive, don't accumulate
Move completed milestones and resolved blockers to `DECISIONS.md` / `BLOCKERS.md`. The agent never needs to read those unless you specifically ask — they stay out of the context window.
