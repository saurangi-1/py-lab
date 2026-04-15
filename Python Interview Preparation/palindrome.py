"""
Palindrome check: string reads the same forwards and backwards.
"""


def is_palindrome(s: str) -> bool:
    """Using slice (simple and idiomatic)."""
    return s == s[::-1]


def is_palindrome_two_pointer(s: str) -> bool:
    """Two pointers, O(n) time, O(1) extra space."""
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def is_palindrome_normalized(s: str) -> bool:
    """Ignore case and non-alphanumeric characters."""
    cleaned = "".join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    assert is_palindrome("racecar")
    assert is_palindrome_two_pointer("racecar")
    assert is_palindrome_normalized("A man, a plan, a canal: Panama")
    print(is_palindrome("hello"))
