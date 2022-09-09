from sqlglot import exp
from sqlglot.dialects.dialect import (
    Dialect
)
from sqlglot.generator import Generator
from sqlglot.parser import Parser
from sqlglot.tokens import Tokenizer, TokenType


class SQLServer(Dialect):
    class Tokenizer(Tokenizer):
        KEYWORDS = {
            **Tokenizer.KEYWORDS,
            "TOP": TokenType.TOP,
        }

    class Parser(Parser):
        FUNCTIONS = {**Parser.FUNCTIONS, "TO_TIMESTAMP": exp.StrToTime.from_arg_list}

    class Generator(Generator):
        IDENTIFIERS = [("[", "]")]