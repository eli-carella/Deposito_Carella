'''
Creare un array NumPy di 15 elementi contenente numeri casuali compresi tra 1 e
100.
Calcolare e stampare la somma di tutti gli elementi dell'array.
Calcolare e stampare la media di tutti gli elementi dell'array.
'''

import numpy as np

# Creare un array NumPy di 15 elementi casuali tra 1 e 100
array = np.random.randint(1, 101, 15)

# Stampare l'array
print("Array:", array)

# Calcolare e stampare la somma di tutti gli elementi
somma = np.sum(array)
print("Somma degli elementi:", somma)

# Calcolare e stampare la media di tutti gli elementi
media = np.mean(array)
print("Media degli elementi:", media)

