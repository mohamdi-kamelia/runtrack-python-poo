class Livre :
    def __init__(self , titre , auteur , pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = pages
    def assesseurs_titre (self):
        return self.__titre
    def assesseurs_auteur(self):
        return self.__auteur
    def assesseurs_pages(self):
        return self.__pages
    def mutateurs_titre(self, nouveau_titre):
        self.__titre = nouveau_titre
    def mutateurs_auteur(self , nouvel_titre):
        self.__auteur = nouvel_titre
    def mutateurs_pages(self ,  nouvelles_pages):
        if type (nouvelles_pages) == int and nouvelles_pages > 0 :
            self.__pages = nouvelles_pages
        else:
            print("message d'erreur : le nombre de pages doit etre entier et positif")
livre_1 = Livre(titre= "une étoile" , auteur = "kamelia" , pages= 250)
print("le titre de livre est :" , livre_1.assesseurs_titre())
print("L'auteur de ce livre s'appelle : ", livre_1.assesseurs_auteur())
print("le nombre de ses pages est :" , livre_1.assesseurs_pages())
#npuvelles valeurs
livre_1.mutateurs_titre("informatique")
livre_1.mutateurs_auteur("Layna")
livre_1.mutateurs_pages(500)
livre_1.mutateurs_pages(-500)
print("le titre du nouveau livre est :" , livre_1.assesseurs_titre())
print("Le nouvel auteur de ce livre s'appelle : ", livre_1.assesseurs_auteur())
print("le nombre des pages de se livre est :" , livre_1.assesseurs_pages())