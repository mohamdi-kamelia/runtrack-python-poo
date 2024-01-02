class Personne:
    def __init__(self ,nom , prenom ):
        self.nom = nom
        self.prenom = prenom
    def SePresenter (self):
        return f"je suis {self.nom} {self.prenom}"
personne1 =Personne(nom = "Mohamdi" , prenom ="Kamelia")
personne2 =Personne(nom = "Bik" , prenom ="Maysa")
personne3 =Personne(nom = "Feraout" , prenom ="Sophia")
personnes = [personne1 , personne2 , personne3]
for personne in personnes:
    print(personne.SePresenter())
