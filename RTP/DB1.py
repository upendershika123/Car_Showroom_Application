import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="")
cur=mydb.cursor()
cur.execute("CREATE DATABASE DB1")
print("database created")
