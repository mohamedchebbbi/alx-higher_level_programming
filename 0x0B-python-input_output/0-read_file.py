#!/usr/bin/python3
""" MODULE FOR READ8FILE"""


def read_file(filename=""):
    """METHOD FOR READ FROM FILE"""
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()
        print(text, end="")
