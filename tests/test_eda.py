import pandas as pd

from simple_eda import (
    categorical_columns,
    missing,
    numeric_columns,
    summarize,
)


def sample_df():
    return pd.DataFrame(
        {
            "age": [30, 25, None],
            "city": ["SF", "LA", "SF"],
            "score": [1.0, 2.5, 3.0],
        }
    )


def test_summarize():
    out = summarize(sample_df())
    assert out["rows"] == 3
    assert out["cols"] == 3
    assert out["columns"] == ["age", "city", "score"]
    # dtype spelling varies across pandas versions ("object" vs "str"); just
    # confirm every column is reported.
    assert set(out["dtypes"]) == {"age", "city", "score"}


def test_missing():
    assert missing(sample_df()) == {"age": 1, "city": 0, "score": 0}


def test_numeric_columns():
    assert numeric_columns(sample_df()) == ["age", "score"]


def test_categorical_columns():
    assert categorical_columns(sample_df()) == ["city"]


def test_returns_plain_python_objects():
    out = summarize(sample_df())
    assert isinstance(out, dict)
    assert isinstance(numeric_columns(sample_df()), list)
