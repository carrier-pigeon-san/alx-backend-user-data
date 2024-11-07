#!/usr/bin/env python3
""""""
import re
from re import sub
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """returns a log message obfuscated"""
    pattern = r'\b(' + '|'.join(fields) + r')=[^' + separator + ']+'
    replace = r'\1=' + redaction
    return re.sub(pattern, replace, message)
