# agent.md — BOSS Tomcat Migration

> **Purpose:** Compact project memory for AI agents (Copilot, Claude, Cursor, etc.).
> Keep this file ≤ 150 lines. Prune completed items. Never paste full code here — use file paths.

---

## Identity

- **Project:** BOSS Application → Apache Tomcat Migration
- **Status:** 🟡 In Progress
- **Owner:** <!-- Team / engineer name -->
- **Last updated:** <!-- YYYY-MM-DD -->

---

## Active Context

### What we are doing right now
<!-- One or two sentences max. Rewrite each session. -->
Migrating JBoss-specific service layer (EJBs) to plain Spring-managed beans. Datasource migration is next.

### Decisions made this session
<!-- Append, then prune when > 5 items. Full log lives in DECISIONS.md -->
1. Use `HikariCP` as the connection pool (not DBCP2) — faster startup
2. `DataSourceProvider` interface kept for testability

### Blockers
<!-- Remove when resolved. Full history in BLOCKERS.md -->
- [ ] `jboss-web.xml` root-context mapping has no direct Tomcat equivalent — needs web.xml filter

---

## Architecture Snapshot

```
[Browser]
    │
    ▼
[Tomcat 10 — WAR]
    ├── web.xml (Servlets, Filters, Listeners)
    ├── context.xml (JNDI DataSource, HikariCP)
    └── Spring Context
          ├── Service Layer (was EJBs)
          ├── DataSourceProvider → HikariCP → PostgreSQL
          └── Security Filter (was PicketLink)
```

---

## File Index
> Point the agent here instead of pasting file contents.

| Purpose | Path |
|---|---|
| Datasource config | `src/main/webapp/META-INF/context.xml` |
| Servlet/filter config | `src/main/webapp/WEB-INF/web.xml` |
| Spring beans | `src/main/resources/applicationContext.xml` |
| Tomcat server ref config | `tomcat-config/server.xml` |
| JVM / startup flags | `tomcat-config/catalina.sh.patch` |
| Decision log | `migration-notes/DECISIONS.md` |
| Blocker log | `migration-notes/BLOCKERS.md` |
| Main service package | `src/main/java/com/yourorg/boss/service/` |
| Datasource abstraction | `src/main/java/com/yourorg/boss/datasource/` |

---

## Completed Milestones
<!-- Move here when done — keeps active context lean -->
- [x] Audit of all JBoss-specific imports complete
- [x] `javax.*` → `jakarta.*` rename applied project-wide

---

## Agent Behaviour Rules

1. **Read files by path** — never ask agent to paste file contents into chat
2. **Minimal diffs** — suggest smallest change that solves the problem
3. **No regressions** — run `mvn test` mentally before proposing changes to shared utilities
4. **Prefer standard APIs** — Jakarta EE / Spring over any vendor-specific API
5. **Log decisions** — any non-obvious choice must go into `DECISIONS.md`, not just code comments
6. **Token discipline** — if the agent needs context, cite the file path; do not summarise entire files

---

## Prompt Templates
Copy-paste these to start focused agent sessions.

### Start of session
```
Read agent.md. Current task: [describe task].
Relevant files: [list 1-3 paths from File Index above].
Do not read other files unless asked.
```

### Code review
```
Review [file path] for JBoss-specific patterns.
Flag: proprietary annotations, javax.* imports, JNDI patterns that won't work in Tomcat.
Output: bullet list of issues + suggested standard replacement. No full rewrites.
```

### Datasource migration
```
Given context.xml at [path] and existing JNDI lookup in [path],
generate the minimal Tomcat-compatible JNDI datasource config using HikariCP.
Output only the changed XML blocks.
```

### Test generation
```
Generate a JUnit 5 integration test for [ClassName] using Testcontainers (Tomcat image).
Mock only external HTTP calls. Use real DB via Testcontainers PostgreSQL.
```

---

## Token Budget Tracker
> Use this to stay within context limits per session.

| Item | Approx tokens |
|---|---|
| This file (agent.md) | ~500 |
| copilot-instructions.md | ~600 |
| One Java service file (~200 lines) | ~600 |
| context.xml | ~100 |
| web.xml (typical) | ~300 |
| **Safe session budget** | **~4 000 remaining** |

**Rule:** Load only the files you need. Close the session when done; re-open fresh for the next task.
