#!/usr/bin/python3
"""
A script that takes in the name of a state as an argument
and lists all cities of that state, using the database
hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == '__main__':
    conn = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306,
        host='localhost')

    pointer = conn.cursor()
    pointer.execute(
        'SELECT cities.name FROM cities\
        INNER JOIN states ON cities.state_id = states.id\
        WHERE states.name = %s \
        ORDER BY cities.id ASC', (sys.argv[4], ))

    totalCities = pointer.fetchall()

    index = 0
    for city in totalCities:
        if index != 0:
            print(", ", end="")
        print("%s" % city, end="")
        index += 1
    print("")

    pointer.close()
    conn.close()
