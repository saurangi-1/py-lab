"""
Find the second highest distinct number in a list without using sort or set.

Returns None if there is no second distinct value (empty list, one element,
or all elements equal).
"""

from typing import Optional


def second_highest(nums: list[float]) -> Optional[float]:
    first = second = float("-inf")

    for num in nums:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num

    if second == float("-inf"):
        return None
    return second


if __name__ == "__main__":
    assert second_highest([10, 5, 8, 20, 15]) == 15
    assert second_highest([5, 5]) is None
    assert second_highest([42]) is None
    assert second_highest([]) is None
    print(second_highest([10, 5, 8, 20, 15]))
