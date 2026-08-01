import matplotlib

matplotlib.use("Agg")  # headless backend for tests

import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.axes import Axes  # noqa: E402

from simple_eda import bar, load_sample, lollipop, slopegraph  # noqa: E402

df = load_sample()


def test_bar_has_one_bar_per_row_and_no_legend():
    ax = bar(df, "region", "sales_2024", title="Sales by region")
    assert isinstance(ax, Axes)
    assert len(ax.patches) == len(df)
    assert ax.get_legend() is None
    plt.close(ax.figure)


def test_bar_highlight_uses_two_colors():
    ax = bar(df, "region", "sales_2024", title="t", highlight="West")
    colors = {tuple(p.get_facecolor()) for p in ax.patches}
    assert len(colors) == 2  # one highlighted bar + muted rest
    plt.close(ax.figure)


def test_lollipop_returns_axes():
    ax = lollipop(df, "region", "stores", title="Stores by region")
    assert isinstance(ax, Axes)
    plt.close(ax.figure)


def test_slopegraph_draws_one_line_per_row():
    ax = slopegraph(df, "region", "sales_2023", "sales_2024", title="Change")
    assert isinstance(ax, Axes)
    assert len(ax.lines) == len(df)
    assert ax.get_legend() is None
    plt.close(ax.figure)
