"""
Remove duplicates from a list: preserve order vs sorted unique.
"""


def unique_preserve_order(items: list) -> list:
    """First occurrence wins; stable order (Python 3.7+ dict preserves insertion order)."""
    return list(dict.fromkeys(items))


def unique_sorted(items: list) -> list:
    """Sorted unique values; use when order should follow sort order."""
    return sorted(set(items))


if __name__ == "__main__":
    xs = [3, 1, 2, 1, 3, 2]
    assert unique_preserve_order(xs) == [3, 1, 2]
    assert unique_sorted(xs) == [1, 2, 3]
    print(unique_preserve_order(["b", "a", "b"]))
