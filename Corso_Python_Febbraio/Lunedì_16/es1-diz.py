'''
stringa, che restituisce freq. di comparsa carattere nella stringa

Scrivete un programma che chiede una stringa all’utente e
restituisce un dizionario rappresentante la "frequenza di
comparsa" di ciascun carattere componente la stringa.
Esempio:
Stringa "ababcc",
Risultato
{"a": 2, "b": 2, "c": 2}
'''

stringa = input("Inserisci una stringa: ")

frequenze = {}

for carattere in stringa:
    key=carattere
    if key in frequenze:
        frequenze[key] += 1
    else:
        frequenze[key] = 1

print(frequenze)

#diz = {carattere: stringa.count(carattere) for carattere in stringa}
