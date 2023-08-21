#!/usr/bin/python3
''' list all cities fromdb '''

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT a.id, a.name, b.name "
                "FROM cities AS a JOIN states AS b ON a.state_id = b.id "
                "ORDER BY a.id")
    db.close()
    rows = cur.fetchall()
    for row in rows:
        print("{}".format(row))
