#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create cursor
    cur = db.cursor()

    # Execute query to select all states and order by id
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all results
    rows = cur.fetchall()

    # Print results
    for row in rows:
        print(row)

    # Close cursor and database connection
    cur.close()
    db.close()

