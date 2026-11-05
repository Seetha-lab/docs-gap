<!-- Add under GDPR → Deleting users, after “Deleting users is done asynchronously…”
     Page: https://getstream.io/chat/docs/javascript/gdpr/
     Cross-link from Channel Members → Removing members. -->

### After you call DeleteUsers

The 201 response marks `deleted_at` immediately and returns a task id. Memberships, messages, and 1:1 conversations are removed later by that task. Group channels (more than two members) are not deleted when `conversations` is `hard` — only the user’s membership is removed.

Until the task completes, the user is already deleted but can still appear in member lists, member counts, and channel query responses.

`UpdateChannel` / `removeMembers` **cannot** be used as a cleanup for a deleted user. The API validates every id in `remove_members` (and add / invite / assign-role) against the user record. If `deleted_at` is set, the call returns **400 / code 4**:

```
Unable to update a channel with deleted user {user_id}
```

There is no `exception_fields` and no `unrecoverable` flag. The leave / system message on the same request is never stored — the check runs first. Removing the message does not change the result.

Once the task has completed, retrying `removeMembers` for that id still returns the same 400 for as long as the user row exists. Removing someone who is **not** a member (and not deleted) is a 2xx no-op. Channel not found is **404 / code 16**, not 4.

`queryUsers` always excludes `deleted_at IS NOT NULL`. An empty result for an id is not a reliable “this user was deleted” signal — never existed, soft-deleted, and hard-deleted all look the same. There is no `include_deleted` flag and no way to read `deleted_at`.

**What to do:** poll `GetTask`. When it is completed, skip `removeMembers` for that user. Treat 400 / code 4 whose message contains `deleted user` or `don't exist` as skip, not retry. Retry 429/9, 408/**48** (not 23), 500/−1, and transport errors.
