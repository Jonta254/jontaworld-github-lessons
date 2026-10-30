"""Lesson 1: deliberately buggy main version. No real user data."""
def completion_percent(statuses):
    if not isinstance(statuses, list):
        raise TypeError("statuses must be a list")
    if any(status not in ("todo", "done") for status in statuses):
        raise ValueError("use only todo or done")
    return round(100 * statuses.count("done") / len(statuses), 1)
