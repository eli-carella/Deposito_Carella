'''
1.Base / Numeri pari e dispari o sequenza Descrizione:
Scrivi un programma che chiede all'utente di inserire un numero o una stringa scegliendo prima quale. 
Il programma dovrebbe determinare se il numero è pari o dispari e stampare il risultato e se deve ripetere o stampare e poi ripetere.
'''

while True:
    scelta = input("Vuoi inserire un numero o una stringa? (numero/stringa): ").lower()
    if scelta=="numero":
        n = int(input("Inserisci un numero:"))

        if(n%2==0):
            print("il numero è pari ", n)
        else:
            print("il numero è dispari ", n)
    
    elif scelta=="stringa":
        testo = input("Inserisci una stringa:")
        n=len(testo)
        if(n%2==0):
            print("la stringa è pari ", n)
        else:
            print("la stringa è dispari ", n)

    else:
        print("Scelta non valida.")

    x = input("vuoi continuare?")
    if x=="no":
        break

