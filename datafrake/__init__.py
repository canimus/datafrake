import re
import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame
from operator import methodcaller
from faker import Faker
from fn import _
from fn.op import F
from modgrammar import ParseError
from collections import OrderedDict

FK = OrderedDict({
    "fn" : "first_name",
    "ln" : "last_name",
    "em" : "email"
})

TK = OrderedDict({
    "i" : "integer",
    "s" : "string",
    "f" : "double",
    "d" : "date",
    "t" : "timestamp"
})

import datafrake.grammar as G

def _vector(source: Faker, fn: str, rows: int) -> DataFrame:
    return pd.DataFrame({fn: np.arange(rows)})

def datafrake(code: str) -> DataFrame:
    try:    
        result = G.DataFrake.parser().parse_string(code)
        dataset = result.find(G.Dataset)
        rows = int(dataset.find(G.Number).string)
        country = dataset.find(G.Country)
        country = country.string if country else "en"
        source = Faker(country)
        return pd.concat([_vector(source, fn, rows) for fn in dataset.find(G.FakerFunction)])
    except ParseError as e:
        print(str(e))
    