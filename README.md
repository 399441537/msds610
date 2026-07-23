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

## Usage

As a library:

```python
from thefuck import greet, add

print(greet("MSDS610"))  # Hello, MSDS610!
print(add(2, 3))         # 5
```

As a command-line tool:

```bash
thefuck            # Hello, world!
thefuck MSDS610    # Hello, MSDS610!
thefuck --version
```

## Development

```bash
pip install -e ".[dev]"
pytest
```
