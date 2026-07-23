"""Common easy-to-make programming mistakes ("gotchas").

Inspired by the classic C prank ``#define true false`` — this module collects
bugs that beginners (and everyone else) trip over, each paired with WHY it
happens and the correct way to write it. It is meant for teaching, not for
copy-pasting the broken versions into real code.

Every entry exposes a ``buggy`` and a ``fixed`` callable so you can run and
compare them::

    from thefuck import gotchas
    print(gotchas.explain("mutable_default"))
    gotchas.mutable_default_buggy()   # surprising
    gotchas.mutable_default_fixed()   # correct
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Optional


# --------------------------------------------------------------------------
# 1. Mutable default argument
# --------------------------------------------------------------------------
def mutable_default_buggy(item: str, bucket: list = []) -> list:
    """WRONG: the default list is created once and shared across all calls."""
    bucket.append(item)
    return bucket


def mutable_default_fixed(item: str, bucket: Optional[list] = None) -> list:
    """RIGHT: use ``None`` as the sentinel and build a fresh list each call."""
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket


# --------------------------------------------------------------------------
# 2. Comparing with `is` instead of `==`
# --------------------------------------------------------------------------
def identity_compare_buggy(n: int) -> bool:
    """WRONG: ``is`` compares identity; it only "works" for small cached ints."""
    return n is 1000  # noqa: F632 - intentional bug for teaching


def identity_compare_fixed(n: int) -> bool:
    """RIGHT: compare values with ``==``."""
    return n == 1000


# --------------------------------------------------------------------------
# 3. Floating-point equality
# --------------------------------------------------------------------------
def float_equality_buggy() -> bool:
    """WRONG: 0.1 + 0.2 is not exactly 0.3 in binary floating point."""
    return 0.1 + 0.2 == 0.3


def float_equality_fixed() -> bool:
    """RIGHT: compare with a tolerance via ``math.isclose``."""
    import math

    return math.isclose(0.1 + 0.2, 0.3)


# --------------------------------------------------------------------------
# 4. Late-binding closures in a loop
# --------------------------------------------------------------------------
def late_binding_buggy() -> list:
    """WRONG: every lambda captures the SAME ``i``, so all return 2."""
    funcs = [lambda: i for i in range(3)]
    return [f() for f in funcs]  # -> [2, 2, 2]


def late_binding_fixed() -> list:
    """RIGHT: bind the current value with a default argument."""
    funcs = [lambda i=i: i for i in range(3)]
    return [f() for f in funcs]  # -> [0, 1, 2]


# --------------------------------------------------------------------------
# 5. Mutating a list while iterating over it
# --------------------------------------------------------------------------
def mutate_while_iterating_buggy(numbers: list) -> list:
    """WRONG: removing items during iteration skips elements."""
    for n in numbers:
        if n % 2 == 0:
            numbers.remove(n)
    return numbers


def mutate_while_iterating_fixed(numbers: list) -> list:
    """RIGHT: iterate over a copy (or build a new list)."""
    return [n for n in numbers if n % 2 != 0]


# --------------------------------------------------------------------------
# 6. Integer vs. true division
# --------------------------------------------------------------------------
def division_buggy(total: int, count: int) -> int:
    """WRONG: ``//`` floors the result, silently dropping the remainder."""
    return total // count


def division_fixed(total: int, count: int) -> float:
    """RIGHT: use ``/`` for an average / true division."""
    return total / count


# --------------------------------------------------------------------------
# Registry so the gotchas can be listed and explained programmatically
# --------------------------------------------------------------------------
@dataclass(frozen=True)
class Gotcha:
    name: str
    title: str
    why: str
    buggy: Callable
    fixed: Callable


GOTCHAS = {
    g.name: g
    for g in [
        Gotcha(
            "mutable_default",
            "Mutable default argument",
            "Default values are evaluated once at definition time, so a default "
            "list/dict is shared between every call.",
            mutable_default_buggy,
            mutable_default_fixed,
        ),
        Gotcha(
            "identity_compare",
            "Using `is` instead of `==`",
            "`is` checks object identity, not equality. It appears to work only "
            "because CPython caches small integers (-5..256).",
            identity_compare_buggy,
            identity_compare_fixed,
        ),
        Gotcha(
            "float_equality",
            "Floating-point equality",
            "Binary floating point can't represent 0.1/0.2/0.3 exactly, so "
            "`0.1 + 0.2 == 0.3` is False.",
            float_equality_buggy,
            float_equality_fixed,
        ),
        Gotcha(
            "late_binding",
            "Late-binding closures in a loop",
            "Closures capture the variable, not its value. By the time the "
            "lambdas run, the loop variable holds its final value.",
            late_binding_buggy,
            late_binding_fixed,
        ),
        Gotcha(
            "mutate_while_iterating",
            "Mutating a list while iterating",
            "Removing elements shifts the remaining ones, so the iterator skips "
            "the item after each removal.",
            mutate_while_iterating_buggy,
            mutate_while_iterating_fixed,
        ),
        Gotcha(
            "division",
            "Integer (`//`) vs. true (`/`) division",
            "`//` floors and returns an int, silently discarding the fractional "
            "part — a classic source of wrong averages.",
            division_buggy,
            division_fixed,
        ),
    ]
}


def list_gotchas() -> list:
    """Return the names of all registered gotchas."""
    return list(GOTCHAS)


def explain(name: str) -> str:
    """Return a human-readable explanation of a single gotcha."""
    try:
        g = GOTCHAS[name]
    except KeyError:
        raise KeyError(
            f"Unknown gotcha {name!r}. Try one of: {', '.join(GOTCHAS)}"
        ) from None
    return f"{g.title}\n{'-' * len(g.title)}\n{g.why}"
