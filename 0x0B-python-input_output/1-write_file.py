#!/usr/bin/python3
"""MODULE FOR WRITE_FILE METHOD"""

def write_file(filename="", text=""):
    """METHOD FOR WRITE A FILE"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
        return len(text)
