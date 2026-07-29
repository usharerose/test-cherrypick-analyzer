"""Utilities for working with the Fibonacci sequence."""


def fibonacci(n: int) -> int:
    """Return the Fibonacci number at zero-based position ``n``.

    The sequence starts with ``0, 1, 1, 2, 3, ...``.

    Args:
        n: A non-negative integer.

    Raises:
        TypeError: If ``n`` is not an integer.
        ValueError: If ``n`` is negative.
    """
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")

    previous, current = 0, 1
    for _ in range(n):
        previous, current = current, previous + current

    return previous
