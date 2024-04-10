#!/usr/bin/env python3
"""logging module"""
import re
from typing import List


def filter_datum(fields: List[str],
                 redaction: str, message: str, separator: str) -> str:
    """filter function"""
    for i in fields:
        message = re.sub(f"(?<={i}=)(.*?)(?={separator})", redaction, message)
    return message
