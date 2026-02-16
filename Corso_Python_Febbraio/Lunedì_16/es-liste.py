#######esercizi
'''
Scrivete un programma che chiede all'utente una
serie di parole e restituisce solo le vocali e l’indice della vocale all’interno delle parole.
'''
frase = input("Inserisci frase: ")

vocali = "aeiou"

parole = frase.lower().split()

for parola in parole:
    print(f"\nParola: {parola}")
    indice = 0
    for lettera in parola:
        if lettera in vocali:
            print("lettera ", lettera, "indice ", indice)
        indice+=1

frase = input("Inserisci frase: ")
parole = frase.split()

vocali = "aeiouAEIOU"

for parola in parole:
    print(f"\nParola: {parola}")
    for indice, lettera in enumerate(parola):
        if lettera in vocali:
            print(f"Vocale: {lettera} - Indice: {indice}")
