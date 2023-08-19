#!/usr/bin/python3
#list all states from mysql database

import MySQLdb
import sys import argv

if __name__ = "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM 'states'")
    [print(state) for state in c.fetchall()]
