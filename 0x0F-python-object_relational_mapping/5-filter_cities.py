#!/usr/bin/python3
"""
a script that takes in the name of a state as an\
argument and lists all cities of that state,\
using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],passwd=sys.argv[2],db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM\
                    cities INNER JOIN states ON cities.state_id = states.id\
                    WHERE states.name = %s"
                    ,(sys.argv[4],))
    cities = cursor.fetchall()
    print(", ".join([city[1] for city in cities]))
    cursor.close()
    db.close()

