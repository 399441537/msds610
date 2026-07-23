# simple-eda-yzheng74

A tiny exploratory-data-analysis (EDA) toolkit for pandas DataFrames, built for
**MSDS610**.

- **Distribution name** (PyPI / pip): `simple-eda-yzheng74`
- **Import name** (in Python): `simple_eda`

## Install

From PyPI (once published):

```bash
pip install simple-eda-yzheng74
```

From a local clone (development mode):

```bash
git clone https://github.com/399441537/msds610.git
cd msds610
pip install -e ".[dev]"
```

## EDA helpers

Every function takes a `pandas.DataFrame` and returns a plain Python object
(dict / list), so results are easy to print, serialize, or test.

```python
import pandas as pd
from simple_eda import summarize, missing, numeric_columns, categorical_columns

df = pd.DataFrame({"age": [30, 25, None], "city": ["SF", "LA", "SF"]})

summarize(df)            # {'rows': 3, 'cols': 2, 'columns': [...], 'dtypes': {...}}
missing(df)              # {'age': 1, 'city': 0}
numeric_columns(df)      # ['age']
categorical_columns(df)  # ['city']
```

## Bonus: full-width punctuation codec

The package also ships a source codec (the Python analog of C's `#define`).
Add `# coding: simple_eda` to the first or second line of a file and any
full-width / Chinese punctuation is rewritten to ASCII *while Python loads the
file* — the file on disk is never changed:

```python
# coding: simple_eda
def add（a，b）：      # full-width parens, comma, colon
    return a ＋ b     # full-width plus
```

Installing the package drops a `simple_eda.pth` into `site-packages`, so the
codec auto-registers at interpreter startup. (`# coding: thefuck` also works as
a legacy alias.)

## Development & tests

```bash
pip install -e ".[dev]"
pytest
```

## Publishing (TestPyPI → PyPI)

```bash
python -m build                              # build wheel + sdist into dist/
python -m twine check dist/*                 # validate metadata
python -m twine upload --repository testpypi dist/*   # upload to TestPyPI first
python -m twine upload dist/*                # then the real PyPI
```

Uploading requires a PyPI / TestPyPI account and an API token.
