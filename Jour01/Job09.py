class Produit:
    def __init__(self , nom , prixHT , TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA
    def CalculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA / 100)
    def afficher(self):
        return f"Nom du produit :{self.nom},PRIX HT: {self.prixHT},TVA : {self.TVA}%"
    def modification_nom(self, nouveauNom):
        self.nom = nouveauNom
    def modification_prixHT(self, nouveauprixHT):
        self.prixHT = nouveauprixHT
    def retourner_nom(self):
        return self.nom
    def retourner_prixHT(self):
        return self.prixHT
    def retourner_TVA(self):
        return self.TVA

produit1 = Produit(nom="Ordinateur Portable", prixHT=220 , TVA=20)
produit2 = Produit(nom="Smartphone", prixHT=200 , TVA=10)
produit3 = Produit(nom="Casque Audio", prixHT=100 , TVA=30)
produits = [produit1, produit2 , produit3]
# Affichage des informations 
for produit in produits:
    print(produit.afficher())
    print(f"Prix TTC du produit : {produit.CalculerPrixTTC()}")

# Modification du nom et du prix 
produit1.modification_nom("Switch")
produit2.modification_nom("Tablette")
produit3.modification_nom("PC")
produit1.modification_prixHT(154)
produit2.modification_prixHT(150)
produit3.modification_prixHT(755)

# Affichage des nouvelles informations 
for produit in produits:
    print(produit.afficher())