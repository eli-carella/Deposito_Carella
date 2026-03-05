import numpy as np

# Creazione di una matrice quadrata
A = np.array([[1, 2], [3, 4]])

# Calcolo dell'inversa della matrice
A_inv = np.linalg.inv(A)
print("Inversa di A:\n", A_inv)

## norma di un vettore

# Creazione di un vettore
v = np.array([3, 4])
# Calcolo della norma del vettore
norm_v = np.linalg.norm(v)
print("Norma di v:", norm_v)
# Output: 5.0


## solve sistema lineare di eq
# Creazione della matrice A e del vettore B
A = np.array([[3, 1], [1, 2]])
B = np.array([9, 8])
# Risoluzione del sistema di equazioni Ax = B
x = np.linalg.solve(A, B)
print("Soluzione x:", x) # Output: [2. 3.]

# Creazione di un segnale
# crea un segnale sintetico composto da due frequenze diverse e poi lo analizza per vedere quali frequenze contiene.
t = np.linspace(0, 1, 400)
sig = np.sin(2 * np.pi * 50 * t) + np.sin(2 * np.pi * 120 * t)

# Calcolo della Trasformata di Fourier
fft_sig = np.fft.fft(sig)

# Frequenze associate
freqs = np.fft.fftfreq(len(fft_sig))

print("Trasformata di Fourier:", fft_sig)
print("Frequenze associate:", freqs)

### broadcasting
arr = np.array([1, 2, 3, 4])
scalar = 10
# Broadcasting aggiunge lo scalare a ogni elemento dell'array
result = arr + scalar
print(result) # Output: [11 12 13 14]

