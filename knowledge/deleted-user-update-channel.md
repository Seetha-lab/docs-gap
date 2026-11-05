# Chat: UpdateChannel after DeleteUsers

Official pages:

- https://getstream.io/chat/docs/javascript/gdpr/
- https://getstream.io/chat/docs/javascript/channel_members/

GDPR says delete is async and queryUsers hides the user. It does not say group memberships linger until the task finishes, or that `removeMembers` of a deleted user is 400 / code 4 with no structured field.

Code: `controllers/common/delete_users.go` marks deleted then publishes `DeleteUsers` on the lowest-priority queue. `state/delete_users.go` `deleteMembershipsForUser` removes all channel types. `conversations: hard` only deletes 1:1. `ValidateChannelMembers` in `get_or_create_channel.go` rejects `DeletedAt != nil` with InputError (code 4). UpdateChannel includes `RemoveMembers` in that check before any system message.

Verified 2026-10-24 10:55:12 UTC, app 1142367, three UpdateChannel 400s on `club_chat:` cids. Do not name the customer in a public PR.
