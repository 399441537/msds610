"""Core functionality for the thefuck package."""

from __future__ import annotations


def greet(name: str = "world") -> str:
    """Return a friendly greeting.

    >>> greet("MSDS610")
    'Hello, MSDS610!'
    """
    return f"Hello, {name}!"


def add(a: float, b: float) -> float:
    """Add two numbers together.

    >>> add(2, 3)
    5
    """
    return a + b
