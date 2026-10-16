---
description: Check Stream source (GitHub or this machine) and say what the product actually does.
deadline: 10m
---

Docs can be late. Code is what ships. You prove the gap against code.

## Where to look

Use the GitHub connector on **GetStream** repos. Prefer:

- Chat API: `GetStream/chat` if they have it, else local `chat/` in the workspace
- Chat send payload: `controllers/chat/v1/payload/message.go` (`text` is `utf8`, not required)
- Message model: `types/message.go`
- Android composer: `GetStream/stream-chat-android` — `MessageComposer.kt` `isInputValid`, `ChatClient.sendMessage`
- JS send: `GetStream/stream-chat-js`

If they only have a local clone, search that. Do not query a customer Stream app.

## Do

1. Find the function or struct that decides the behaviour.
2. Quote the bit that matters (e.g. `text` validate is `utf8` only; send button checks `isNotBlank`).
3. Answer with:
   - **Repo / file**
   - **Does:** one or two lines
   - **Vs docs:** match / docs missing / docs wrong

## Do not

- Test on customer or guest apps. Only Seetha apps if an API check is required (`g6nd8fstmy5s`, `xet9vdq8j7ye`), and only if they asked.
- Claim an SDK bug you did not see.
- Paste secrets or `.env`.
