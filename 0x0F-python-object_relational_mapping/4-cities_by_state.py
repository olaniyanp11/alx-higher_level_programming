#!/usr/bin/python3
""" a script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__  ==  "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM cities")
    cities = cur.fetchall()
    for city in cities:
        print(city)
    cur.close()
    db.close()

