'''
Esercizio:
1. Crea un array di 12 numeri equidistanti tr
a 0 e 1 usando linspace.
2. Cambia la forma dell'array a una matrice 3x4.
3.Genera una matrice 3x4 di numeri casuali tra
0 e 1.
4.Calcola e stampa la somma degli elementi di entrambe le
matrici.
'''
import numpy as np
arr =np.linspace(0,1, 12)
matr1 = np.reshape(arr, (3,4))
print(arr)

matr2 = np.random.rand(3,4)
print('Somma Matrice 1', np.sum(matr1))
print('Somma Matrice 2', np.sum(matr2))