'''
Descrizione: Scrivi un programma che chieda all'utente di inserire un numero intero positivo n. Il programma deve poi eseguire le seguenti operazioni:

Utilizzare un ciclo while per garantire che l'utente inserisca un numero positivo. Se l'utente inserisce un numero negativo o zero, il programma deve continuare a chiedere un numero fino a quando non viene inserito un numero positivo.
Utilizzare un ciclo for con range per calcolare e stampare la somma dei numeri pari da 1 a n.
Utilizzare un ciclo for per stampare tutti i numeri dispari da 1 a n.
Utilizzare una struttura if per determinare se n è un numero primo. Un numero primo è divisibile solo per 1 e per se stesso. Il programma deve stampare se n è primo o no.
'''
tentativi=[]
while True:
    
    n = int(input("Inserisci un numero positivo:"))
    tentativi.append(n)
    if(n<=0):
        continue

    #somma
    somma=0
    for i in range(1, n+1):
        if i % 2 == 0:
            somma+=i
    print("la somma dei numeri pari è:", somma)

    #dispari
    dispari=[]
    for i in range(1, n+1):
        if(i%2!=0):
            dispari.append(i)
    print("numeri dispari:", dispari)

    # controllo numero primo
    if n < 2:
        print("Il numero non è primo")
    else:
        primo = True

    for i in range(2, n):
        if n % i == 0:
            primo = False
            break

    if primo:
        print("Il numero è primo")
    else:
        print("Il numero non è primo")

    ripeti = input("Vuoi ripetere?")
    if ripeti == "no":

        print("\nLista tentativi:", tentativi)
        scelta = input("Vuoi visionare, modificare o uscire? (v, m, u)").lower()

        if scelta == "v":
            print("Tentativi inseriti:", tentativi)

        elif scelta == "m":
            pass

        elif scelta == "u":
            print("Programma terminato.")
            break

        else:
            print("Scelta non valida")
        
        break