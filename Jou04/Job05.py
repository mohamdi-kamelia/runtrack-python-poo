import math
class Forme:
    def aire(self):
        return 0
class Rectangle(Forme):
    def __init__(self , largeur , hauteur):
        self.__largeur = largeur 
        self.__hauteur = hauteur
    def aire (self):
        return self.__hauteur * self.__largeur   

class Cercle(Forme):
    def __init__(self , radius):
        self.radius = radius
    def aire (self):
        return math.pi * self.radius **2

mon_rectangle=Rectangle( largeur =16 , hauteur =18)
print ("l' air de rectangle = " , mon_rectangle.aire())

mon_cercle = Cercle(radius = 4)
print("L'air de cercle = " , mon_cercle.aire())

