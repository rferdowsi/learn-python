# WIP
import pymysql

con = pymysql.connect('localhost', 'root', 'r00t', 'mytest')

with con:
    cur = con.cursor()
    cur.execute("SELECT VERSION()")

    version = cur.fetchone()
    
    print("Database version: {}".format(version[0]))
