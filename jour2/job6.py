import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "DX?&S@@k#fMQ5",
    database = "laplateforme"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT CONCAT('La capacité de toutes les salles est de : ', SUM(capacite)) FROM salle;")
result = mycursor.fetchall()

# On extrait le résultat de la liste puis du tuple
string = result[0][0]

# On affiche le résultat
print(string)