#Ex 8:Ecrire une fonction qui cherche un élément dans une matrice puis renvoi sa position «i,j».
def searchElementInMatrix(matrix,num):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if(matrix[i][j] == num):
               return "la position de %d est <<"%(num,i,j)
        return "le nombre %d n existe pas dans cette matrice"%(num) 
        


