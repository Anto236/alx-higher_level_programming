#!/usr/bin/python3
""" Script that lists state based on argument passed"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states where name='{}'".format(argv[4]))
    result = cursor.fetchall()
    for row in result:
        print(row)

    cursor.close()
    db.close()
