import matplotlib

matplotlib.use("Agg")  # headless backend for tests

import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402
from matplotlib.axes import Axes  # noqa: E402

from simple_eda import bar, lollipop, slopegraph  # noqa: E402


def sample_df():
    return pd.DataFrame(
        {
            "region": ["North", "South", "East", "West", "Central"],
            "sales_2023": [120, 200, 90, 160, 75],
            "sales_2024": [145, 190, 130, 175, 60],
            "stores": [8, 14, 6, 11, 5],
        }
    )


def test_bar_has_one_bar_per_row_and_no_legend():
    df = sample_df()
    ax = bar(df, "region", "sales_2024", title="Sales by region")
    assert isinstance(ax, Axes)
    assert len(ax.patches) == len(df)
    assert ax.get_legend() is None
    plt.close(ax.figure)


def test_bar_highlight_uses_two_colors():
    ax = bar(sample_df(), "region", "sales_2024", title="t", highlight="West")
    colors = {tuple(p.get_facecolor()) for p in ax.patches}
    assert len(colors) == 2  # one highlighted bar + muted rest
    plt.close(ax.figure)


def test_lollipop_returns_axes():
    ax = lollipop(sample_df(), "region", "stores", title="Stores by region")
    assert isinstance(ax, Axes)
    plt.close(ax.figure)


def test_slopegraph_draws_one_line_per_row():
    df = sample_df()
    ax = slopegraph(df, "region", "sales_2023", "sales_2024", title="Change")
    assert isinstance(ax, Axes)
    assert len(ax.lines) == len(df)
    assert ax.get_legend() is None
    plt.close(ax.figure)
