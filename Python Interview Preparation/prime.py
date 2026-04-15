"""
Prime numbers: integers greater than 1 with no positive divisors other than 1 and itself.
"""

import math


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = int(math.isqrt(n))
    for d in range(3, limit + 1, 2):
        if n % d == 0:
            return False
    return True


def primes_up_to(n: int) -> list[int]:
    """All primes from 2 through n inclusive."""
    return [x for x in range(2, n + 1) if is_prime(x)]


if __name__ == "__main__":
    assert not is_prime(1)
    assert is_prime(2)
    assert is_prime(17)
    assert not is_prime(18)
    print(primes_up_to(30))
