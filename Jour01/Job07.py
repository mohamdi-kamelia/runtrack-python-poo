class Personnage:
    def __init__ (self , x = 0 , y = 0):
        self.x = x
        self.y = y
    def haut(self):
        self.y += 1
    def bas(self):
        self.y -= 1
    def droite(self):
        self.x += 1
    def gauche(self):
        self.x -= 1
    def position (self):
        return f"Positionns des coordonnées : ({self.x} , {self.y})"

personnage = Personnage()
print(personnage.position())
personnage.droite()
personnage.haut()
print(personnage.position())