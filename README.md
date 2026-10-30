# GitHub Lesson 1: Fix an empty-list crash

Original Jontaworld teaching code. Synthetic task statuses only; no credentials,
private project files or personal datasets are used.

## Start with the problem

`completion_percent(["done", "todo"])` returns `50.0`.
On the intentionally buggy `main` version, `completion_percent([])` raises
`ZeroDivisionError`. For this example we choose `0.0` when there are no tasks.
That is a product rule for this lesson, not a universal meaning of empty progress.

Run the eight tests with Python 3.14 (standard library only):

```sh
python -m unittest -v
```

The initial main-branch suite intentionally has one error. The lesson fixes it
on `codex/fix-empty-list`, reviews the two-line guard, and reruns the same tests.
Select that fix branch to inspect the corrected version while its pull request
is open. Read branch names before copying code; this is not a production library.

## Learning workflow

1. Reproduce the failure with a test.
2. Create a separate fix branch.
3. Add the smallest relevant guard.
4. Check the diff for unrelated changes.
5. Verify the tests, then propose the change through a pull request.

A commit is not the same as a pull request, and an open pull request does not
mean a change has been merged. Eight passing examples are not proof that every
possible input is correct. No deployment or real business task data is involved.

Development work: https://jontaworld.com
