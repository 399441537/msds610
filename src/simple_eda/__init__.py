"""simple_eda — a tiny EDA toolkit for MSDS610.

Two features:

* EDA helpers for pandas DataFrames (:func:`summarize`, :func:`missing`,
  :func:`numeric_columns`, :func:`categorical_columns`).
* A source codec that rewrites full-width / Chinese punctuation to ASCII when a
  file declares ``# coding: simple_eda`` (see :mod:`simple_eda.codec`).
"""

from simple_eda.codec import register
from simple_eda.confusables import CONFUSABLES
from simple_eda.eda import (
    categorical_columns,
    missing,
    numeric_columns,
    summarize,
)

# Importing the package registers the source codec.
register()

__version__ = "0.1.0"
__all__ = [
    "summarize",
    "missing",
    "numeric_columns",
    "categorical_columns",
    "CONFUSABLES",
    "register",
    "__version__",
]
