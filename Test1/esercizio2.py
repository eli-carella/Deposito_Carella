# Funzione conteggio vocali
def conta_vocali(testo):
    vocali = "aeiou"
    num = 0
    #ciclo for su lettere in minuscolo della parola
    for lettera in testo.lower():
        if lettera in vocali:
            num += 1

    return num

v = input("Inserisci una vocale:")
#chimata funzione e stampa
tot=conta_vocali(v)
print(tot)
