Phase 10 verification

A harmless note. The build fails on a broken apt-get step in ci.yml,
which this diff does not touch - so the expected lane is informational.

What this proves if a diagnosis appears: the rotated WEBHOOK_SECRET,
GITHUB_TOKEN, GROQ_API_KEY and database password all work together in
production.
