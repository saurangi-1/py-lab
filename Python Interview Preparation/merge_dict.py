"""
Merge dictionaries: later keys win when the same key appears in both.
Python 3.9+: use `a | b`. Older style: `{**a, **b}`.
"""


def merge_dicts(a: dict, b: dict) -> dict:
    """Return a new dict: keys from `b` override keys from `a`."""
    return {**a, **b}


if __name__ == "__main__":
    left = {"x": 1, "y": 2}
    right = {"y": 99, "z": 3}
    assert merge_dicts(left, right) == {"x": 1, "y": 99, "z": 3}
    # Equivalent on 3.9+
    assert left | right == merge_dicts(left, right)
    print(merge_dicts(left, right))
