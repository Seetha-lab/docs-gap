# Docs Gap

**Official name:** Docs Gap  
**Platform:** Stream Sovereign AI (Agents)

A text agent that finds a hole (or wrong line) in official Stream docs, proves it from the docs page and from code, then opens a **GitHub PR** (or Linear) — only after a human says yes.

It is not a Zendesk writer. It does not query customer apps. It does not invent SKUs, feature flags, or docs URLs.

---

## What it does

| Step | What happens |
|---|---|
| 1. Ask | You paste a customer question, ticket dump, or a docs URL you think is wrong |
| 2. Product skill | Chat / Video / Feeds / Moderation playbook |
| 3. `verify-docs` | Official getstream.io pages only |
| 4. `check-code` | Code wins when docs and code disagree |
| 5. Confirm | Shows gap, URL, code behaviour, proposed patch — waits for **yes** |
| 6. `open-pr` | GitHub PR preferred; Linear if no writable docs repo; optional Slack note |

Conversation loop: `instructions.md`  
Guardrail: `guardrail.md`  
Agent config: `agent.yaml`

---

## Repo layout

```
docs-gap/
├── agent.yaml              # name, llm, connectors
├── instructions.md         # conversation loop
├── guardrail.md            # what it refuses
├── skills/
│   ├── chat|video|feeds|moderation/
│   ├── verify-docs/
│   ├── check-code/
│   └── open-pr/
├── knowledge/              # verified gap notes
├── proposed/               # ready-to-paste docs patches
├── visualisations/         # team walkthrough (HTML)
└── FEEDBACK.md             # hackathon surface log for the AI team
```

---

## Verified gaps (examples)

1. **When can Chat `text` be `""`?**  
   Patch: `proposed/chat-send-message-empty-text.md`

2. **`removeMembers` of a deleted user → 400 / code 4**  
   Patch: `proposed/chat-update-channel-deleted-user.md`  
   Do not name the customer in a public docs PR.

Team walkthrough: open `visualisations/docs-gap.html` in a browser.

---

## Publish / run (clear path)

### 0. Prerequisites

- A Stream app you own (dev/test — never a customer app)
- Beta `getstream` CLI (stable `1.1.0` has **no** `agents` command)
- Dashboard access to Library → Agents / Connectors

### 1. Install the beta CLI

```bash
curl -fsSL https://getstream.io/cli/beta/install.sh | bash
getstream --version
# Expect a date+hash build, e.g. 2026-10-28-02dc1ca — not 1.1.0
```

If an older beta points at a dead host, run `getstream update`.

### 2. Clone and connect your app

```bash
git clone https://github.com/Seetha-lab/docs-gap.git
cd docs-gap
getstream init          # paste YOUR app key + secret when prompted
getstream agents init   # follow the prompt if it asks for an agent id
```

Keys stay local under `.stream/` (gitignored). Never commit them. Never put keys in this README.

### 3. Connectors (Dashboard)

Dashboard → **Library → Connectors**:

| Connector | Label | Required? |
|---|---|---|
| GitHub | `company` | Yes (PRs) |
| Linear | optional | Fallback when no docs repo |
| Slack | optional | Notify `#hackathon-product-feedback` |

`agent.yaml` expects GitHub with `connection: company`. Until that OAuth completes, sync/session may fail — see `FEEDBACK.md`.

### 4. Sync the agent

From this folder (exact subcommand may match your CLI help):

```bash
getstream agents sync .
# or: getstream agents init .
```

Confirm the agent appears in the Dashboard as **docs-gap** / **Docs Gap**.

### 5. First chat (smoke test)

Paste:

```
When will a message have text: "" ?
```

Expect: product skill → verify-docs → check-code → a proposed patch → **it waits**.  
Say **no** once (must stop). Say **yes** only when you want a PR/Linear issue.

---

## Rules (non-negotiable)

- Official getstream.io docs only for “what the docs say”
- Code check when the gap needs proof
- No customer app queries
- No PR / Linear without an explicit yes
- Bugs and naming feedback → `#hackathon-product-feedback`

---

## Sovereign AI surfaces this hits

| Surface | Where |
|---|---|
| Conversation loop | `instructions.md` |
| Nested skills | `skills/*/SKILL.md` (+ notes / reference) |
| Connectors (catalog MCP) | `agent.yaml` → github / linear / slack |
| Extra MCP | only when a real URL exists (none invented) |
| CLI | beta `getstream` init + sync |
| Dashboard | session URL the runner prints |

---

## Feedback

See `FEEDBACK.md` for the AI-team surface checklist and known blockers (CLI beta, GitHub OAuth `redirect_uri`, etc.).
