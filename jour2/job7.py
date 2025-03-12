import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "DX?&S@@k#fMQ5",
    database = "entreprise"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM employe WHERE salaire > 3000")
result = mycursor.fetchall()
for x in result :
    print(x)

mycursor.execute("""SELECT employe.nom, employe.prenom, employe.salaire, service.nom AS service
    FROM employe
    JOIN service ON employe.id_service = service.id;
""")

result = mycursor.fetchall()

for ligne in result:
    print(f"Nom: {ligne[0]}, Prénom: {ligne[1]}, Salaire: {ligne[2]}, Service: {ligne[3]}")