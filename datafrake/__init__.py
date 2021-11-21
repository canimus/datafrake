import re
import pandas as pd
from pandas.core.frame import DataFrame
from collections import OrderedDict
from operator import methodcaller
import faker
from fn import _
from fn.op import F

FK = OrderedDict({
    "fn" : "first_name",
    "ln" : "last_name",
    "em" : "email"
})

def _faker(key: str, data_source) -> str:
    return methodcaller(FK[key])(data_source)

def _rows_and_locale(code: str) -> tuple:
    return re.compile(r"^#(\d+)/?([a-z]{2})?").match(code).groups()

def _column_generator(code: str, rows: int) -> dict:
    return tuple([])

def datafrake(code: str) -> DataFrame:
    assert code, "Please provide a valid datafrake syntax"
    assert len(code) >= 2, "Dataframe expression is incomplete"
    tokens = code.split()

    dataset_token = tokens[0]
    column_tokens = tokens[1:]

    rows, locale = _rows_and_locale(dataset_token)
    source = faker.Faker(locale) if locale else faker.Faker("en")

    assert str(rows).isdigit(), "First token should be a number prefixed by #"
    assert all([column in FK.keys() for column in column_tokens]), "Unrecognized datafrake tokens"

    # Each key should return a dataframe

    # Concatenate the columns
    records = {
        FK[key]:[_faker(key, source) for _ in range(int(rows))] 
        for key in column_tokens
    }


    return pd.DataFrame(records)