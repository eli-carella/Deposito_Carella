'''
Creare un array NumPy di forma (4, 4) contenente numeri casuali interi tra 10 e 50.
Utilizzare fancy indexing per selezionare e stampare gli elementi agli indici (0,
1), (1, 3), (2, 2) e (3, 0).
Utilizzare fancy indexing per selezionare e stampare tutte le righe dispari
dell'array (considerando la numerazione delle righe che parte da 0).
Modificare gli elementi selezionati nel primo punto dell'esercizio aggiungendo 10
al loro valore.
'''

import numpy as np

arr = np.random.randint(10,51, 16)
matr=arr.reshape(4,4)


# Indici da selezionare
righe = [0, 1, 2, 3]
colonne = [1, 3, 2, 0]

# Selezionare e stampare gli elementi specifici
elementi_selezionati = matr[righe, colonne]
print("\nElementi selezionati agli indici (0,1), (1,3), (2,2), (3,0):", elementi_selezionati)

# Selezionare e stampare tutte le righe dispari
righe_dispari = matr[1::2]
print("\nRighe dispari:\n", righe_dispari)

# Modificare gli elementi selezionati aggiungendo 10
matr[righe, colonne] += 10
print("\nArray dopo aver aggiunto 10 agli elementi selezionati:\n", matr)