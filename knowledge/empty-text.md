# Chat: when is `text` empty?

Official page: https://getstream.io/chat/docs/javascript/send-message/

`text` is optional. The page does not say the API stores `{ "text": "" }` with no attachments, that default UI blocks blank send, or that two `{userId}-{uuid}` ids a few ms apart are a double send.

Code: send payload `Text` is `validate:"utf8"` only. `html` comes from `TextToHTML()`. Android Compose send button requires `isNotBlank()` or attachments. `ChatClient.sendMessage` does not reject empty text.

Soft delete keeps text and sets `type: deleted`. Empty + `regular` is not a delete.

Do not write that Stream will delete the twins or query the customer app.
