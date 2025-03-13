import mysql.connector



class Employe:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "DX?&S@@k#fMQ5",
            database = "entreprise"
        )
        self.mycursor = self.mydb.cursor()
    
    def creer_employe(self, nom, prenom, salaire, id_service) :
        """Crée un nouvel employé et l'ajoute à la base de donnée"""
        requete = "INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        valeurs = (nom, prenom, salaire, id_service)
        self.mycursor.execute(requete, valeurs)
        self.mydb.commit()
        print(f"{prenom} {nom} ajouté")
    
    def afficher_employe(self) :
        """Affiche en console tous les employés et leurs informations"""
        self.mycursor.execute("SELECT employe.nom, employe.prenom, employe.salaire, service.nom, employe.id FROM employe JOIN service ON employe.id_service = service.id ORDER BY employe.id;")
        resultat = self.mycursor.fetchall()
        for ligne in resultat:
            print(f"{ligne[4]}. {ligne[1]} {ligne[0]} : {ligne[2]} $ ({ligne[3]})")

    
    def supprimer_employe(self, employe_id) :
        """Supprime un employé de la base de donnée"""
        requete = "DELETE FROM employe WHERE id = " + str(employe_id)
        self.mycursor.execute(requete)
        self.mydb.commit()
        print(f"Employé numéro {employe_id} supprimé")
    
    def changer_employe_id(self, ancien_id, nouveau_id) :
        """Change l'id d'un employe"""
        requete = "UPDATE employe SET id = " + str(nouveau_id) + " WHERE id = " + str(ancien_id)
        self.mycursor.execute(requete)
        self.mydb.commit()

db = Employe()
db.afficher_employe()

# db.creer_employe('Long', 'Steve', 3100.00, 1)
# db.supprimer_employe(14)
# db.changer_employe_id(17, 5)

db.afficher_employe()