#Ex 3: Ecrire une fonction en Python pour trouver la somme des séries 1! / 1 + 2! / 2 + 3! / 3 + 4! / 4 + 5! / 5 en utilisant la fonction.
def factorial (x):
    j=1
    for i in range (1,x+1):
        j= i*j
    return j 
def somme_serie():
    k=0
    for i in range (1,6):
            k=k+(factorial(i)/i)
            print ("%d!/%d"%(factorial(i),i))       
    return k
print("la somme est ",somme_serie())
    