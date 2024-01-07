class CompteBancaire:
    def __init__ (self ,numéro ,  nom , prénom , solde ,découvert = False):
        self.__numéro = numéro 
        self.__nom = nom
        self.__prénom = prénom
        self.__solde = solde
        self.__découvert = découvert

    def get_solde(self):
        return self.__solde
    
    def get_numéro(self):
        return self.__numéro


    def afficher(self):
        print("Le Nom :" , self.__nom)
        print("Le prénom :" ,self.__prénom)
        print("Le numéro de compte :" , self.__numéro)
        print("Votre solde : " , self.__solde)
        print("Découvert autorisé :", "Oui" if self.__découvert else "Non")
    
    def afficherSolde(self):
        print("le solde est:" , self.__solde , "EUR")
    
    def versement(self , le_montant):
        self.__solde += le_montant
        print("le montant de versement est :" , le_montant , "Votre nouveau solde est " , self.__solde)

    def retrait (self , montant_retirer):
        if self.__solde >= montant_retirer :
            self.__solde -= montant_retirer
            print("Vous avez retirer un montant de :" , montant_retirer , "EUR")
        else:
            print("Solde insuffisant !")
    def agios(self, taux_agios):
        if self.__solde< 0:
            if self.__solde == 0:
                agios = 0              #pas besion de calculer puicq les agios = 0 
            else:
                agios = -self.__solde * taux_agios
            self.retrait(agios)
            print("Agios aoolqués est :" , agios , "€ ." , "votre nouveau solde est :" , self.__solde , "€" )
    
    def virement (self , référence , compte_bancaire , montant):
        if self.__solde  >= montant or self.__découvert :
            self.retrait(montant)
            compte_bancaire.versement(montant)
            print("virement effectué vers le compte :" , compte_bancaire.get_numéro())
        else:
            print("Solde insuffisant !")



Mon_compte = CompteBancaire("75538" , "Mohamdi" , "Kamelia" ,2000)    
Mon_compte.afficher()
Mon_compte.versement(200)
Mon_compte.retrait(400)     
Mon_compte.afficherSolde()

compte = CompteBancaire("847634" , "Bik" , "Maysa" , -450 , découvert= True)
compte.afficher()
compte.virement(Mon_compte, compte, 350)
Mon_compte.afficher()
compte.afficher()

