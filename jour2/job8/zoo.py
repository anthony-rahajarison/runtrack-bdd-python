import mysql.connector

class Zoo:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "DX?&S@@k#fMQ5",
            database = "zoo"
        )
        self.mycursor = self.mydb.cursor()
    
    def ajouter_animal(self, nom, race, id_cage, date_naissance, pays_origine):
        requete = "INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine) VALUES (%s, %s, %s, %s, %s)"
        valeurs = (nom, race, id_cage, date_naissance, pays_origine)
        self.mycursor.execute(requete, valeurs)
        self.mydb.commit()
        print(f"'{nom}' ajouté avec succès !")

    def supprimer_animal(self, id_animal) :
        requete = "DELETE FROM animal WHERE id = %s"
        self.mycursor.execute(requete, (id_animal,))
        self.mydb.commit()
        print(f"Animal avec l'ID {id_animal} supprimé")
    
    def modifier_id_cage(self, id_animal, id_cage) :
        requete = "UPDATE animal SET id_cage " + str(id_cage) + "WHERE id_animal = " + str(id_animal)
        self.mycursor.execute(requete)
        self.mydb.commit()