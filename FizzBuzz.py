class FizzBuzz:
    def affiche(self,nombreMin,nombreMax):
        resultat=""

        for i in range(nombreMin, nombreMax + 1):
            if i%15==0 :
                resultat +="FrisBee"
            elif i%5==0:
                resultat +="Buzz"
            elif i%3==0:
                resultat += "Fizz"
            else:
                resultat += str(i)
        
        return resultat