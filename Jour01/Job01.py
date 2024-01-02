class Opération:
    def __init__(self , nombre01 = 4 , nombre02 = 17): 
        self.nombre01 = nombre01
        self.nombre02 = nombre02
    def addition(self) :
        resultat = self.nombre01 + self.nombre02
        print("le résultat est :", resultat)
#Instancier la première classe
Opération_instence = Opération()
#impression d'objet en console
print(Opération_instence)
