class Cercle :
    def __init__ (self , r = 1):
        self.r = r
    def changerRayon(self , rayon):
        self.r = rayon
    def afficherInfos (self):
        return f"Les informations du cercle : rayon = {self.r}"
    def circonférence(self):
        return self.r * 2 * 3,141592653589793 
    def aire(self):
        return (self.r ** 2) * 3,141592653589793
    def diametre (self):
        return 2 * self.r
cercle1 = Cercle(r = 4)
cercle2 = Cercle(r = 7)
print(cercle1.afficherInfos())
print(cercle2.afficherInfos())
print (f"circonférence du cercle 1 : {cercle1.circonférence()}")
print (f"circonférence du cercle 2 : {cercle2.circonférence()}")
print (f"L'aire du cercle 1 : {cercle1.aire()}")
print (f"L'aire du cercle 2 : {cercle2.aire()}")
print (f"Le diametre du cercle 1 : {cercle1.diametre()}")
print (f"Le diametre du cercle 2 : {cercle2.diametre()}")