#funzione calcolo seq fibonacci fino a N
def fibonacci_fino_a(N: int):
    a = 0
    b = 1
    # ciclo su tutti int da 0 a N
    while a <= N:
        print(a, end=" ")
        a, b = b, a + b

N = int(input("Inserisci un numero: "))
#chiamata funzione
fibonacci_fino_a(N)

