
from datetime import date
class CompteBancaire:
    cmp = 1000
    def __init__(self,client,typecompte,sold=0):
      
        CompteBancaire.cmp +=1
        self.numéro_compte = CompteBancaire.cmp
        self.__sold = sold
        self.proprietaire = client
        self.historique_transactions = []
        self.type = typecompte
        self.decouvret_autorise = 0

    def gestiontypecompte(self):
        if self.type == "CompteCourant":
            self.decouvret_autorise = -500
        elif self.type == "CompteEpargne":
            self.decouvret_autorise = 0
    @property
    def deposer(self):
        return self.__sold
    
    @deposer.setter
    def deposer(self,montant):
        if self.type == "CompteCourant":
            if montant > 0 :
                if self.decouvret_autorise == -500:
                    self.__sold += montant
                    self.historique_transactions.append({"date": str(date.today()), "type": "dépôt", "montant": montant, "solde_après": self.__sold})
                    print("ok")
                else:
                    x = 0
                    if self.decouvret_autorise != -500:
                        x = (-500) - (self.decouvret_autorise)
                        if montant <= abs(x):
                            self.decouvret_autorise -= montant
                        else:
                            h = 0
                            h = montant - abs(x) 
                            self.decouvret_autorise = self.decouvret_autorise + x
                            self.__sold = self.__sold + h
                        self.historique_transactions.append({"date": str(date.today()), "type": "dépôt", "montant": montant, "solde_après": self.__sold,"decouvret autorise" : self.decouvret_autorise})
                        print("ok")
        elif self.type == "CompteEpargne":
            self.__sold += montant
            self.historique_transactions.append({"date": str(date.today()), "type": "dépôt", "montant": montant, "solde_après": self.__sold,"decouvret autorise" : self.decouvret_autorise})
    @property
    def retirer(self):
        return self.__sold
    @retirer.setter
    def retirer(self,montant):
        if self.type == "CompteEpargne":
            if self.__sold >= montant :
                self.__sold -= montant
                self.historique_transactions.append({"date": str(date.today()), "type": "retirer", "montant": montant, "solde_après": self.__sold,"decouvret autorise" : self.decouvret_autorise})
        else:
            if self.type == "CompteCourant" :
                if self.__sold + abs(self.decouvret_autorise) >= montant:
                    x = 0
                    y = 0
                    if self.__sold >= montant:
                        self.__sold -= montant
                        self.historique_transactions.append({"date": str(date.today()), "type": "retirer", "montant": montant, "solde_après": self.__sold,"decouvret autorise" : self.decouvret_autorise})
                    elif self.__sold <= montant :
                        x = montant - self.__sold 
                        y = montant - x 
                        self.__sold = self.__sold - y
                        self.decouvret_autorise = self.decouvret_autorise + x
                        self.historique_transactions.append({"date": str(date.today()), "type": "retirer", "montant": montant, "solde_après": self.__sold,"decouvret autorise" : self.decouvret_autorise})
                else:
                    print("error sold")



    def appliquer_interets(self):
        pass


    def historiquetransaction(self):
        return self.historique_transactions





    def __str__(self):
        return f"proprietaire : { self.proprietaire} \n numéro_compte : {self.numéro_compte} \n sold : {self.__sold} \n decouvret autorise : {self.decouvret_autorise} "
    def to_json(self):
        return {
            "numéro_compte" : self.numéro_compte,
            "__sold" : self.__sold,
            "historique_transactions" : self.historique_transactions,
            "type" : self.type,
            "decouvret_autorise" : self.decouvret_autorise

        }
    @classmethod
    def from_json(cls,data,client):
        compte = CompteBancaire(client,data["type"],data["__sold"])
        compte.numéro_compte = data["numéro_compte"]
        compte.historique_transactions = data["historique_transactions"]
        compte.decouvret_autorise = data["decouvret_autorise"]
        return compte