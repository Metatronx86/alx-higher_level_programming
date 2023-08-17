#!/usr/bin/python3
"""
This script takes in an argument and retrieves records
from the states table where the `name` matches the argument,
displaying the retrieved values. This is done using a secure
method to prevent MySQL injections.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    with db.cursor() as cur:
        '''
        Execute a parameterized query to prevent SQL injection
        '''
        cur.execute("""
            SELECT
                *
            FROM
                states
            WHERE
                name LIKE BINARY %(name)s
            ORDER BY
                states.id ASC
        """, {
            'name': argv[4]
        })

        
        rows = cur.fetchall()

    
    if rows is not None:
        for row in rows:
            print(row)

