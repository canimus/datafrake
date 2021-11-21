from modgrammar import LITERAL, Grammar, WORD, OR, OPTIONAL, REPEAT, WHITESPACE
import pycountry
from datafrake import FK, TK

class ManyOperator (Grammar):
    """Functor for number of rows in dataset"""
    grammar = (LITERAL("#"))

class LocaleOperator(Grammar):
    """Functor for locale in dataset or column """
    grammar = (LITERAL("/"))

class RangeOperator(Grammar):
    """Functor for start and end values"""
    grammar = (LITERAL(":"))

class Country(Grammar):
    grammar = (OR(*[LITERAL(c.alpha_2.lower()) for c in pycountry.countries ]))

class Number (Grammar):
    grammar = (WORD("0-9"))

class Dimension(Grammar):
    grammar = (ManyOperator, Number)

class DataTypeOperator(Grammar):
    grammar = (OPTIONAL(Dimension), LITERAL("_"), WORD("sifdt", greedy=False))

class PrefixOperator(Grammar):
    grammar = (LITERAL("<"))

class SuffixOperator(Grammar):
    grammar = (LITERAL(">"))

class RenameOperator(Grammar):
    grammar = ((PrefixOperator | SuffixOperator), WORD("a-z_"))

class FakerFunction(Grammar):
    """Maps a two-character function map to Faker default provider"""
    grammar = (
        OPTIONAL(Dimension),
        OR(OR(*[LITERAL(f.lower()) for f in list(FK.keys())]), DataTypeOperator),
        OPTIONAL(RenameOperator)
        )

class Dataset(Grammar):
    grammar = (Dimension, OPTIONAL(LocaleOperator, Country))

class DataFrake(Grammar):
    """A dataframe fake data generator"""
    grammar = (Dataset, WHITESPACE, REPEAT(WHITESPACE | FakerFunction))

# Test
#DataFrake.parser().parse_string("#100/es fn ln").find_all(FakerFunction)