#!/usr/bin/python3
''' list all states where name matche argumentfrom database '''

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name = %s ORDER BY id",
                (argv[4],))
    db.close()
    rows = cur.fetchall()
    for row in rows:
        print("{}".format(row))
