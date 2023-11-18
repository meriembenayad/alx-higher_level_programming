#!/usr/bin/python3
"""
   script that takes in an argument and displays all values
   in the states table of hbtn_0e_0_usa
   where name matches the argument.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )

    cur = conn.cursor()
    user_input = sys.argv[4]
    query_sql = "SELECT * FROM states WHERE name LIKE BINARY '{}'\
        ORDER BY id ASC".format(
        user_input)
    cur.execute(query_sql)

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()
