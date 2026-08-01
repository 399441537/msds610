from simple_eda import load_sample


def test_load_sample_columns_and_shape():
    df = load_sample()
    assert list(df.columns) == ["region", "sales_2023", "sales_2024", "stores"]
    assert len(df) == 5


def test_load_sample_returns_fresh_copy():
    a = load_sample()
    a.loc[0, "sales_2024"] = -999
    b = load_sample()
    assert b.loc[0, "sales_2024"] != -999
