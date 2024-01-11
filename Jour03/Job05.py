
import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        degats = random.randint(1, 10)
        print(f"{self.nom} attaque {adversaire.nom} et lui inflige {degats}.")
        adversaire.subir_degats(degats)

    def subir_degats(self, degats):
        self.vie -= degats
        print(f"{self.nom} a subi {degats}. Vie restante : {self.vie}")

class Jeu:
    def __init__(self):
        self.niveau = 1

    def choisir_niveau(self):
        self.niveau = int(input("Choisissez le niveau de difficulté (1, 2, 3) : "))

    def lancer_jeu(self):
        self.choisir_niveau()

        joueur = Personnage("Kamelia", 50)
        ennemi = Personnage("Maysa", 50)

        print(f"\nUn combat commence entre : {joueur.nom} et {ennemi.nom}\n")

        while joueur.vie > 0 and ennemi.vie > 0:
            print("Tour du joueur:")
            joueur.attaquer(ennemi)
            if ennemi.vie <= 0:
                print(f"\nFélicitations pour {joueur.nom}, il a gagné!")
                break

            print("Tour de l'adversaire")
            ennemi.attaquer(joueur)
            if joueur.vie <= 0:
                print(f"\nDommage ! {ennemi.nom} a vaincu {joueur.nom}.")
                break

# Exécution du jeu
jeu = Jeu()
jeu.lancer_jeu()




                          


        
