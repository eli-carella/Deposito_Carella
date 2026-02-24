'''
Crea un array NumPy (ndarray) utilizzando np.arange con valori da 0 a 49. più altre 50 posizioni casuali tra 49 e 101.
Stampa l’array, il suo dtype e la sua shape.
Modifica il tipo di dato (dtype) dell’array in float64.
Verifica e stampa di nuovo dtype e shape.
Utilizza lo slicing per ottenere:
i primi 10 elementi
gli ultimi 7 elementi
gli elementi dall’indice 5 all’indice 20 escluso
ogni quarto elemento dell'array
Modifica tramite slicing gli elementi dall’indice 10 a 15 (escluso) assegnando loro il valore 999.
Utilizza la fancy indexing per selezionare:
gli elementi in posizione [0, 3, 7, 12, 25, 33, 48]
tutti gli elementi pari dell’array utilizzando una maschera booleana
tutti gli elementi maggiori della media dell'array
Stampa:
l’array originale dopo tutte le modifiche
tutti i sotto-array ottenuti tramite slicing e fancy indexin
'''
import numpy as np

arr1 = np.arange(50)
#array con numeri random tra 49 e 101 di 50 posti
arr2 = np.random.randint(49, 102, 50)
# concateno i due array
arr = np.concatenate((arr1, arr2))
#stampa dtype e shape
print("Array:", arr)
print("dtype:", arr.dtype)
print("shape:", arr.shape)
#conversione in dtype float
arr = arr.astype(np.float64)
print("dtype:", arr.dtype)
print("shape:", arr.shape)

#slicing
print(arr[:10])
print(arr[-7:])
print(arr[5:20])
print(arr[::4])

#modifica elementi
arr[10:15]=999

#fancy indexing
index=[0,3,7,12,25,33,48]
print(arr[index])

#mask n umeri pari
mask=(arr%2==0)
print(arr[mask])

#mask elementi > mean
mask2= (arr>np.mean(arr))
print(np.mean(arr))
print(arr[mask2])

print("\nArray finale dopo modifiche:")
print(arr)