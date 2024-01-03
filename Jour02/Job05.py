class Voiture :
    def __init__ (self , marque , modèle , année , kilométrage ):
        self.__marque = marque
        self.__modèle = modèle
        self.__année = année
        self.__kilométrage = kilométrage
        self.__en_marche = False
        self.__reservoir = 60
    def get_marque(self):
        return self.__marque 
    def get_modèle(self):
        return self.__modèle
    def get_année(self):
        return self.__année
    def get_kilométrage(self):
        return self.__kilométrage
    def get_en_marche(self):
        return self.__en_marche

    def set_marque(self , nouvelle_marque):
        self.__marque = nouvelle_marque
    def set_modèle(self , nouvelle_modèle):
        self.__modèle = nouvelle_modèle
    def set_année(self , nouvelle_année):
        self.__année = nouvelle_année
    def set_kilométrage(self , nouveau_kilométrage):
        self.__kilométrage = nouveau_kilométrage
    
    def __verifier_plein(self):
        return self.__reservoir > 5
    def demarer(self):
        if self.__verifier_plein():
            self.__en_marche = True
            print("démarrage de la voiture")
        else:
            print("la voiture peur pas démarrer")
    def arreter(self):
        self.__en_marche = False
        print("voiture arretée")
    
voiture_1 = Voiture(marque="Mecedes", modèle="G classe", année=2020, kilométrage=15000)

print("La marque de la voiture est :" , voiture_1.get_marque())
print("Le modèle de la voiture est : " , voiture_1.get_modèle())
print("L'année de la voiture :" ,voiture_1.get_année())
print("Le Kilométrage :" , voiture_1.get_kilométrage())
#print("En marche" , voiture_1.get_en_marche())

voiture_1.demarer()
voiture_1.arreter()