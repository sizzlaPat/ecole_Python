from Etudiant import Etudiant
from Personne import Personne
from Classe import Classe

def addEtudiant():
    print("Saisir un nouvelle étudiant\n")
    nom= input("merci de saisir une nom\n")
    matricule= input("merci de saisir un matricule\n")
    note= input("merci de saisir une note\n")
    dateDeNaissance= input("merci de saisir la dateDeNaissance\n")
    etudiant= Etudiant(nom,dateDeNaissance,matricule,note)
    return etudiant

def menu():
   menu=["Ajouter un étudiant","Modifier un étudiant","Supprimmer un étudiant","Afficher la liste des etudiant"]
   print ("choix du menu")
   for i in range (len(menu)):
    print(i+1,")",menu[i],"\n") 
   choix=int( input("Entrez votre choix : "))
   return choix-1
   
def MaJ(matricule):
  etudiant=etudiant.rechercheEtudiantParMatricule(matricule)
  menu=["Modifier le nom","Modifier la date de naissance","Modifier matricule","Modifier la note "]
  print ("choix du menu")
  for i in range (0,len(menu)):
    print(i+1,")",menu[i],"\n") 
  choix=int( input("Entrez votre choix : "))
      
  if(choix-1 == 0):
    etudiant.setNom("nouveauNom")
    
  elif(choix-1 == 1):
    etudiant.setDateDeNaissance("nouveaudateDeNaissance")
      
  elif(choix-1 == 2):
    etudiant.setMatricule("nouveaumatricule")
  
  elif(choix-1 == 3):
    etudiant.setNote("nouvelleNote")



if __name__=='__main__':
  maclasse=Classe("maClasse")

  selection =menu()
 
  if (selection == 0) :
    start=True
    while(start):   
        etudiant=addEtudiant() 
        maclasse.ajoutEtudiant(etudiant)

        reponse= input("voulez vous sasisir un nouvelle employée? O/N \n")
        if( reponse == "N" or reponse == "n"):
            start=False

  elif( selection == 1):
    start=True
    while(start):
        matricule=int( input("Entrez le matricule : "))
        MaJ(matricule)
    reponse= input("voulez vous sasisir un nouvelle modification? O/N \n")
    if( reponse == "N" or reponse == "n"):
        start=False

    elif( selection == 2):
        matricule=int( input("Entrez le matricule de l'étudiant à supprimer : "))
        maclasse.supprimerEtudiant(matricule)

    elif( selection == 3):
        maclasse.affichageList()

  else:
    print ( "En revoir")
