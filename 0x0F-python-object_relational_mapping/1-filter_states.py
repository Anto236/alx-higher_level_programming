#!/usr/bin/python3
""" Script that lists states starting with letter N from specified database"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM states where name REGEXP '^[N].*$' \
                     ORDER BY id ASC""")
    result = cursor.fetchall()
    for row in result:
        print(row)

    cursor.close()
    db.close()
