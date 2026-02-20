'''
scrivete un programma che utilizza una funzione che accetta
come parametro una stringa passata dall’utente e restituisce in
risposta se è palindroma o no.
Esempio:
‘I topi non avevano nipoti’ è palindroma
‘Ciao’ non è palindroma
'''

def palindroma(testo):

    testo_new=""
    for carattere in testo.lower():
        if carattere.isalpha():
            testo_new+=carattere

    if testo_new == testo_new[::-1]:
        print("palindroma")
    else:
        print("non è palindroma")


while True:
    frase = input("Inserisci una frase: ")
    palindroma(frase)

    scelta = input("\n vuoi continuare?(s/n)")
    if scelta == "n":
        break


