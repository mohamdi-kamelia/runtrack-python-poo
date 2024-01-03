class Commande:
    def __init__(self, numéro_commande):
        #initialisation de la commande
        self.__num_commande = numéro_commande
        self.__plats_commandés = {}
        self.__statut_commande = "en cours"

    def ajouter_plat(self, nom_plat, prix_plat):
        if self.__statut_commande == "en cours":
            self.__plats_commandés[nom_plat] = {'prix': prix_plat, 'statut': 'en cours'}
            print("Le plat ajouté est :", nom_plat)

    def annulation_commande(self):
        self.__statut_commande = "annulée"
        print("La commande est annulée")
#affichage des détails de la commade
    def afficher_commande(self):
        print("Numéro de la commande est", self.__num_commande)
        print("Les plats commandés : ")
        for nom_plat, plat in self.__plats_commandés.items():
            print(f" - {nom_plat}: {plat['prix']} € ({plat['statut']})")
        print(f"Total à payer : {self.__calculer_total()} €")
#calcule du total
    def __calculer_total(self):
        total = sum(plat['prix'] for plat in self.__plats_commandés.values() if plat['statut'] == 'en cours')
        return total
#calcule de tva 
    def calculer_tva(self, taux_tva):
        return self.__calculer_total() * (taux_tva / 100)

commande_1 = Commande(1)
commande_1.ajouter_plat("Pates", 13)
commande_1.ajouter_plat("Sandwitch", 10)
commande_1.ajouter_plat("Tacos", 9.5)
commande_1.afficher_commande()

commande_1.annulation_commande()
commande_1.afficher_commande()
