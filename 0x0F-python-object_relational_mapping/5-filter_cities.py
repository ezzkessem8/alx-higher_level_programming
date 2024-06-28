#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all cities of that state,
using the database hbtn_0e_4_usa.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} username password database state_name".format(sys.argv[0]))
        sys.exit(1)

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

    # Get state name from command-line argument
    state_name = sys.argv[4]

    # Execute query to select cities of the specified state
    cur.execute("SELECT cities.name FROM cities \
                JOIN states ON cities.state_id = states.id \
                WHERE states.name = %s ORDER BY cities.id ASC", (state_name,))

    # Fetch all results
    rows = cur.fetchall()

    # Extract city names from rows
    cities = [row[0] for row in rows]

    # Print city names separated by commas
    print(", ".join(cities))

    # Close cursor and database connection
    cur.close()
    db.close()

