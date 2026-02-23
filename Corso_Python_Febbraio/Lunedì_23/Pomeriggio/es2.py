'''
Esercizio su NumPy Slicing
Consegna:
1.Crea un array NumPy 1D di 20 numeri interi casuali compresi
tra 10 e 50.
2.Utilizza lo slicing per estrarre i primi 10 elementi
dell'array.
3.Utilizza lo slicing per estrarre gli ultimi 5 elementi
dell'array.
4.Utilizza lo slicing per estrarre gli elementi dall'indice 5
all'indice 15 (escluso).
5.Utilizza lo slicing per estrarre ogni terzo elementodell'array.
6.Modifica, tramite slicing,gli elementi dall'indice 5
all'indice 10 (escluso) assegnando loro il valore 99.
7.Stampa l'array originale e tutti i sottoarray ottenuti tramite slicing.
Obiettivo:
Esercitarsi nell'utilizzo dello slicing di NumPy per estrarre e
modificare sottoarray specifici da un array più grande.
'''
import numpy as np
#20 numeri interi casuali tra 10 e 50
data = np.random.randint(10, 51, 20)
#primi 10
print(data[:10])
#ultimi 5
print(data[-5:])
#dal 5 al 15 escluso
print(data[5:15])
#ogni 3 
print(data[::3])
#riassegna 88 dal 5 al 10 escluso
data[5:10]=99
#stampa array modificato
print(data)
