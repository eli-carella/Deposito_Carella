'''
Scrivere un programma che genera 5 numeri casuali e li salva su un file.
L'utente dovrà cercare di indovinarne almeno 2 oppure avrà perso.

# In collaborazione con Fabio D'Alessandro, Elisabetta Carella e Stefano Romaniello
'''

import random

NOME_FILE = "file.txt"

def scriviNumeriFile(nome_file):
    result = ""
    numeri_appoggio = []
    while True:  
        limite_numeri = int(input("Inserisci quanti numeri random vuoi generare (min 1 & max 90): ")) 
        if 90 > limite_numeri > 0:
            while limite_numeri > 0:
                numero_generato = random.randint(1, 91)
                if numero_generato not in numeri_appoggio:
                    numeri_appoggio.append(numero_generato)
                    limite_numeri -= 1
            break

    for i in range(len(numeri_appoggio)):

        if i != len(numeri_appoggio)-1:
            result += str(numeri_appoggio[i]) + ","
        else:
            result += str(numeri_appoggio[i])

    with open(NOME_FILE, "w") as file:
        file.write(result)

def leggiNumeriFile(nome_file):
    righe = []   
    with open(nome_file, "r") as file:
        contenuto = file.read()
    righe = contenuto.split(",")
    return righe

print("SuperEnalotto")
tentativi_rimasti = int(input("Scegli quanti tentativi vuoi fare: "))

scriviNumeriFile(NOME_FILE)
numeri_file = leggiNumeriFile(NOME_FILE)
print("righe file: ", numeri_file)
print(numeri_file)
print(type(numeri_file[0]).__name__)
print(numeri_file[0])

numeri_indovinati = 0
numeri_inseriti = []
while tentativi_rimasti > 0:
    try:
        while True:
            tentativo = int(input("Inserici il numero: "))
            if 90 > tentativo > 0:
                break
            else:
                print("Numero fuori range!")
    except:
        print("errore!")

    if tentativo not in numeri_inseriti:
        numeri_inseriti.append(str(tentativo))
        tentativi_rimasti -= 1
        print(tentativi_rimasti)
    else:
        print("Numero già inserito!")


for n in numeri_file:
    if n in numeri_inseriti:
        numeri_indovinati += 1
        
print("hai indovinato: ", numeri_indovinati)


if numeri_indovinati >= 2:
    print("Hai vinto!")
else:
    print("Hai perso!")