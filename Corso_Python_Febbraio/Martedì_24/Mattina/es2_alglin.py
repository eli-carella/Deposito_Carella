'''
Creare una matrice 5x5 contenente numeri interi sequenziali da 1 a 25.
Estrarre e stampare la seconda colonna della matrice.
Estrarre e stampare la terza riga della matrice.
Calcolare e stampare la somma degli elementi della diagonale principale della
matrice.
'''
import numpy as np
arr=np.linspace(1,25, 25)
matr=arr.reshape((5,5))
print(matr)
print(matr[:, 2])
print(matr[3, :])

diag = np.diag(matr)
somma = np.sum(diag)
print(somma)