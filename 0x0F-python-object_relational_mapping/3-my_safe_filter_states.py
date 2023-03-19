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

    # Create SQL query using placeholders
    sql = "SELECT * FROM states WHERE name=%s ORDER BY id ASC"

    # Execute SQL query with safe parameters
    cursor.execute(sql, (sys.argv[4],))

    # Fetch all the matching rows
    rows = cursor.fetchall()

    # Print rows
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
