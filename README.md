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
thefuck greet            # Hello, world!
thefuck greet MSDS610    # Hello, MSDS610!
thefuck --version
```

## Common gotchas

The `thefuck.gotchas` module collects easy-to-make programming mistakes — the
Python cousins of the classic C prank `#define true false`. Each one ships a
`buggy` and a `fixed` version plus an explanation, so you can run and compare
them:

```python
from thefuck import gotchas

print(gotchas.list_gotchas())
print(gotchas.explain("mutable_default"))

gotchas.late_binding_buggy()   # [2, 2, 2]  <- surprising
gotchas.late_binding_fixed()   # [0, 1, 2]  <- correct
```

Or from the command line:

```bash
thefuck gotchas                # list all gotchas
thefuck gotchas float_equality # explain one
```

Covered so far: mutable default arguments, `is` vs `==`, floating-point
equality, late-binding closures, mutating a list while iterating, and
integer vs. true division.

## Development

```bash
pip install -e ".[dev]"
pytest
```
