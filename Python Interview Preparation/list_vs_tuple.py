"""
List vs tuple: mutability, hashing, and typical use cases.
"""

# Lists are mutable; tuples are immutable.
# Tuples can be dict keys if all elements are hashable; lists cannot.

if __name__ == "__main__":
    lst = [1, 2, 3]
    lst[0] = 10
    assert lst == [10, 2, 3]

    t = (1, 2, 3)
    # t[0] = 10  # would raise TypeError

    coord_index = {(0, 0): "origin", (1, 0): "east"}
    assert coord_index[(0, 0)] == "origin"

    # Lists: homogeneous sequences you append to; tuples: fixed records / keys.
    print("list:", lst, "tuple:", t)
