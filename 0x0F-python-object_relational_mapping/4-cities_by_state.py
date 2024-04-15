#!/usr/bin/python3
"""
A script that lists all cities from the database hbtn_0e_4_usa
"""

import sys
import MySQLdb

if __name__ == '__main__':
    conn = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306,
        host='localhost')

    pointer = conn.cursor()
    pointer.execute(
        'SELECT cities.id, cities.name, states.name FROM cities JOIN states ON\
        cities.state_id = states.id;')

    allStates = pointer.fetchall()

    for state in allStates:
        print(state)
