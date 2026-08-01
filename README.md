# simple-eda-yzheng74

A tiny **visualization + EDA** library for pandas DataFrames (MSDS610). Every
chart follows the Evergreen & Emery *Data Visualization Checklist* by default:
a descriptive title, data labeled directly, an intentional order, and a
colorblind-safe palette that stays legible in black & white.

- **Install name** (pip): `simple-eda-yzheng74`
- **Import name** (Python): `simple_eda`

## Install

```bash
pip install simple-eda-yzheng74
```

## Visualizations

Each function takes a DataFrame plus the column names to plot, and returns a
Matplotlib `Axes` you can save or tweak.

```python
import pandas as pd
from simple_eda import bar, lollipop, slopegraph

df = pd.DataFrame({
    "region": ["North", "South", "East", "West", "Central"],
    "sales_2023": [120, 200, 90, 160, 75],
    "sales_2024": [145, 190, 130, 175, 60],
    "stores": [8, 14, 6, 11, 5],
})
```

### `bar` — horizontal bar chart

Ranks categories; pass `highlight` to color one bar.

```python
ax = bar(df, "region", "sales_2024",
         title="West and North lead 2024 regional coffee sales",
         subtitle="Net sales by region (thousands USD)",
         highlight="West")
ax.figure.savefig("bar.png", dpi=150)
```

### `lollipop` — lollipop chart

A lighter-ink alternative to bars.

```python
ax = lollipop(df, "region", "stores",
              title="South operates the most stores",
              highlight="South")
ax.figure.savefig("lollipop.png", dpi=150)
```

### `slopegraph` — before/after slopegraph

Shows change between two columns; rising lines are blue, falling ones orange.

```python
ax = slopegraph(df, "region", "sales_2023", "sales_2024",
                title="East surged while Central slipped, 2023 to 2024",
                start_label="2023", end_label="2024")
ax.figure.savefig("slopegraph.png", dpi=150)
```

## EDA helpers

Each takes a DataFrame and returns a plain Python object (dict or list).

```python
from simple_eda import summarize, missing, numeric_columns, categorical_columns

summarize(df)            # {'rows': 5, 'cols': 4, 'columns': [...], 'dtypes': {...}}
missing(df)              # {'region': 0, 'sales_2023': 0, ...}
numeric_columns(df)      # ['sales_2023', 'sales_2024', 'stores']
categorical_columns(df)  # ['region']
```