from client import Client
from comptebancaire import CompteBancaire
from banque import Banque

class App :
    bank = Banque()
    def ajoutercompte(self):
        nom = str(input("Nom : "))
        prenom  = str(input("Prénom : "))
        client = Client(nom,prenom)
        typecompte = "CompteCourant"
        
        sold = float(input("solde : "))
        App.bank.ajouterclient(client)


        compte = CompteBancaire(client,typecompte,sold)
        if typecompte == "CompteCourant":
            compte.decouvret_autorise = -500
        elif self.type == "CompteEpargne":
            compte.decouvret_autorise = 0

        App.bank.ajoutercompte(compte)
        client.Liercomptesbancaires(compte)
        
    def affichercompte(self):
        App.bank.affichercompte()
    def deposer(self):
        App.bank.affichercompte()
        n = int(input("numéro_compte : "))
        for c in App.bank.comptes:
            if c.numéro_compte == n:
                App.bank.removecompte(c)
                sol = float(input("sold ajouter : " ))
                c.deposer = sol
                App.bank.ajoutercompte(c)
    def retirer(self):
        App.bank.affichercompte()
        n = int(input("numéro_compte : "))
        for c in App.bank.comptes:
            if c.numéro_compte == n:
                App.bank.removecompte(c)
                sol = float(input("retirer sold : " ))
                c.retirer = sol
                App.bank.ajoutercompte(c)
    def historiquetransaction(self):
        App.bank.affichercompte()
        n = int(input("numéro_compte : "))
        for c in App.bank.comptes:
            if c.numéro_compte == n:
                print(c.historiquetransaction())


    def menu(self):
        while True:
            print("1 ajouter compte ")
            print("2 afficher compte")
            print("3 deposer ")
            print("4 retirer ")
            print("5 historique transaction ")
            print("6 trouver_compte ")
            print("7 break")
            choix = int (input("choix : "))
            match choix :
                case 1 : self.ajoutercompte()
                case 2 : self.affichercompte()
                case 3 : self.deposer()
                case 4 : self.retirer()
                case 5 : self.historiquetransaction()
                case 6 : pass
                case 7 : break

test = App()
test.menu()
                
            