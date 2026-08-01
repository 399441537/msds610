"""simple_eda — a tiny visualization + EDA toolkit for MSDS610.

* Visualizations that follow the Evergreen & Emery Data Visualization Checklist
  (:func:`bar`, :func:`lollipop`, :func:`slopegraph`).
* EDA helpers for pandas DataFrames (:func:`summarize`, :func:`missing`,
  :func:`numeric_columns`, :func:`categorical_columns`).
* A sample dataset (:func:`load_sample`).
"""

from simple_eda.datasets import load_sample
from simple_eda.eda import (
    categorical_columns,
    missing,
    numeric_columns,
    summarize,
)
from simple_eda.viz import bar, lollipop, slopegraph

__version__ = "0.1.0"
__all__ = [
    # visualizations
    "bar",
    "lollipop",
    "slopegraph",
    # eda
    "summarize",
    "missing",
    "numeric_columns",
    "categorical_columns",
    # data
    "load_sample",
    "__version__",
]
