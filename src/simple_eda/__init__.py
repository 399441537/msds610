"""simple_eda — a tiny EDA + visualization toolkit for MSDS610.

Features:

* **Visualizations** that follow the Evergreen & Emery Data Visualization
  Checklist (:func:`bar`, :func:`lollipop`, :func:`slopegraph`).
* **EDA helpers** for pandas DataFrames (:func:`summarize`, :func:`missing`,
  :func:`numeric_columns`, :func:`categorical_columns`).
* A sample dataset (:func:`load_sample`).
* A source codec that rewrites full-width / Chinese punctuation to ASCII when a
  file declares ``# coding: simple_eda`` (see :mod:`simple_eda.codec`).
"""

from simple_eda.codec import register
from simple_eda.confusables import CONFUSABLES
from simple_eda.datasets import load_sample
from simple_eda.eda import (
    categorical_columns,
    missing,
    numeric_columns,
    summarize,
)
from simple_eda.viz import bar, lollipop, slopegraph

# Importing the package registers the source codec.
register()

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
    # extras
    "CONFUSABLES",
    "register",
    "__version__",
]
