import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "DX?&S@@k#fMQ5",
    database = "laplateforme"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT nom, capacite FROM salle")
result = mycursor.fetchall()


print(result)