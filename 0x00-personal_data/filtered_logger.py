#!/usr/bin/env python3
""" A modulle that implements various logging functionalities """
import logging
import re
from re import sub
from typing import List

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """returns a log message obfuscated"""
    field_values = r'[^' + re.escape(separator) + ']+'
    pattern = r'\b(' + '|'.join(map(re.escape, fields)) + r')=' + field_values
    replace = r'\1=' + redaction
    return re.sub(pattern, replace, message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Constructor method """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Filters values in incoming log records using filter_datum function
        """
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)

def get_logger(self) -> logging.Logger:
    """ Returns a logger object """
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)
    return logger
