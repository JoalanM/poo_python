
class Voiture:
    def __init__(self, essence, ):
        self.essence  = essence
        


    def roule(self, km):
        self.km = km
        self.essence = self.essence - (km*5)/100
 


    def afficher_reservoir(self, ):

        print(f"La voiture contient {self.essence} litres d'essence")
        if self.essence<=0:
            print("Vous n'avez plus d'essence, faites le plein ! ")
        if self.essence<=10:
            print(f"Il vous reste {self.essence} litre, vous n'avez bientôt plus d'essence ! ")
           

    def faire_le_plein(self,):
        if self.essence ==0 :
            self.essence=100
            print("vous pouvez repartir")
        elif self.essence <=10:
            self.essence= 100
            print("Vous pouvez repartir")    

litre= int(input("Bonjour veuillez entrez le nombre de litre qu'il vous reste dans le véhicules : "))  
voiture1= Voiture(litre)

distance = int(input("Veuillez entrée la distance que vous devez parcourir en KM : "))
voiture1.roule(distance)

voiture1.afficher_reservoir()

plein=int(input("Pour faire le plein tapez 1 : "))
if plein == 1:
    voiture1.faire_le_plein()




