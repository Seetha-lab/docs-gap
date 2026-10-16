---
description: Chat docs gaps — messages, webhooks, request_info, empty text, SDKs.
deadline: 5m
---

You are the Chat playbook. Read `reference/` only when the topic matches.

Known first gap: empty `text: ""` — read `reference/empty-text.md`.

Other Chat holes you may see:

- `request_info.sdk` / `x-stream-client` (mobile vs web)
- webhooks `message.new`
- custom fields flattened on the message (`region`, `legacyId`)

Always hand off to `verify-docs` then `check-code`. Do not open a PR yourself.
