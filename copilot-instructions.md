# Copilot Instructions — Tomcat Migration Project

## Project Overview
Migrating a BOSS application to Apache Tomcat. Use this file to orient Copilot quickly without re-explaining context each session.

---

## Stack & Scope

| Layer | Technology |
|---|---|
| App Server (target) | Apache Tomcat (specify version, e.g., 10.x) |
| App Server (source) | <!-- e.g., JBoss EAP 7.x / WildFly 26 --> |
| Language | Java <!-- e.g., 17 --> |
| Build Tool | <!-- Maven / Gradle --> |
| Packaging | WAR |
| DB | <!-- e.g., PostgreSQL 15 --> |
| Auth | <!-- e.g., Keycloak / LDAP --> |

> **Update this table at project start.** Copilot uses it to avoid wrong-stack suggestions.

---

## Key Migration Concerns

1. **JBoss-specific APIs to replace** — EJBs, JMS, JNDI lookups, `@Stateless`, `@MessageDriven`
2. **Datasource config** — move from `standalone.xml` / `jboss-web.xml` to `context.xml` + JNDI in `server.xml`
3. **Security** — replace PicketLink / JAAS realm with Tomcat `Realm` or external IdP
4. **Logging** — replace JBoss logging with Log4j2 or SLF4J + Logback
5. **Deployment descriptors** — `jboss-web.xml` → `context.xml`; `jboss-deployment-structure.xml` → removed
6. **Class loading** — Tomcat's flat classloader vs JBoss modular system
7. **Transaction management** — replace Narayana/JTA with Spring TX or manual JDBC

---

## Conventions Copilot Must Follow

- All config files live in `src/main/webapp/META-INF/` or `src/main/resources/`
- No proprietary JBoss annotations — use standard Jakarta EE or Spring equivalents
- Datasource bean names use pattern `jdbc/<ServiceName>DS`
- All JNDI lookups must be abstracted behind a `DataSourceProvider` interface
- Tests use JUnit 5 + Mockito; integration tests use Testcontainers with real Tomcat
- Java package root: `<!-- com.yourorg.boss -->`

---

## What Copilot Should NOT Do

- Do not suggest EJB or `@Stateless` — we are migrating away from these
- Do not use `javax.*` imports — use `jakarta.*` (Jakarta EE 9+)
- Do not suggest WildFly/JBoss-specific Maven plugins
- Do not auto-generate deployment to JBoss/WildFly

---

## File Map (update as project grows)

```
/src
  /main
    /java
      /com/yourorg/boss
        /config        ← Spring/servlet config
        /datasource    ← DataSourceProvider, JNDI wrappers
        /service       ← Business logic (no EJBs)
        /web           ← Servlets / controllers
    /webapp
      /META-INF
        context.xml    ← Tomcat datasource + resource refs
      /WEB-INF
        web.xml        ← Servlet, filter, listener config
/tomcat-config
  server.xml           ← Reference config (not deployed automatically)
  catalina.sh.patch    ← JVM args, memory, GC flags
/migration-notes
  DECISIONS.md         ← Architectural decisions log
  BLOCKERS.md          ← Current blockers
```

---

## Prompt Shortcuts for Copilot Chat

Use these prefixes to get focused answers:

| Prefix | Meaning |
|---|---|
| `[DATASOURCE]` | Question about JNDI / connection pool / context.xml |
| `[SECURITY]` | Auth, realms, session management |
| `[DEPLOY]` | WAR packaging, Tomcat startup, catalina.out errors |
| `[REFACTOR]` | Replacing JBoss API with standard equivalent |
| `[TEST]` | Unit or integration test for migrated component |

Example: `[DATASOURCE] How do I configure a connection pool in context.xml for PostgreSQL?`

---

## Current Sprint Focus
<!-- Update this each sprint to keep Copilot context tight -->
- [ ] Replace all `@Stateless` EJBs in `com.yourorg.boss.service`
- [ ] Migrate datasource config to `context.xml`
- [ ] Validate WAR deploys cleanly to Tomcat 10

---

## References
- [Tomcat 10 Docs](https://tomcat.apache.org/tomcat-10.1-doc/)
- [Jakarta EE Migration Guide](https://jakarta.ee/resources/migration/)
- `migration-notes/DECISIONS.md` — all past architectural decisions
