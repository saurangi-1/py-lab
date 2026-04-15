"""
*args and **kwargs: variable positional and keyword arguments in Python.
"""


def sum_all(first, *args, extra=0, **kwargs):
    """
    `first` is a required positional parameter.
    `*args` collects extra positional arguments into a tuple.
    `extra` is keyword-only (after *args).
    `**kwargs` collects extra keyword arguments into a dict.
    """
    total = first + sum(args) + extra
    if kwargs:
        total += sum(kwargs.values())
    return total


def describe_call(name, *args, **kwargs):
    """Demonstrates forwarding *args and **kwargs."""
    parts = [f"name={name!r}", f"args={args}", f"kwargs={kwargs}"]
    return ", ".join(parts)


if __name__ == "__main__":
    assert sum_all(1, 2, 3, extra=4) == 10
    assert sum_all(1, 2, a=5, b=6) == 14
    print(describe_call("demo", 1, 2, x=10, y=20))
