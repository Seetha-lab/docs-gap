# Feedback for the AI team

Docs Gap is the app we drive. The point is to hit every surface and write what broke / what was unclear in `#hackathon-product-feedback`.

Do not skip a box to “finish the demo.”

## Surfaces they asked us to try

| Surface | What we will do | Status | Note |
|---|---|---|---|
| CLI (beta) | `getstream agents init`, sync this folder, `--version` is date+hash | blocked | Installed CLI is `1.1.0`. No `agents`, no `docs`. Beta install not run yet. |
| Dashboard UI | Create/open the agent, watch a session, connect GitHub/Linear/Slack | not started | Need beta + login |
| Conversation loop | Ask → verify docs → check code → confirm → PR. Interrupt mid-loop. | designed only | In `instructions.md`, not run on the router |
| Nested skills | `chat/` + `reference/empty-text.md`; hand off `verify-docs` → `check-code` → `open-pr` | designed only | Watch for `[handed to …]` / `delegated` |
| Connectors | GitHub company, Linear company, Slack (user) | not started | Catalog MCP. Need dashboard label `company` |
| MCP (`mcp_servers`) | Add a real extra MCP URL when we have one | skipped | No fake URL. Need a docs MCP or any public server they want us to hit |
| Naming | Suggest a name instead of Accelerate | open | Docs Gap / Steward / Keeper |

## Already found (paste-ready)

**CLI:** Current `getstream` `1.1.0` has no `agents` or `docs`. Hackathon skill says beta looks like `2026-10-13-eab135f`. Easy to miss — you think you have the CLI and you cannot sync an agent.

**Docs site:** Passworded Vercel docs (`/agents/docs/`) returned 401 from here. Agent skill says use `getstream docs`, which this CLI does not have.

**Connectors vs MCP:** Catalog connectors are MCP. `mcp_servers` is “a URL the router has never heard of.” Easy to confuse. We left `mcp_servers` empty on purpose (no invented URL).

## Run order (do not skip)

1. Install beta CLI. Confirm version is date+hash.
2. `getstream init` on a Seetha app only.
3. Sync `docs-gap/` (`getstream agents init` or whatever beta prints).
4. Dashboard: open the agent. Connect GitHub + Linear. Label `company`.
5. One chat: `When will a message have text: "" ?` — see if it asks, then uses `chat` → `verify-docs` → `check-code`, then waits.
6. Say no to the PR. See if it stops.
7. Say yes. See if GitHub PR or Linear works. Note the exact error.
8. Slack: does the “gap found” message post?
9. Break it: wrong docs URL, customer app id, empty question, two skills at once.
10. Write what happened below and in Slack.

## Log (add a line every time something is weird)

| When | Surface | What I did | What happened | Wanted |
|---|---|---|---|---|
| 2026-10-16 | CLI | `getstream agents -h` | unknown command on `1.1.0` | `agents` on beta |
| 2026-10-16 | GitHub | `gh repo create` + push | Worked as Seetha-lab. Repo: https://github.com/Seetha-lab/docs-gap | — |
| | Dashboard | connect GitHub/Linear | not started | need beta CLI |
| | | | | |

## Naming dump (they asked)

Docs Gap, Steward, Keeper, Helios, Loom.
