#!/usr/bin/python3
"""MODULE FOR WRITE_FILE METHOD"""

for write_file(filename="", text=""):
    """METHOD FOR WRITE A FILE"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
