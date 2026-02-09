'''
1. Esercizio Base: Indovina il numero
Descrizione: Scrivi un programma che genera un numero casuale
tra 1 e 100 (inclusi). L'utente deve indovinare quale numero è
stato generato. Dopo ogni tentativo, il programma dovrebbe
dire all'utente se il numero da indovinare è più alto o più
basso rispetto al numero inserito. Il gioco termina quando
l'utente indovina il numero o decide di uscire.
'''
import random 
#funzioe che confronta numero segreto e tentativo
def confronto(a:int, b:int):
    if a > b:
        print("Il numero da indovinare è più alto")
        return False
    elif a<b:
        print("Il numero da indovinare è più basso")
        return False
    else:
        print("Il numero è corretto")
        return True

# Genera numero casuale tra 1 e 100
numero_segreto = random.randint(1, 100)
while True:
    
    tentativo = int(input("Indovina numero tra 1 e 100"))
    #chiamata funzione
    risultato = confronto(numero_segreto, tentativo)

    #se corretto esce
    if risultato:
        break
    
    #continua o esci
    ripeti = input("Vuoi uscire? (s/n)")
    if ripeti == "s":
        break
            


