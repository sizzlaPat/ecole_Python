from Personne import Personne
class Etudiant(Personne):
   
    def __init__(self,nom,dateDeNaissance,matricule,note) :
        super().__init__(nom)
        self.__nom = nom
        self.__matricule = matricule
        self.__note = note
        self.__dateDeNaissance = dateDeNaissance
    
    def getNom(self):
      return self.nom

    def getDateDeNaissance(self):
      return self.dateDeNaissance

    def getNatricule(self):
      return self.matricule
    
    def getNote(self):
       return self.note
     
    def setNom(self,nouveau):
      self.nom=nouveau

    def setDateDeNaissance(self,nouveaudateDeNaissance):
      self.dateDeNaissance=nouveaudateDeNaissance

    def setMatricule(self,nouveaumatricule):
      self.matricule=nouveaumatricule
    
    def setNote(self,nouveaunote):
     self.note=nouveaunote

    def display(self):
       print("Nom étudiant : ", self.getNom(),"\nMatricule : ", self.getNatricule(),"\nNote : ", self.getNote())
   
   

    
    