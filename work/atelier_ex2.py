#Ex 2 : Ecrire une fonction python qui calcul la factorielle d’un nombre donné
a = int (input ("entrer un nbr: "))
def factorial (x):
    j=1
    for i in range (1,x+1):
        j= i*j
    return j 
print ("factorielle de %d est "%a,factorial(a))
