class Livre:
    def __init__(self, titre, auteur, pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = pages
        self.__disponible = True

    # Méthodes getter
    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_pages(self):
        return self.__pages

    def get_disponible(self):
        return self.__disponible

    # Méthodes setter
    def set_titre(self, nouveau_titre):
        self.__titre = nouveau_titre

    def set_auteur(self, nouvel_auteur):
        self.__auteur = nouvel_auteur

    def set_pages(self, nouvelles_pages):
        if isinstance(nouvelles_pages, int) and nouvelles_pages > 0:
            self.__pages = nouvelles_pages
        else:
            print("Message d'erreur : le nombre de pages doit être un entier positif")

    def set_disponible(self, disponible):
        self.__disponible = disponible

    # Autres méthodes de la classe
    def emprunter(self):
        if self.get_disponible():
            print("Livre emprunté !")
            self.set_disponible(False)
        else:
            print("Le livre n'est pas disponible !")

    def rendre(self):
        if not self.get_disponible():
            print("Livre rendu")
            self.set_disponible(True)
        else:
            print("Le livre est déjà disponible")

# Utilisation de la classe
livre_1 = Livre(titre="une étoile", auteur="kamelia", pages=250)

print("Le titre du livre est :", livre_1.get_titre())
print("L'auteur de ce livre s'appelle :", livre_1.get_auteur())
print("Le nombre de ses pages est :", livre_1.get_pages())

# Nouvelles valeurs
livre_1.set_titre("informatique")
livre_1.set_auteur("Layna")
livre_1.set_pages(500)
livre_1.set_pages(-500)  # Affichera le message d'erreur

# Affichage des nouvelles valeurs
print("Le titre du nouveau livre est :", livre_1.get_titre())
print("Le nouvel auteur de ce livre s'appelle :", livre_1.get_auteur())
print("Le nombre des pages de ce livre est :", livre_1.get_pages())

# Emprunt du livre
livre_1.emprunter()
print("Le livre est-il disponible après l'emprunt ?", livre_1.get_disponible())
livre_1.rendre()

# Vérification
print("Le livre est-il disponible après le rendu ?", livre_1.get_disponible())
