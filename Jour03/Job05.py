class Personne:
    def __init__(self, nom, vie):
        self._nom = nom  
        self._vie = vie

    def attaquer(self, adversaire):
        points = 10
        adversaire.recevoir_points(points)

    def recevoir_points(self, points):
        self._vie -= points
        print(self._nom, "a subi", points, ". Vie restante :", self._vie)

class Jeu:
    def __init__(self):
        self.niveau = 1

    def choisirNiveau(self):
        self.niveau = int(input("Choisissez le niveau de 1 à 3 :"))

    def lancerJeu(self):
        Joueur = Personne("Kamelia", 100 * self.niveau)
        Adversaire = Personne("Maysa", 50 * self.niveau)

        print("Un combat commence entre :", Joueur._nom, "et", Adversaire._nom)

        while Joueur._vie > 0 and Adversaire._vie > 0:
            print("Tour du joueur:")
            Joueur.attaquer(Adversaire)

            if Adversaire._vie <= 0 :
                break
            print("Tour de l'adversaire")

        self.verifierGagnant(Joueur, Adversaire)

    def verifierGagnant(self, Joueur, Adversaire):
        if Joueur._vie <= 0:
            print("Félicitations pour ", Adversaire._nom, ", il a gagné!")
        else:
            print("Félicitations pour ", Joueur._nom, ", il a gagné!")

# Utilisation des classes
le_jeu = Jeu()
le_jeu.choisirNiveau()
le_jeu.lancerJeu()



                          


        
