class Tache:
    def __init__(self, titre, description, statut="A faire"):
        self.titre = titre
        self.description = description
        self.statut = statut

    def afficher_details(self):
        return f"{self.titre} - {self.description} - Statut : {self.statut}"


class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)
        print("La tache :", tache.titre, "est ajoutée !")

    def supprimerTache(self, titre):
        tache_restante = [tache for tache in self.taches if tache.titre != titre]
        if len(tache_restante) < len(self.taches):
            print("Tache", titre, "supprimée !")
        else:
            print("Tache", titre, "introuvable !")
        self.taches = tache_restante

    def marquerCommeFinie(self, titre):
        for tache in self.taches:
            if tache.titre == titre:
                tache.statut = "Terminée"
                print("La tache", titre, "est faite")
                return
        print("Tache introuvable")

    def afficherListe(self):
        for tache in self.taches:
            print(tache.afficher_details())

    def filterListe(self, statut):
        taches_filtrées = [tache for tache in self.taches if tache.statut == statut]
        return taches_filtrées


tache_1 = Tache("Faire le ménage", "Nettoyer la maison")
tache_2 = Tache("Faire le shopping", "Acheter des provisions")
tache_3 = Tache("Révision", "Préparer pour les examens")

liste_taches = ListeDeTaches()

#  ajouter des tâches
liste_taches.ajouterTache(tache_1)
liste_taches.ajouterTache(tache_2)
liste_taches.ajouterTache(tache_3)

#  afficher la liste
print("Liste de mes taches :")
liste_taches.afficherListe()

#  marquer une tâche comme terminée
liste_taches.marquerCommeFinie("Révision")

#suuprimer une tache 
liste_taches.supprimerTache("Faire le ménage")

#  afficher la nouvelle liste
print("Nouvelle Liste :")
liste_taches.afficherListe()

print("Liste après suppression:")
liste_taches.afficherListe()

# filtrer les tâches à faire
taches_a_faire = liste_taches.filterListe("A faire")
print("Tâches à faire:")
for tache in taches_a_faire:
    print(tache.afficher_details())











