#!/usr/bin/python3
'''list all states from mysql database'''

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
            passwd=argv[2], db=argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute('SELECT * FROM states ORDER BY id ASC')
    for rows in cur.fetchall():
        print(rows)
    cur.close()
    db.close()
