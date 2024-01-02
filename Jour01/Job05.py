class Point:
    def __init__(self, x=1 , y=2):
        self.x = x
        self.y = y
    def afficherLesPoints (self):
        print("les coordonnées des points:", "x=",self.x ,"y=" , self.y )
    def afficherX(self):
        print("coordonnées x = " , self.x)
    def afficherY(self):
        print("coordonnées y = " , self.y)
    def nouvelleX(self , nouvelle_valeur):
        self.x = nouvelle_valeur
    def nouvelleY(self , nouvelle_valeur):
        self.y = nouvelle_valeur
Point().afficherLesPoints()
Point().afficherX()
Point().afficherY()
Valeur = Point()
Valeur.nouvelleX(5)
Valeur.nouvelleY(10)
Valeur.afficherLesPoints()
Valeur.afficherX()
Valeur.afficherY()