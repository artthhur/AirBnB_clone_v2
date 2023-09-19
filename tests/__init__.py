#!/usr/bin/python
"""This module contains functions used in test methods"""

from typing import TextIO


def clear_output(stream: TextIO):
    """ function clears the contents of the giving stream
    Args:
        stream: the stream to be cleared
    """
    stream.seek(0)
    stream.truncate(0)
