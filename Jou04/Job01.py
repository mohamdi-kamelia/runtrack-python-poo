class Personne :
    def __init__(self , age = 14 ):
        self.age = age
    def afficherAge(self):
        print("J'ai" , self.age , "ans")
    def Bonjour(self):
        print("Hello")
    def modifierAge(self , age_2):
        self.age = age_2

class Eleve (Personne):
        def allerEnCours(self):
            print("Je vais en cours")
        def afficherAge(self):
            print("J'ai" , self.age , "ans")

class Professeur (Personne):
    def __init__ (self ,age= 30  ,  matiereEnseignee = "Analyse"):
        Personne.__init__(self, age)
        self.matiereEnseignee = matiereEnseignee

    def enseigner(self):
        self.afficherAge() 
        print("J'enseigne la matière :", self.matiereEnseignee)
        print("Le cours va commencer")

kamelia = Personne()
Maysa = Eleve()
prof = Professeur( )

Maysa.Bonjour()
Maysa.afficherAge()
Maysa.allerEnCours()
prof.enseigner()





