#!/usr/bin/env python3
"""logging module"""
import re
from typing import List
import logging


PII_FIELDS = ("name", "email", "ssn", "password", "ip")


def filter_datum(fields: List[str],
                 redaction: str, message: str, separator: str) -> str:
    """filter function"""
    for i in fields:
        message = re.sub(f"(?<={i}=)(.*?)(?={separator})", redaction, message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """format method"""
        record.msg = filter_datum(self.fields,
                                  self.REDACTION, record.msg, self.SEPARATOR)
        return super().format(record)


def get_logger() -> logging.Logger:
    """get logger function"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    stream = logging.StreamHandler()
    stream.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    logger.addHandler(stream)
    return logger
