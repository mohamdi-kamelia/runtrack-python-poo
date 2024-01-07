class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    # Getter (assesseur) pour la longueur
    def get_longueur(self):
        return self.__longueur

    # Getter (assesseur) pour la largeur
    def get_largeur(self):
        return self.__largeur

    # Setter (mutateur) pour la longueur
    def set_longueur(self, nouvelle_longueur):
        self.__longueur = nouvelle_longueur

    # Setter (mutateur) pour la largeur
    def set_largeur(self, nouvelle_largeur):
        self.__largeur = nouvelle_largeur

# Utilisation des getter et setter
rectangle_1 = Rectangle(longueur=15, largeur=6)

print("longueur :", rectangle_1.get_longueur())
print("largeur :", rectangle_1.get_largeur())

rectangle_1.set_largeur(18)
rectangle_1.set_longueur(8)

print("Nouvelle longueur :", rectangle_1.get_longueur())
print("Nouvelle largeur :", rectangle_1.get_largeur())
