"""Lesson 1: fixed empty-list progress example. No real user data."""
def completion_percent(statuses):
    if not isinstance(statuses, list):
        raise TypeError("statuses must be a list")
    if any(status not in ("todo", "done") for status in statuses):
        raise ValueError("use only todo or done")
    if not statuses:
        return 0.0
    return round(100 * statuses.count("done") / len(statuses), 1)
