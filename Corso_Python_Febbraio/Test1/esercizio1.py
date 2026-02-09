"""
Chieda all’utente di inserire un numero intero positivo. 
Usi un ciclo for per stampare tutti i numeri da 1 fino al numero inserito. 
Per ogni numero: 
stampi "pari" se il numero è pari 
stampi "dispari" se il numero è dispari 
Se l’utente inserisce un numero minore o uguale a zero, il programma deve stampare un messaggio di errore.
"""

numero = int(input("Inserisci un numero intero positivo: "))
#controllo che il numero sia positivo, con negativo stampa errore
if numero <= 0:
    print("Errore: il numero deve essere maggiore di zero.")
else:
    #ciclo su numeri da 1 a n
    for i in range(1, numero + 1):
        #controllo se è pari o dispari e stampa il risultato
        if i % 2 == 0:
            print(i, "pari")
        else:
            print(i, "dispari")
