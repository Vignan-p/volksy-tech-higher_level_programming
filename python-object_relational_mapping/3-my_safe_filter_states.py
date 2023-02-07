#!/usr/bin/python3
"""SQL Injection"""


import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    sql = "SELECT * FROM `states` WHERE name = '%s'"
    val = (sys.argv[4], )
    c.execute(sql, val)
    for i in c:
        print(i)
