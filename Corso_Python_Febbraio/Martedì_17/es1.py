'''
Scrivete un gioco in cui il Giocatore1 inserisce un numero da 1 a 100 e il Giocatore2 ha 5 tentativi per indovinare il numero.
Il programma fornisce suggerimenti (troppo alto, troppo basso), termina quando l'utente indovina correttamente, quando i tentativi finiscono o se scrive "mi arrendo".
'''

import random


def giocatore1():
    numero1 = random.randint(1, 100)
    return numero1

def giocatore2(numero1):
    numero2 = input("Giocatore 2 inserisci un numero da 1 a 100 o 'mi arrendo' per arrenderti: ")
    
    if numero2 == 'mi arrendo':
        return True
    
    numero2 = int(numero2)
    if numero2 == numero1:
        print("Hai indovinato!")
        return True
    elif numero2 > numero1:
        print("Troppo alto!")
        return False
    else:
        print("Troppo basso!")
        return False


tentativi = 5
numero_segreto = giocatore1()

while tentativi >= 0:
    if not giocatore2(numero_segreto):
        tentativi -= 1
        if tentativi == -1:
            print("Hai perso!")
    else:
        break