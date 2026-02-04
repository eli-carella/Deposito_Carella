# Chiedi all'utente di inserire un numero. 
# Il programma dovrebbe quindi fare un conto alla rovescia a partire da quel numero fino a zero, 
# stampando ogni numero e chiederti se vuoi ripetere o no.

controllore = True

while controllore:
    numero = int(input("Inserisci un numero: "))

    for i in range(numero, -1, -1):
        print(i)

    esci = input("Vuoi uscire - Sì o NO")
    if esci.lower() == "sì":
        controllore = False
    else:
        controllore = True
