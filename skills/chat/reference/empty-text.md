# Chat: when is `text` empty?

## Customer question

When does a message have `text: ""`? (Also: empty twin next to a real message, 2–86ms apart.)

## Official docs

[Messages overview / send message](https://getstream.io/chat/docs/javascript/send-message/)

- `text` is **optional**.
- Attachments, polls, location are the usual “no caption” cases.
- The page does **not** say:
  - the API stores `{ "text": "" }` with no attachments
  - default UI SDKs block blank send; `sendMessage` does not
  - two client ids `{userId}-{uuid}` a few ms apart is a double send
  - `html` is generated from `text`, so empty text → empty html
  - soft delete keeps text and sets `type: deleted` (so empty + `regular` is not a delete)

## Code (checked)

- Send payload `MessageRequest.Text` is `validate:"utf8"` only — empty string is allowed.
  `chat/controllers/chat/v1/payload/message.go`
- `html` comes from `TextToHTML()` — empty text stays empty html.
  `chat/types/message.go`
- Android Compose send button: `isInputValid` requires `value.isNotBlank()` or attachments.
  `MessageComposer.kt` `DefaultMessageComposerTrailingContent`
- `ChatClient.sendMessage` does not reject empty text. New id per call: `{user.id}-{uuid}`.
  `ensureId` / `generateMessageId`
- Same-id dedupe does not drop two different ids.

## Patch to add

See `proposed/chat-send-message-empty-text.md` in this agent folder.

## Do not write in the docs

- That Stream will delete the empty twins
- That we will query the customer app
- That this is a confirmed Android 6.45.1 SDK bug (default composer blocks empty; custom send may not)
