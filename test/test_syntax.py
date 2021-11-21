from pandas.core.frame import DataFrame
from datafrake import datafrake

def test_dataframe_rows():
    df = datafrake("#100 fn ln em")
    assert isinstance(df, DataFrame)
    assert df.shape[0] == 100
    assert df.shape[1] == 3
    assert set(df.columns) == set(["first_name", "last_name", "email"])

def test_dataframe_with_locale():
    df = datafrake("#20/nl fn ln")
    assert isinstance(df, DataFrame)
    assert df.shape[0] == 20
    assert df.shape[1] == 2
    assert set(df.columns) == set(["first_name", "last_name"])