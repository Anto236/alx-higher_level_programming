#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa
where name matches the argument
"""

import MySQLdb
import sys

if __name__ == '__main__':
    # Connect to database
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)
    # Create cursor
    cursor = db.cursor()

    # Create SQL query using user input
    sql = "SELECT * FROM states WHERE \
           CONVERT(`name` USING Latin1) \
           COLLATE Latin1_General_CS = '{}';".format(sys.argv[4])

    # Execute SQL query
    cursor.execute(sql)

    # Fetch all the matching rows
    rows = cursor.fetchall()

    # Print rows
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
