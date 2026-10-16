# Docs Gap

Hackathon agent: find a hole in Stream docs, check the official page and the code, open a PR (or Linear).

Uses the Sovereign AI surface they asked us to hit:

| They said | Where it is |
|---|---|
| Conversation loop | `instructions.md` — ask → verify docs → check code → confirm → PR |
| Nested skills | `skills/chat/` (SKILL + `reference/`), same for video / feeds / moderation; plus `verify-docs`, `check-code`, `open-pr` |
| Connectors | GitHub (PR), Linear (fallback), Slack (tell the company) in `agent.yaml` |
| MCP | Those connectors are the catalog MCP. Extra `mcp_servers` when a docs MCP URL exists — do not invent one |
| CLI | Beta `getstream` — init + sync this folder |
| Dashboard | Watch the session URL the runner prints |

Not a Zendesk writer. Not WWSD. Not a live call.

## First real gap (already verified)

**When is `text: ""`?**

- Docs: `text` is optional. They do not say empty twins / UI vs API / `{userId}-{uuid}`.
- Code: send payload allows empty; Android default composer does not; two ids = two sends.
- Patch: `proposed/chat-send-message-empty-text.md`

Do not open the PR until you say which docs repo we can write to.

## Run

1. Beta CLI (your `getstream` 1.1.0 is not enough):

```bash
curl -fsSL https://getstream.io/cli/beta/install.sh | bash
getstream --version    # should look like 2026-10-13-eab135f
```

2. Connect this folder to your Stream app (your keys only: `g6nd8fstmy5s` / `xet9vdq8j7ye`):

```bash
cd docs-gap
getstream init
getstream agents init
```

3. Dashboard → Library → Connectors: GitHub, Linear, Slack. Label the company ones `company`.

4. Chat: paste a question or a payload. First demo:

```
When will a message have text: "" ?
```

Or run the example the same way as Vision-Agents `mcp_plugins` (`stream.Accelerated(config="docs-gap")`) from a clone of [Vision-Agents `accelerate`](https://github.com/GetStream/Vision-Agents/tree/accelerate).

## Rules

- Official getstream.io docs only for “what the docs say”
- Code when they asked us to check code
- No customer app queries
- No PR without a yes
- Bugs / naming: `#hackathon-product-feedback`
