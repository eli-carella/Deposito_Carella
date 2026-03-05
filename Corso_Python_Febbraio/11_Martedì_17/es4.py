'''
Scrivete un programma che genera 5 numeri
casuali e li salva su un file, l’utente dovrà cercare di indovinarne almeno 2 oppure
avrà perso.
'''
import random

def scriviNumeriFile(nome_file):
    with open(nome_file, "w") as file:
        numeri_appoggio = []

        while True:
            limite_numeri = 5 #int(input("Inserisci quanti numeri random vuoi generare (min 1 & max 90): "))

            if 90 > limite_numeri > 0:
                while limite_numeri > 0:
                    numero_generato = random.randint(1, 91)

                    if numero_generato not in numeri_appoggio:
                        numeri_appoggio.append(numero_generato)
                        file.write(str(numero_generato) + "\n")
                        limite_numeri -= 1
                break

def leggiNumeriFile(nome_file):
    numeri = []

    with open(nome_file, "r") as file:
        for riga in file:
            numeri.append(int(riga))

    return numeri


scriviNumeriFile("file.txt")
numeri_file = leggiNumeriFile("file.txt")

tentativi_rimasti = int(input("Scegli quanti tentativi vuoi fare: "))
#tentativi_rimasti = 6  # Debug
numeri_giocati = []
numeri_indovinati = 0

while tentativi_rimasti > 0:
    try:
        while True:
            tentativo = int(input("Inserisci il numero: "))

            if 90 > tentativo > 0:
                break
            else:
                print("Numero fuori range!")

    except:
        print("Errore!")

    if tentativo not in numeri_giocati:
        numeri_giocati.append(tentativo)
        tentativi_rimasti -= 1
        print("Tentativi rimasti:", tentativi_rimasti)
    else:
        print("Numero già inserito!")

print("Numeri generati:", numeri_file)

for n in numeri_giocati:
    if n in numeri_file:
        numeri_indovinati += 1
        print("Indovinato:", n)

if numeri_indovinati >= 2:
    print("Hai vinto!")
else:
    print("Hai perso!")
