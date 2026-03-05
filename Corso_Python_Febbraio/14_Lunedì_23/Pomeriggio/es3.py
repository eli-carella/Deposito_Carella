'''
1)  Crea una matrice NumPy 2D di dimensioni 6x6 contenente
numeri interi casuali compresi tra 1 e 100.
2)  Estrai la sotto-matrice centrale 4x4 dalla matrice
originale.
3)  Inverti le righe della matrice estratta (cioè, la prima riga
diventa l'ultima, la seconda diventa la penultima, e cosìvia).
4)  Estrai la diagonale principale della matrice invertita ecrea un array 1D contenente questi elementi.
5)  Sostituisci tutti gli elementi della matrice invertita che
sono multipli di 3 con il valore -1.
6)  Stampa la matrice originale, la sotto-matrice centrale
estratta, la matrice invertita, la diagonale principale e lamatrice invertita modificata.
'''
import numpy as np

data = np.random.randint(1, 100, 36)
data = data.reshape((6,6))
print(data.shape)
print(f"matrice inziale {data}")

data_new=data[1:5, 1:5]
print(f"Sottomatrice {data_new}")

data_inv = data_new[::-1, :]
print(f"Matrice invertita {data_inv}")

diag=np.diag(data_inv)
print(diag)
print(f"Diagonale {diag}")

data_inv[data_inv % 3 == 0] = -1
print("Matrice invertita modificata", data_inv)