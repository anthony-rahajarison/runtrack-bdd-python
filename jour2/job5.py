import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "DX?&S@@k#fMQ5",
    database = "laplateforme"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT CONCAT('La superficie de La Plateforme est de ', SUM(superficie), ' m2') FROM etage;")
result = mycursor.fetchall()

# On extrait le résultat de la liste puis du tuple
string = result[0][0]

# On affiche le résultat
print(string)