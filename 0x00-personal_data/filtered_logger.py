#!/usr/bin/env python3
"""logging module"""
import re
import os
from typing import List
import logging
import mysql.connector


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


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
    logger.addHandler(stream.setFormatter(RedactingFormatter(PII_FIELDS)))
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """connect to database"""
    host = os.environ.get('PERSONAL_DATA_DB_HOST', "localhost")
    user = os.environ.get('PERSONAL_DATA_DB_USERNAME', "root")
    password = os.environ.get('PERSONAL_DATA_DB_PASSWORD', "")
    database = os.environ.get('PERSONAL_DATA_DB_NAME')
    connection = mysql.connector.connection.MySQLConnection(
      host=host, user=user, password=password, database=database)
    return connection
