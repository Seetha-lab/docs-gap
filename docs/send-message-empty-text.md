# Empty text (Chat)

Draft for [Messages overview](https://getstream.io/chat/docs/javascript/send-message/). This is the first Docs Gap fix — a PR on this repo, not on Stream’s docs CMS until we have write access there.

`text` is optional. The API accepts a message with `text` set to an empty string.

That is normal when the message has attachments (image, file, audio, video, voice), a poll, a shared location, or MML, and the user did not add a caption. `html` is generated from `text`, so empty text also means empty `html`.

The API also accepts a message that has no text and no attachments. The default UI SDKs do not send that (the send button stays off until there is text or an attachment). A server-side call, a custom client, or a `before_message_send` webhook can still create it.

A soft-deleted message keeps its original text and sets `type` to `deleted`. An empty `regular` message is not a delete.

Client SDKs set the message id to `{userId}-{uuid}` when you do not pass one. Two sends from the same user a few milliseconds apart are two messages, not one edit. If you see an empty twin next to a real message, look at your send path (custom composer, interceptor, or a second `sendMessage` after the composer was cleared).
