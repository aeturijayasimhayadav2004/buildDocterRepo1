Phase 10 verification, second pass

Same shape as the first: a harmless note file. The build fails on the
broken apt-get step in ci.yml, which this diff does not touch, so the
expected lane is informational.

What this one is really testing is the GitHub token write permission -
the previous run classified correctly but could not post its comment,
failing with 403 on post_commit_comment.
