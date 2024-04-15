#!/usr/bin/python3
"""
A script that takes in arguments and displays all values
in the states table of hbtn_0e_0_usa
where name matches the argument.But this time,
write one that is safe from MySQL injections!
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
    pointer.execute('SELECT * from states WHERE name = %s ORDER BY states.id',
                    (sys.argv[4], ))

    allStates = pointer.fetchall()
    for state in allStates:
        print(state)

    pointer.close()
    conn.close()
