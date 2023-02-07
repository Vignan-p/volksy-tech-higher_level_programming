#!/usr/bin/python3
"""SELECT command"""


def sql_cmd(args):
    """Connect to DATABASE"""
    db = MySQLdb.connect(host='localhost', 
           port=3306, 
           user=args[0], 
           passwd=args[1], 
           db=args[2])
    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY id ASC")
    for i in c:
        print(i)
    c.close()
    db.close()


if __name__ == "__main__":
    import MySQLdb
    import sys
    sql_cmd(sys.argv[1:])
