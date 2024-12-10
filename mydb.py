import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = '12Tsunoda04!'

	)

# prepare cursor object
cursorObject = dataBase.cursor()

# create database
cursorObject.execute("CREATE DATABASE sadg")

print("Go Sean Go!")