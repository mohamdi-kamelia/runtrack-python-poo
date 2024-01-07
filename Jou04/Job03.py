class Rectangle :
    def __init__(self , longueur , largeur):
        self.__longueur  = longueur
        self.__largeur = largeur
    
    def getLongueur(self):
        return self.__longueur

    def getLargeur(self):
        return self.__largeur
    
    def setLongueur(self ,longueur):
        self.__longueur = longueur

    def setLargeur(self ,largeur):
        self.__largeur = largeur

    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)
    
    def surface(self):
        return self.__largeur * self.__longueur

class Parallelepipede(Rectangle):
    def __init__(self , longueur , largeur , hauteur):
        Rectangle.__init__(self ,largeur , longueur)
        self.__hauteur = hauteur

    def getHauteur(self):
        return self.__hauteur
    
    def setHauteur(self , hauteur):
        self.__hauteur = hauteur

    def volume (self):
        return self.surface() * self.__hauteur
    

mon_rectangle = Rectangle(longueur = 10 , largeur = 6)
print("Périmètre du  rectangle est " , mon_rectangle.perimetre())
print("La surface du  rectongle est " , mon_rectangle.surface())

#modifications des paramétre 
mon_rectangle.setLongueur(4)
mon_rectangle.setLargeur(2)
print("Nouveau périmètre du rectangle est " , mon_rectangle.perimetre())
print("Nouvelle surface du  rectongle est " , mon_rectangle.surface())

parallelepipede = Parallelepipede(longueur= 8 , largeur= 15 , hauteur=  4)
#print("Hauteur du parallélépipède est ", parallelepipede.getHauteur())
#print("Longueur du parallélépipède est ", parallelepipede.getLongueur())
#print("Largeur du parallélépipède est ", parallelepipede.getLargeur())
print("Volume du parallélépipède  est  " , parallelepipede.volume())



