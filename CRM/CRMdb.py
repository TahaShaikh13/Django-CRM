import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '20082006',

)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE CRMdb")
