#!/usr/bin/python3
"""
A script that lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == '__main__':
    conn = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306,
        host='localhost'
    )

    pointer = conn.cursor()
    pointer.execute("SELECT * \
                    FROM states \
                    WHERE CONVERT(`name` USING Latin1) \
                    COLLATE Latin1_General_CS \
                    LIKE 'N%';")
    allStates = pointer.fetchall()
    for state in allStates:
        print(state)
    pointer.close()
    conn.close()
