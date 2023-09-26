#!/usr/bin/python3
"""
This script takes an argument and retrieves
all records in the states table where the `name` matches
the provided argument from the database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Establish a connection to the database and fetch the states
    based on the provided argument.
    """

    
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()

    cur.execute("SELECT * FROM states \
                 WHERE name LIKE BINARY '{}' \
                 ORDER BY states.id ASC".format(argv[4]))
    rows = cur.fetchall()

    
    for row in rows:
        print(row)

