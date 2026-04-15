"""
Reverse a string. Strings are immutable: methods return new strings.
"""


def reverse_string_slice(s: str) -> str:
    return s[::-1]


def reverse_string_join(s: str) -> str:
    return "".join(reversed(s))


if __name__ == "__main__":
    s = "Python"
    assert reverse_string_slice(s) == reverse_string_join(s) == "nohtyP"
    print(reverse_string_slice("hello"))
