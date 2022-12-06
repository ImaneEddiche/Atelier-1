#Ex 1 :Ecrire une fonction qui renvoie la puissance d’un nombre Xn
a = int (input ("entrer un nbr: "))
b = int (input ("entrer la puissance: "))
def puissance(x,n):
    for i in range (1,n) :
        x=x*x
    return x 
print (puissance (a,b))
