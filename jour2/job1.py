import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "DX?&S@@k#fMQ5"
)

mycursor = mydb.cursor()

mycursor.execute("USE laplateforme")
mycursor.execute("SELECT * FROM etudiant")

for x in mycursor :
    print(x)