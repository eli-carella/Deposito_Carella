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
            


