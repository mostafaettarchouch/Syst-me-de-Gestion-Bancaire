from client import Client
from comptebancaire import CompteBancaire
import json
import os
class Banque:
    def __init__(self):
        self.clients = []
        self.comptes = []
        self.load()

    def save(self):
        data1 = []
        data2 = []
        client = {}
        for c in self.clients:
            data1.append(c.to_json())
        client["client"] = data1
        for cp in self.comptes:
            data2.append(cp.to_json())
        client["compte"] = data2

        with open("data.json","w") as file:
            json.dump(client,file)



    def load(self):
        if os.path.exists("data.json") == False:
            return
        
        with open("data.json","r") as file:
            data = json.load(file)
        
        listcliant = data["client"]
        listcompte = data["compte"]
        for client in listcliant :
            self.clients.append(Client.from_json(client))
            for compte in listcompte:
                self.comptes.append(CompteBancaire.from_json(compte,Client.from_json(client)))

    def ajouterclient(self,client):
        if isinstance(client,Client):
            self.clients.append(client)
            self.save()
            

    def ajoutercompte(self,compte):
        if isinstance(compte,CompteBancaire):
            self.comptes.append(compte)
            self.save()

    def trouver_client(self,id):
        for client in  self.clients :
            if client.id_client == id :
                print(client)
    def trouver_compte(self,id):
        for compte in  self.comptes :
            if compte.numéro_compte == id :
                print(compte)
    def afficherclient(self):
        
        for c in  self.clients:
            print(c)


    def affichercompte(self):
        
        
        for c in  self.comptes:
            print(c)
    
    def removecompte(self,compte):
        self.comptes.remove(compte)
        print ("remove")
        self.save()
        
        
    
