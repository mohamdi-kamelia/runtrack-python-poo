import random

class Carte:
    def __init__(self, valeur_carte, couleur_carte):
        self.valeur = valeur_carte
        self.couleur = couleur_carte

    def __str__(self):
        return f"{self.valeur} de {self.couleur}"

class PaquetDeCartes:
    def __init__(self):
        self.paquet = self.initialiser_paquet()

    def initialiser_paquet(self):
        valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'V', 'D', 'R', 'As']
        couleurs = ['Cœur', 'Carreau', 'Trèfle', 'Pique']
        paquet = [Carte(valeur_carte, couleur_carte) for valeur_carte in valeurs for couleur_carte in couleurs]
        return paquet

    def melanger_paquet(self):
        random.shuffle(self.paquet)

    def tirer_carte(self):
        if len(self.paquet) == 0:
            print("Le paquet est vide.")
            return None
        return self.paquet.pop()

def calculer_valeur_main(main):
    total = 0
    as_present = False

    for carte in main:
        if carte.valeur.isdigit():
            total += int(carte.valeur)
        elif carte.valeur in ['V', 'D', 'R']:
            total += 10
        elif carte.valeur == 'As':
            as_present = True
            total += 11

    if as_present and total > 21:
        total -= 10

    return total

def afficher_main(main):
    for carte in main:
        print(carte)

def jouer_partie():
    paquet_de_cartes = PaquetDeCartes()
    paquet_de_cartes.melanger_paquet()

    main_joueur = [paquet_de_cartes.tirer_carte(), paquet_de_cartes.tirer_carte()]
    main_croupier = [paquet_de_cartes.tirer_carte(), paquet_de_cartes.tirer_carte()]

    print("La partie commence !")
    print("\nMain du joueur :")
    afficher_main(main_joueur)
    print("\nMain du croupier :")
    print(f"{main_croupier[0]} et une carte face cachée")

    while True:
        choix = input("\nVoulez-vous piocher une carte (p) ou passer (n)? ").lower()

        if choix == 'p':
            nouvelle_carte = paquet_de_cartes.tirer_carte()
            main_joueur.append(nouvelle_carte)
            print(f"Vous avez tiré le {nouvelle_carte}.")
            afficher_main(main_joueur)

            if calculer_valeur_main(main_joueur) > 21:
                print("Vous avez dépassé 21. Vous avez perdu.")
                break
        elif choix == 'n':
            while calculer_valeur_main(main_croupier) < 17:
                nouvelle_carte_croupier = paquet_de_cartes.tirer_carte()
                main_croupier.append(nouvelle_carte_croupier)
                print(f"Le croupier a tiré le {nouvelle_carte_croupier}.")

            print("\nMain du joueur :")
            afficher_main(main_joueur)
            print("\nMain du croupier :")
            afficher_main(main_croupier)

            if calculer_valeur_main(main_joueur) > 21:
                print("Vous avez dépassé 21. Vous avez perdu.")
            elif calculer_valeur_main(main_joueur) > calculer_valeur_main(main_croupier):
                print("Vous avez gagné !")
            elif calculer_valeur_main(main_joueur) < calculer_valeur_main(main_croupier):
                print("Le croupier a gagné.")
            else:
                print("Match nul")

            break
        else:
            print("Choix invalide. Veuillez choisir 'p' pour piocher une carte ou 'n' pour passer.")

# Exécution du jeu
jouer_partie()




