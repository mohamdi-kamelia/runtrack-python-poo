class Joueur:
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts_marques = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0

    def marquer_un_but(self):
        self.buts_marques += 1

    def effectuer_une_passe_decisive(self):
        self.passes_decisives += 1

    def recevoir_un_carton_jaune(self):
        self.cartons_jaunes += 1

    def recevoir_un_carton_rouge(self):
        self.cartons_rouges += 1

    def afficher_statistiques(self):
        return f"{self.nom}, Numéro: {self.numero}, Buts: {self.buts_marques}, Passes décisives: {self.passes_decisives}, Cartons jaunes: {self.cartons_jaunes}, Cartons rouges: {self.cartons_rouges}"


class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.liste_joueurs = []

    def ajouter_joueur(self, joueur):
        self.liste_joueurs.append(joueur)

    def afficher_statistiques_joueurs(self):
        for joueur in self.liste_joueurs:
            print(joueur.afficher_statistiques())

    def mettre_a_jour_statistiques_joueur(self, nom_joueur, action):
        for joueur in self.liste_joueurs:
            if joueur.nom == nom_joueur:
                if action == 'but':
                    joueur.marquer_un_but()
                elif action == 'passe':
                    joueur.effectuer_une_passe_decisive()
                elif action == 'carton_jaune':
                    joueur.recevoir_un_carton_jaune()
                elif action == 'carton_rouge':
                    joueur.recevoir_un_carton_rouge()


# Création des joueurs
joueur_1 = Joueur("Cristiano Ronaldo", 7, "Attaquant")
joueur_2 = Joueur("Lionel Messi", 10, "Attaquant")
joueur_3 = Joueur("Neymar Jr", 11, "Milieu")
joueur_4 = Joueur("Riyad Mahrez", 7, "Attaquant")

# Création des équipes
equipe_1 = Equipe("Equipe 1")
equipe_2 = Equipe("Equipe 2")

# Ajout des joueurs aux équipes
equipe_1.ajouter_joueur(joueur_1)
equipe_1.ajouter_joueur(joueur_2)
equipe_2.ajouter_joueur(joueur_3)
equipe_2.ajouter_joueur(joueur_4)

# Affichage des statistiques avant le match
print("Statistiques des joueurs avant le match :")
equipe_1.afficher_statistiques_joueurs()
equipe_2.afficher_statistiques_joueurs()

# Simulation d'un match
equipe_1.mettre_a_jour_statistiques_joueur("Lionel Messi", "but")
equipe_1.mettre_a_jour_statistiques_joueur("Lionel Messi", "carton_jaune")
equipe_2.mettre_a_jour_statistiques_joueur("Neymar Jr", "carton_jaune")
equipe_2.mettre_a_jour_statistiques_joueur("Riyad Mahrez", "but")

# Affichage des statistiques après le match
print("\nStatistiques des joueurs après le match :")
equipe_1.afficher_statistiques_joueurs()
equipe_2.afficher_statistiques_joueurs()
