class Rectangle:
    def __init__ (self , longueur , largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    def assesseurs_longueur(self):
        return self.__longueur
    def assesseurs_largueur(self):
        return self.__largeur
    def mutateurs_longueur(self , nouvelle_longueur):
        self.__longueur = nouvelle_longueur
    def mutateurs_largueur(self , nouvelle_longueur):
        self.__largeur = nouvelle_longueur
rectangle_1 = Rectangle(longueur = 15 , largeur = 6)
print("longueur : " , rectangle_1.assesseurs_longueur())
print("largeur : " , rectangle_1.assesseurs_largueur())
rectangle_1.mutateurs_largueur(18)
rectangle_1.mutateurs_longueur(8)
print("Nouvelle longueur : " , rectangle_1.assesseurs_longueur())
print("Nouvelle largeur : " , rectangle_1.assesseurs_largueur())