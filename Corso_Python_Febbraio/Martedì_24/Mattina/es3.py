'''
1) Utilizza np.linspace per creare un array di 50 numeri equidistanti tra 0 e 10.
2) Utilizza np.random.random per creare un array di 50 numeri casuali compresi
tra 0 e 1.
3) Somma i due array elemento per elemento per ottenere un nuovo array.
4) Calcola la somma totale degli elementi del nuovo array.
5) Calcola la somma degli elementi del nuovo array che sono maggiori di 5.
6) Stampa gli array originali, il nuovo array risultante dalla somma e le somme calcolate.
7) Salva i dati su un file TXT a ogni giro
8) Rendi ripetibile il processo complessivo
9) Chiedi se si vuole sovrascrivere il TXT o no.
'''

import numpy as np
#array tra 0-10 equidistante di 50 posti
arr1 = np.linspace(0,10, 50)
print('\nArray 1 ',arr1)
#array random tra 0-1 50 posti
np.random.seed(42) #rende ripetibile il processo, numero iniziale (seed) per l’algoritmo pseudo-casuale.
arr2 = np.random.random(50)
print('\nArray 2 ',arr2)
#array somma 
arr3=arr1+arr2
print('\nArray nuovo ',arr3)
#somma dell'array
somma = np.sum(arr3)
print('\n Somma totale ',somma)
#somma di elementi >5
mask=(arr3>5)
somma2=np.sum(arr3[mask])
print('Somma elementi >5', somma2)

#scrittura su file con scelta modalità sovrascrittura o append
scelta = input("\nVuoi sovrascrivere il file? (s/n): ")

if scelta.lower() == "s":
    mod = "w"
else:
    mod = "a"

with open("risultati.txt", mod) as f:
    f.write("Array 1:\n")
    f.write(str(arr1) + "\n\n")
    
    f.write("Array 2:\n")
    f.write(str(arr2) + "\n\n")
    
    f.write("Array 3 (somma):\n")
    f.write(str(arr3) + "\n\n")
    
    f.write(f"Somma totale: {somma}\n")
    f.write(f"Somma elementi > 0.5: {somma2}\n")