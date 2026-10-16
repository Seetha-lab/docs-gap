---
description: Open a GitHub PR with the docs patch, or a Linear issue if there is no writable docs repo.
deadline: 10m
---

Only run after verify-docs and check-code, and only after the human said **yes**.

## GitHub PR (preferred)

1. Ask which repo and branch if it is not already set. Default guess: their docs repo on `GetStream`. If you cannot write there, stop and use Linear.
2. Create a branch `docs/gap-<short-topic>` from the default branch.
3. One focused change. No drive-by rewrites.
4. Commit message: why, not what. Example: `Document when a Chat message can have empty text.`
5. Open the PR. Body:

```
## Summary
- Gap: …
- Docs page: …
- Code: …

## Test plan
- [ ] Page renders
- [ ] No new promise Stream cannot keep
```

6. Never force-push, never skip hooks, never commit `.env` or keys.

## Linear fallback

If GitHub refuses or docs live in a CMS:

- Title: `Docs gap: <one line>`
- Description: the same summary + the full markdown patch
- Team: Docs (or whatever they name)

## Slack

If Slack is connected, one short message: gap, PR or Linear URL, product. No customer names, no app keys.

## Do not

- Open a PR they did not approve
- “Fix” by deleting customer data or promising a backend wipe
- Touch code repos unless they asked for a code PR (this skill is docs first)
