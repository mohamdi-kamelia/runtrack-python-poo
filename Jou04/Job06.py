class Vehicule :
    def __init__( self ,marque, modèle , année , prix ):
        self.marque = marque
        self.modèle = modèle
        self.année = année 
        self.prix = prix
        
    def informationsVehicule (self):
        print("La marque de vehicule est :" , self.marque)
        print("le modèle de vehicule est :" , self.modèle)
        print("l'année de vehicule est :" , self.année)
        print("Le prix de vehicule :" , self.prix)
    
    def demarrer (self):
        print("Attention, je roule !!")
class Voiture(Vehicule) :
    def __init__ ( self , marque, modèle , année , prix , portes = 4):
        Vehicule.__init__(self , marque, modèle , année , prix )
        self.portes = portes 
    def informationsVehicule(self):
        Vehicule.informationsVehicule(self)
        print("Nombre de portes de la voiture est :" , self.portes)
    def demarrer(self):
        print("La Voiture  démarre !!!")

voiture = Voiture("Mercedes", "G class ", 2024, 153150)
voiture.informationsVehicule()  
voiture.demarrer() 

class Moto (Vehicule) :
    def __init__(self , marque, modèle , année , prix ):
        Vehicule.__init__(self , marque, modèle , année , prix ) 
        self.roue = 2
    def informationsVehicule(self):
        Vehicule.informationsVehicule(self)
        print("Nombre de roue est :" , self.roue)
    def demarrer(self):
        print("La Moto démarre !!!")

moto = Moto("Yamaha", "1200 Vmax ", 1987 , 4500)
moto.informationsVehicule()
moto.demarrer()
                  