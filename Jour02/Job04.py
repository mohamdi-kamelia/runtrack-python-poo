class Student:
    def __init__(self, nom, prenom, numéro_étudiant):
        self.__nom = nom
        self.__prenom = prenom 
        self.__numéro_étudiant = numéro_étudiant
        self.__nombre_crédit = 0
        self.__level = self.studentEval()

    def add_crédits(self, crédits):
        if crédits > 0:
            self.__nombre_crédit += crédits
            self.__level = self.studentEval()
        else:
            print("message d'erreur : nombre de crédit doit être positif")

    def get_total_crédit(self):
        return self.__nombre_crédit

    def studentEval(self):
        if self.__nombre_crédit >= 90:
            return "Excellent"
        elif self.__nombre_crédit >= 80:
            return "Très Bien"
        elif self.__nombre_crédit >= 70:
            return "Bien"
        elif self.__nombre_crédit >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def studentInfo(self):
        print("Nom :", self.__nom)
        print("Prenom :", self.__prenom)
        print("Numéro d'étudiant :", self.__numéro_étudiant)
        print("Niveau :", self.__level)

# Instanciation d'un étudiant
etudiant = Student(nom="Doe", prenom="John", numéro_étudiant=145)

# Ajout de crédits
etudiant.add_crédits(20)
etudiant.add_crédits(20)
etudiant.add_crédits(20)

# Affichage des informations de l'étudiant
etudiant.studentInfo()

# Affichage du total de crédits
print("Le total de crédits de", etudiant._Student__nom, etudiant._Student__prenom, "est de", etudiant.get_total_crédit())

