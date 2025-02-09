from datetime import date
from comptebancaire import CompteBancaire

class Client:
    cmp = 1000
    def __init__(self,nom,prenom):
        Client.cmp += 1
        self.id_client = Client.cmp
        self.nom = nom
        self.prenom = prenom
        self.date_inscription = date.today()
        self.comptes_bancaires = []
    def Liercomptesbancaires(self,compte):
        if isinstance (compte,CompteBancaire):
            if compte not in self.comptes_bancaires:
                self.comptes_bancaires.append(compte.numéro_compte)
        
    def dissociercomptesbancaires(self,compte):
        if isinstance (compte,CompteBancaire):
            if compte in self.comptes_bancaires:
                self.comptes_bancaires.remove(compte.numéro_compte)
        
    def __str__(self):
        return f" Nom : {self.nom} \t Prénom : {self.prenom} \t date inscription : {self.date_inscription} \n comptes bancaires : {self.comptes_bancaires}  "
    
    def to_json(self):
        return{
            "id_client" : self.id_client ,
            "nom" : self.nom ,
            "prenom" : self.prenom,
            "date_inscription" : str(self.date_inscription),
            "comptes_bancaires" : self.comptes_bancaires
        }
    @classmethod
    def from_json(cls,data):
        client = Client(data["nom"],data["prenom"])
        client.id_client = data["id_client"]
        client.date_inscription = data["date_inscription"]
        client.comptes_bancaires = data["comptes_bancaires"]
        return client




