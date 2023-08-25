#!/usr/bin/python3
"""
Script that takes argument and display values 
in states table where name mathches argument
but safe from sql injection
"""

import MySQLdb
from sys import argv

# The code should not be excuted when imported
if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name = %s", argv[4])

    rows = cur.fetchall()
    for i in rows:
        print(i)
    cur.close()
    db.close()
