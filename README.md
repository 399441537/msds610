# thefuck

A private practice package for **MSDS610**.

> Note: `thefuck` here is a private/course package and is unrelated to the
> public tool of the same name. It is not published to PyPI.

## Install

Because this package is private (not on PyPI), install it directly from GitHub:

```bash
pip install "git+https://github.com/399441537/msds610.git"
```

Or install from a local clone (editable / development mode):

```bash
git clone https://github.com/399441537/msds610.git
cd msds610
pip install -e .
```

## What's inside

`thefuck.confusables.CONFUSABLES` — a mapping of characters that *look* like
ASCII but aren't. When a Chinese IME is left in full-width mode, these sneak
into source code and cause a `SyntaxError` even though the line looks fine on
screen (the spiritual cousin of the C prank `#define true false`).

```python
from thefuck import CONFUSABLES

CONFUSABLES["（"]   # -> "("   full-width parenthesis
CONFUSABLES["“"]   # -> '"'   smart double quote
CONFUSABLES["，"]   # -> ","   full-width comma
```

## Development

```bash
pip install -e ".[dev]"
pytest
```
