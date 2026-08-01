"""A small, deterministic sample dataset for demos and tests.

Fictional annual sales (in thousands of USD) for a coffee chain's regions,
with two years so it works for comparison charts (bar, lollipop) and
before/after charts (slopegraph).
"""

from __future__ import annotations

import pandas as pd

_SAMPLE = {
    "region": ["North", "South", "East", "West", "Central"],
    "sales_2023": [120, 200, 90, 160, 75],
    "sales_2024": [145, 190, 130, 175, 60],
    "stores": [8, 14, 6, 11, 5],
}


def load_sample() -> pd.DataFrame:
    """Return the sample sales DataFrame (a fresh copy each call)."""
    return pd.DataFrame(_SAMPLE)
