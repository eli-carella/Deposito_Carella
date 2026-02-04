# Chiedi all'utente di inserire un numero. 
# Il programma dovrebbe controllare se il numero inserito è primo/pari o no. Se è primo, lo salva e stampa "Il numero è primo". 
# Altrimenti, stampa "Il numero non è primo", si ferma quando ha 5 numeri primi. 

numeri_primi = []

while len(numeri_primi) < 5:
    numero = int(input("Inserisci un numero: "))

    if numero < 2:
        print("Il numero non è primo")
        continue

    # Controllo se il numero è primo
    primo = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            primo = False
            break

    if primo:
        numeri_primi.append(numero)
        print("Il numero è primo")
    else:
        print("Il numero non è primo")

print("Numeri primi:", numeri_primi)


'''
numeri_pari = []

while len(numeri_pari) < 5:
    numero = int(input("Inserisci un numero: "))

    if numero % 2 == 0:  # Controllo se il numero è pari
        numeri_pari.append(numero)
        print("Il numero è pari")
    else:
        print("Il numero è dispari")

print("Numeri pari:", numeri_pari)

'''
