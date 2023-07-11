from Etudiant import Etudiant

class Classe():

   
    def __init__(self,nom_classe) :
        self.__nom_classe = nom_classe
        self.__moyenne=0
        self.__elevesList=[]

    def getNom_classe(self):
        return self.nom_classe
    
    
    
# Calcul de la moyenne de la classe

    def getMoyenne(self):
        somme=0
        for i in range (0,len(self.__elevesList)):
         somme=somme+ self.__elevesList[i].note
        self.moyenne=somme/len(self.__elevesList)
        return self.moyenne   
    
    
# Methode d'ajout d'un étudiant dans la liste

    def ajoutEtudiant(self,etudiant) :
        self.__elevesList.append(etudiant)
        
        
 #   Recherche d'étudiant par matricule
    
    def rechercheEtudiantParMatricule(self,matricule):
        for i in range (0,len(self.__elevesList)):
            if(self.__elevesList[i].getMatricule() == matricule):
                return i
            else:
                print ("Aucun étudiant n'a le matricule ", matricule )
                return -1
            
    
             
    # Recherche et suppression d'un étudiant par Id
             
    def supprimerEtudiantByMatricule(self,matricule):
         index= self.rechercheEtudiantParMatricule(matricule)
         if (index > 0) :
              self.__elevesList.pop(index)
         else :
             print("l'étudiant n'existe pas!!")
             
             

    # Affichage de la liste des éléves d'une classe et la moyenne de la classe
    
    def  affichageList(self):
        for i in range (0,len(self.__elevesList)):
            print("la classse \n",self.getNom_classe(),"Liste des etudiants \n",self.__elevesList[i].display() )
        print("La moyenne de la classe est de \n" , self.getMoyenne())
    
    
   



    
        
