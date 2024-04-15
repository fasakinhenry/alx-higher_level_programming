#!/usr/bin/python3
"""
A script that takes in an argument and displays all values
in the statestable of hbtn_0e_0_usa where name matches
the argument.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    pointer = conn.cursor()
    pointer.execute("""SELECT * FROM states
                WHERE name LIKE BINARY '{}'
                ORDER BY states.id ASC""".format(sys.argv[4]).strip("'"))
    [print(state) for state in pointer.fetchall()]
