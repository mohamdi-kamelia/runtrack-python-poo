class Livre:
    def __init__(self, titre, auteur, pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = pages

    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_pages(self):
        return self.__pages

    def set_titre(self, nouveau_titre):
        self.__titre = nouveau_titre

    def set_auteur(self, nouvel_auteur):
        self.__auteur = nouvel_auteur

    def set_pages(self, nouvelles_pages):
        if isinstance(nouvelles_pages, int) and nouvelles_pages > 0:
            self.__pages = nouvelles_pages
        else:
            print("Message d'erreur : le nombre de pages doit être un entier positif")

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
