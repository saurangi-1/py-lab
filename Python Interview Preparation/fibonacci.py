"""
Fibonacci sequence: F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2).
"""


def fibonacci_terms(n: int) -> list[int]:
    """Return the first `n` Fibonacci numbers (iterative, O(n) time, O(n) space)."""
    if n <= 0:
        return []
    if n == 1:
        return [0]
    out = [0, 1]
    for _ in range(2, n):
        out.append(out[-1] + out[-2])
    return out


def fibonacci_generator():
    """Infinite Fibonacci generator (for discussion)."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    assert fibonacci_terms(0) == []
    assert fibonacci_terms(7) == [0, 1, 1, 2, 3, 5, 8]
    gen = fibonacci_generator()
    first_ten = [next(gen) for _ in range(10)]
    assert first_ten == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    print(fibonacci_terms(12))
