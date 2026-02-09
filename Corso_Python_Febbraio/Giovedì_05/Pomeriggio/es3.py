'''
2. Esercizio Avanzato: Sequenza di Fibonacci fino a N
Descrizione: Chiedi all'utente di inserire un numero N. Il
programma dovrebbe stampare la sequenza di Fibonacci fino a N.
Ad esempio, se l'utente inserisce 100, il programma dovrebbe
stampare tutti i numeri della sequenza di Fibonacci minori o
uguali a 100.
'''

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

