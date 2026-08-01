"""Visualizations that follow the Evergreen & Emery Data Visualization Checklist.

Design decisions baked in as defaults (so every chart passes the checklist):

* **Text** — a 6-12 word descriptive title, left-justified in the upper left;
  an optional subtitle; data labeled directly on the marks (no legend);
  horizontal text; hierarchical font sizes.
* **Arrangement** — data sorted into an intentional order; two-dimensional
  marks only; no gridlines, boxes, or other decoration.
* **Color** — one intentional highlight color against a muted gray; a
  colorblind-safe blue/orange pair for up/down; everything stays legible in
  black and white.

Each function draws on a Matplotlib ``Axes`` and returns it, so the caller can
save it (``ax.figure.savefig(...)``) or tweak it further.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import pandas as pd

# --- intentional palette (colorblind-safe, B&W-legible) --------------------
MUTED = "#B4B4B4"      # supporting data
HIGHLIGHT = "#2A6EBB"  # the one thing we want the eye to land on (blue)
UP = "#2A6EBB"         # increase (blue)
DOWN = "#E1701A"       # decrease (orange)
INK = "#333333"        # text
SUBTLE = "#767676"     # subtitle / secondary text


def _titles(ax, title: str, subtitle: str | None) -> None:
    """Left-justified descriptive title (upper left) + optional subtitle."""
    ax.text(0.0, 1.14, title, transform=ax.transAxes, ha="left", va="bottom",
            fontsize=14, fontweight="bold", color=INK)
    if subtitle:
        ax.text(0.0, 1.045, subtitle, transform=ax.transAxes, ha="left",
                va="bottom", fontsize=10.5, color=SUBTLE)


def _strip(ax, keep_left_labels: bool = True) -> None:
    """Remove spines, ticks and gridlines — leave only the data and labels."""
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.tick_params(length=0)
    ax.grid(False)
    ax.set_xticks([])
    if not keep_left_labels:
        ax.set_yticks([])


def bar(df: pd.DataFrame, category: str, value: str, *, title: str,
        subtitle: str | None = None, highlight: str | None = None,
        ax=None):
    """Horizontal bar chart, sorted, with values labeled directly on the bars.

    ``highlight`` names the one category to paint in the highlight color; all
    other bars stay muted gray.
    """
    data = df[[category, value]].dropna().sort_values(value)  # largest on top
    if ax is None:
        _, ax = plt.subplots(figsize=(7, 0.55 * len(data) + 1.6))

    colors = [HIGHLIGHT if c == highlight else MUTED for c in data[category]]
    ax.barh(data[category], data[value], color=colors, height=0.62)

    span = data[value].max() or 1
    for cat, val in zip(data[category], data[value]):
        ax.text(val + span * 0.01, cat, f"{val:,.0f}", va="center",
                ha="left", fontsize=10, color=INK)

    _strip(ax)
    ax.set_xlim(0, span * 1.12)
    ax.tick_params(axis="y", labelsize=10)
    _titles(ax, title, subtitle)
    ax.figure.subplots_adjust(top=0.80, left=0.22, right=0.97, bottom=0.06)
    return ax


def lollipop(df: pd.DataFrame, category: str, value: str, *, title: str,
             subtitle: str | None = None, highlight: str | None = None,
             ax=None):
    """Lollipop chart — a bar chart's lighter cousin (a stem plus a dot)."""
    data = df[[category, value]].dropna().sort_values(value)
    if ax is None:
        _, ax = plt.subplots(figsize=(7, 0.55 * len(data) + 1.6))

    span = data[value].max() or 1
    for cat, val in zip(data[category], data[value]):
        color = HIGHLIGHT if cat == highlight else MUTED
        ax.plot([0, val], [cat, cat], color=color, lw=2, zorder=1)
        ax.scatter(val, cat, color=color, s=90, zorder=2)
        ax.text(val + span * 0.02, cat, f"{val:,.0f}", va="center",
                ha="left", fontsize=10, color=INK)

    _strip(ax)
    ax.set_xlim(0, span * 1.15)
    ax.tick_params(axis="y", labelsize=10)
    _titles(ax, title, subtitle)
    ax.figure.subplots_adjust(top=0.80, left=0.22, right=0.97, bottom=0.06)
    return ax


def slopegraph(df: pd.DataFrame, category: str, start: str, end: str, *,
               title: str, subtitle: str | None = None,
               start_label: str | None = None, end_label: str | None = None,
               ax=None):
    """Slopegraph — connect each category's start and end value with a line.

    Lines slanting up are blue (increase), down are orange (decrease); both
    ends are labeled directly, so there is no axis or legend to read.
    """
    data = df[[category, start, end]].dropna()
    if ax is None:
        _, ax = plt.subplots(figsize=(6.5, 0.5 * len(data) + 2.4))

    for _, row in data.iterrows():
        rose = row[end] >= row[start]
        color = UP if rose else DOWN
        ax.plot([0, 1], [row[start], row[end]], color=color, lw=1.9,
                marker="o", markersize=5, solid_capstyle="round", zorder=2)
        ax.text(-0.03, row[start], f"{row[category]}  {row[start]:,.0f}",
                ha="right", va="center", fontsize=9.5, color=INK)
        ax.text(1.03, row[end], f"{row[end]:,.0f}  {row[category]}",
                ha="left", va="center", fontsize=9.5, color=INK)

    # headroom so the period headers clear the highest points
    values = pd.concat([data[start], data[end]])
    lo, hi = float(values.min()), float(values.max())
    pad = (hi - lo) * 0.22 or 1.0
    ax.set_ylim(lo - pad * 0.5, hi + pad)
    ax.set_xlim(-0.55, 1.55)

    header_y = hi + pad * 0.45
    ax.text(0, header_y, start_label or start, ha="center", va="bottom",
            fontsize=11, fontweight="bold", color=INK)
    ax.text(1, header_y, end_label or end, ha="center", va="bottom",
            fontsize=11, fontweight="bold", color=INK)

    _strip(ax, keep_left_labels=False)
    _titles(ax, title, subtitle)
    ax.figure.subplots_adjust(top=0.72, left=0.16, right=0.84, bottom=0.05)
    return ax
