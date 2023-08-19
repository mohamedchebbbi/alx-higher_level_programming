#!/usr/bin/python3
# list state from datatbase
# syntax: ./0-select_states.py user passwd db_name
import sys
import MySQLdb

if __name__ = "__main__":
    db = MySQLdb.connect(user=sys.argv[1],passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states")
    [print(state) for state in c.fetchall()]
