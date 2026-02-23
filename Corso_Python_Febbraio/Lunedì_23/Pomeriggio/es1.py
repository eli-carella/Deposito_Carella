'''
Crea un array NumPy utilizzando arange e
verifica il tipo di dato (dtype) e la forma
(shape) dell'array.
Esercizio:
1.Utilizza la funzione np.arange per creare
un array di numeri interi da 10 a 49.
2.Verifica il tipo di dato dell'array e
stampa il risultato.
3.Cambia il tipo di dato dell'array in
float64 e verifica di nuovo il tipo di
dato.
4.Stampa la forma dell'array.
'''
import numpy as np
data = np.arange(10, 50)
print('Array 10-49', data)
print(f'Tipo di dato {data.dtype}')
data_float = data.astype(float)
print(f'Tipo di dato nuovo convertito {data_float.dtype}')
print(f'Forma array: {data_float.shape}')
