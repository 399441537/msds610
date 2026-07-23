"""A tiny exploratory-data-analysis (EDA) toolkit for pandas DataFrames.

Every function follows the same contract: it takes a ``pandas.DataFrame`` and
returns a plain Python object (dict / list) so the results are easy to print,
serialize, or assert on in tests.
"""

from __future__ import annotations

import pandas as pd


def summarize(df: pd.DataFrame) -> dict:
    """Return a small overview of the DataFrame.

    Keys: ``rows``, ``cols``, ``columns`` (list of names), ``dtypes``
    (column name -> dtype string).
    """
    return {
        "rows": int(df.shape[0]),
        "cols": int(df.shape[1]),
        "columns": list(df.columns),
        "dtypes": {col: str(dtype) for col, dtype in df.dtypes.items()},
    }


def missing(df: pd.DataFrame) -> dict:
    """Return the number of missing (NaN) values per column as a dict."""
    return {col: int(n) for col, n in df.isna().sum().items()}


def numeric_columns(df: pd.DataFrame) -> list:
    """Return the names of the numeric columns."""
    return list(df.select_dtypes(include="number").columns)


def categorical_columns(df: pd.DataFrame) -> list:
    """Return the names of the non-numeric (categorical / object) columns."""
    return list(df.select_dtypes(exclude="number").columns)
