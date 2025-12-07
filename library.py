import mysql.connector
import functions

#Connects code to MySQL
libdb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="libpassword!",
    database = "library"
)

cursor = libdb.cursor()
rflag = False
lflag = False

functions.init(cursor, libdb)

functions.Welcome_Screen()
