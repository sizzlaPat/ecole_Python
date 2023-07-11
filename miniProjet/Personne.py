from abc import ABC,abstractmethod
class Personne:


 def __init__(self,nom) :
    self.nom = nom

 @abstractmethod
 def display(self):
   pass
        