class Ville:
    def __init__(self , nom , nombre_habitant) :
        self.__nom = nom
        self.__nombre_habitant = nombre_habitant

    def ajouter_population(self):
        self.__nombre_habitant += 1

    def get_nom_habitant(self) :
        return self.__nombre_habitant

class Personne :
    def __init__(self , nom , age , ville):
        self.__nom = nom
        self.__age = age 
        self.__ville = ville
        self.__ville.ajouter_population()
    

Paris = Ville("Paris" , 1000000)
print("Le Nombre d'habitants de Paris est:" , Paris.get_nom_habitant())  
Marseille = Ville("Marseille" , 861635)
print("Le Nombre d'habitants de Marseille est:" , Marseille.get_nom_habitant())

John =Personne("John" , 25 , Paris)
myrtille = Personne("Myrtille" , 4 , Paris)
chloe = Personne("Chloé", 18, Marseille)

print("Mise a jour de la population de la ville de Paris :" , Paris.get_nom_habitant())

print("Mise a jour de la population de la ville de Marseille : " , Marseille.get_nom_habitant())
    


