# thefuck

A private practice package for **MSDS610**.

> Note: `thefuck` here is a private/course package and is unrelated to the
> public tool of the same name. It is not published to PyPI.

## Install

Because this package is private (not on PyPI), install it directly from GitHub:

```bash
pip install "git+https://github.com/399441537/msds610.git"
```

Or install from a local clone:

```bash
git clone https://github.com/399441537/msds610.git
cd msds610
pip install .
```

## What it does

Ever typed full-width / Chinese punctuation by accident (`（`, `，`, `“`) and
got a `SyntaxError` on a line that looks perfectly fine? This package installs
a **source codec** — the Python analog of C's `#define` — that swaps those
look-alike characters for their ASCII equivalents *while Python loads the
file*, before the parser ever sees them.

Opt a file in with a coding cookie on its **first or second line**:

```python
# coding: thefuck
def add（a，b）：      # full-width parens, comma, colon
    return a ＋ b     # full-width plus

print（add（1，2））   # -> 3
```

Running that file just works. Your file on disk is **not modified** — the
substitution happens only in memory at load time, exactly like `#define`.

### How activation works

Installing the package drops a `thefuck.pth` file into `site-packages`, whose
single line `import thefuck.codec` registers the codec at every interpreter
startup. So once installed, any file with `# coding: thefuck` works
automatically — you don't even need to `import thefuck` yourself.

The characters it rewrites are listed in `thefuck.confusables.CONFUSABLES`
(full-width brackets/quotes/operators, ideographic comma & period, full-width
space, …).

## Development

```bash
pip install -e ".[dev]"
pytest
```

Note: editable installs may not place the `.pth`; during development just
`import thefuck` once to register the codec.
