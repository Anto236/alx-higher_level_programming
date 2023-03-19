#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa
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

    # Execute SQL query to fetch all cities
    cursor.execute("SELECT * FROM cities ORDER BY id ASC")

    # Fetch all the matching rows
    rows = cursor.fetchall()

    # Print rows
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
