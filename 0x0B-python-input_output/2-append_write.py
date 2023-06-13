#!/usr/bin/python3
"""MODULE FOR APPEND_WRITE METHOD"""

def append_write(filename="", text=""):
    """Method for reading lines from file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
