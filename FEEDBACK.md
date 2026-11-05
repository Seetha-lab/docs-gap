# Feedback for the AI team

Docs Gap is the app we drive. The point is to hit every surface and write what broke / what was unclear in `#hackathon-product-feedback`.

Do not skip a box to “finish the demo.”

## Surfaces they asked us to try

| Surface | What we will do | Status | Note |
|---|---|---|---|
| CLI (beta) | `getstream agents init`, sync this folder, `--version` is date+hash | unblocked | Updated 2026-10-29: `2026-10-28-02dc1ca`. Old CLI host `accelerate.gcp.stream-io-api.com` was NXDOMAIN. |
| Dashboard UI | Create/open the agent, watch a session, connect GitHub/Linear/Slack | not started | Need beta + login |
| Conversation loop | Ask → verify docs → check code → confirm → PR. Interrupt mid-loop. | designed only | In `instructions.md`, not run on the router |
| Nested skills | `chat/` + `reference/empty-text.md`; hand off `verify-docs` → `check-code` → `open-pr` | designed only | Watch for `[handed to …]` / `delegated` |
| Connectors | GitHub company, Linear company, Slack (user) | GitHub pending | App connection `company` created 2026-10-29 (`github`, oauth2). Status pending until dashboard OAuth. Linear/Slack not created. |
| MCP (`mcp_servers`) | Add a real extra MCP URL when we have one | skipped | No fake URL. Need a docs MCP or any public server they want us to hit |
| Naming | Suggest a name instead of Accelerate | **chosen: Docs Gap** | Agent id `docs-gap`; display name Docs Gap |

## Second verified gap (2026-10-29)

From a group-chat Support ticket, not a synthetic prompt:

GDPR docs say delete is async and `queryUsers` hides the user. They do **not** say `UpdateChannel` / `removeMembers` of a deleted user is **400 / code 4** (`Unable to update a channel with deleted user`), with no `exception_fields`, while group memberships still linger until the `DeleteUsers` task finishes. Empty `queryUsers` is not a deleted signal. 408 is code **48**, not 23.

Patch: `proposed/chat-update-channel-deleted-user.md`. Do not name the customer in a public PR.

Team demo page: `visualisations/docs-gap.html`.

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
| 2026-10-16 | CLI | `getstream agents init` no args | `accepts 1 arg(s), received 0` | Skill says `getstream agents init` |
| 2026-10-16 | Schema | `sync .` | `unexpected key tools` (we copied `tools.progressive` from Vision-Agents accelerate example) | CLI keys: name, description, mode, llm, connectors, … no top-level `tools` |
| 2026-10-16 | Skills | template README | "one markdown file per skill" — nested `skills/foo/SKILL.md` is what the hackathon asked to test | confirm if nested folders sync |
| 2026-10-16 | App | `agents init schema-probe` | `CreateCallType` / channel type `Forbidden` on a Feeds-only test app (Singapore) | agent call + channel type on a Feeds app |
| 2026-10-16 | Connectors | `sync .` with `connection: company` | `no app connection with id or label "company"` | Sync fails before you can even open a session. Dashboard label is easy to miss. |
| 2026-10-16 | Nested skills | `load_skill` in `agents test` | `harness: this skill has no files` after we flattened to one `.md` (template README: one markdown file per skill) | Harness wants a folder with extra files. Template and harness disagree. |
| 2026-10-16 | Connectors | `agents test .` (terminal) | Banner: github/linear/slack left out; use `--dashboard` | Cannot test session connectors in the TUI |
| 2026-10-29 | CLI host | Old CLI `2026-10-14-3abc1b3` ListConnectors | NXDOMAIN `accelerate.gcp.stream-io-api.com`. Fixed by `getstream update` → `2026-10-28-02dc1ca` | Working host is `accelerate-us-east4.gcp.stream-io-api.com` |
| 2026-10-30 | GitHub OAuth | Dashboard Connect GitHub (`company`, pending) | GitHub: `redirect_uri is not associated with this application`. Connector `redirect_uri` is `https://accelerate-us-east4.gcp.stream-io-api.com/v1/agents/connectors/oauth/callback`. `GetConnectorOAuthClient github` → router has no customer OAuth client, so this is Stream's operator GitHub app. | Add that callback on Stream's GitHub OAuth app, or document SetConnectorOAuthClient / bearer |
| | Dashboard | connect GitHub/Linear | not started | need beta CLI |
| | | | | |

## Naming (decided)

**Docs Gap** — agent id `docs-gap`. Rejected alternatives: Steward, Keeper, Helios, Loom.
