# simple-eda-yzheng74

A tiny **visualization + EDA** toolkit for pandas DataFrames, built for
**MSDS610**. Every chart is designed to satisfy the
[Evergreen & Emery *Data Visualization Checklist*](https://stephanieevergreen.com/data-visualization-checklist/)
by default.

- **Distribution name** (PyPI / pip): `simple-eda-yzheng74`
- **Import name** (in Python): `simple_eda`

## Install

```bash
pip install simple-eda-yzheng74          # from PyPI (once published)
```

From a local clone (development mode):

```bash
git clone https://github.com/399441537/msds610.git
cd msds610
pip install -e ".[dev]"
```

## Quick start

```python
from simple_eda import load_sample, bar, slopegraph, lollipop

df = load_sample()   # fictional regional coffee sales, 2023 & 2024

ax = bar(df, "region", "sales_2024",
         title="West and North lead 2024 regional coffee sales",
         subtitle="Net sales by region (thousands USD)", highlight="West")
ax.figure.savefig("bar.png", dpi=150)
```

The sample dataset also ships as [`examples/sample_data.csv`](examples/sample_data.csv).

## ⭐ My two favorite visualizations

### 1. Horizontal bar — `bar()`

![horizontal bar chart](examples/fav1_bar.png)

My favorite workhorse: nothing communicates a ranking faster. Aesthetic
choices:

- **Horizontal bars** keep the category labels horizontal and instantly
  readable — no tilted text.
- **Sorted largest-to-smallest** gives the reader an intentional order, so the
  ranking *is* the shape of the chart.
- **Values labeled directly** at the end of each bar, so I could delete the
  x-axis, its ticks, and all gridlines — the data carries the numbers.
- **One highlight color** (a single blue bar) against **muted gray** points the
  eye at the "so what?"; because it's the only dark bar, the emphasis survives
  even when the chart is printed in black and white.
- A **descriptive, left-justified title** in the upper-left states the takeaway
  in ~8 words instead of a generic "Sales by region."

### 2. Slopegraph — `slopegraph()`

![slopegraph](examples/fav2_slopegraph.png)

The most elegant way to show *change between two points in time*. Aesthetic
choices:

- **Just two anchors** (2023 → 2024) connected by a line: the **slope itself**
  encodes both direction and magnitude of change — almost no ink, maximum
  meaning.
- **Both ends labeled directly** with the region name and value, so there is no
  legend and no y-axis to bounce between.
- **Color encodes the story, not the category**: blue for rising regions,
  orange for falling ones. Blue/orange is colorblind-safe (no red/green), and
  because the lines also physically slope up or down, the message is still
  clear in grayscale.
- **Thin muted lines with solid end-dots** keep it calm; the title carries the
  conclusion.

### How these meet the checklist

| Checklist area | How the charts comply |
| --- | --- |
| **Text** | 6–12 word descriptive title, left-justified upper-left; subtitle for units; direct data labels; all text horizontal; title > subtitle > labels in size |
| **Arrangement** | data sorted into an intentional order; accurate proportions; 2-D only; no gridlines, boxes, or decoration |
| **Color** | intentional palette (not matplotlib defaults); one highlight vs. muted gray; colorblind-safe blue/orange; legible in black & white |

## Other tools in the library

EDA helpers — each takes a DataFrame and returns a plain Python object:

```python
from simple_eda import summarize, missing, numeric_columns, categorical_columns
summarize(df)   # {'rows': 5, 'cols': 4, 'columns': [...], 'dtypes': {...}}
missing(df)     # {'region': 0, 'sales_2023': 0, ...}
```

Bonus source codec (the Python analog of C's `#define`): add
`# coding: simple_eda` to a file's first or second line and any full-width /
Chinese punctuation is rewritten to ASCII *while Python loads the file* (the
file on disk is unchanged). `# coding: thefuck` still works as a legacy alias.

## Development & tests

```bash
pip install -e ".[dev]"
pytest
```

## Publishing (TestPyPI → PyPI)

```bash
python -m build                                       # wheel + sdist into dist/
python -m twine check dist/*                          # validate metadata
python -m twine upload --repository testpypi dist/*   # TestPyPI first
python -m twine upload dist/*                         # then real PyPI
```

Uploading requires a PyPI / TestPyPI account and an API token.
