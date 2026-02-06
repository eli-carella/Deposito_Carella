'''
Definisca una funzione chiamata conta_vocali. 
 
 La funzione deve:
 ricevere una stringa come parametro 
 contare quante vocali contiene (a, e, i, o, u) 
 restituire il numero totale di vocali 
'''
# Funzione conteggio vocali
def conta_vocali(testo:str):
    vocali = "aeiou"
    num = 0
    #ciclo for su lettere in minuscolo della parola
    for lettera in testo.lower():
        if lettera in vocali:
            num += 1

    return num

v = input("Inserisci una parola:")
#chimata funzione e stampa
tot=conta_vocali(v)
print("Il numero totale di vocali è:", tot)
