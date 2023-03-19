#!/usr/bin/python3
"""
Lists all cities of a given state from the database hbtn_0e_4_usa
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

    # Prepare SQL query
    sql = "SELECT cities.name FROM cities \
           JOIN states ON cities.state_id = states.id \
           WHERE states.name = %s ORDER BY cities.id ASC"

    # Execute SQL query with user input as parameter
    cursor.execute(sql, (sys.argv[4],))

    # Fetch all the matching rows
    rows = cursor.fetchall()

    # Print rows
    print(", ".join(city[0] for city in rows))

    # Close cursor and database connection
    cursor.close()
    db.close()
