'''
create un programma che richiede all’utente tre numeri e verifica la presenza di almeno due numeri uguali, 
se non ci sono ci restituisce il numero più grande dei tre
'''

# Richiesta dei tre numeri in input
n1 = int(input("Inserisci il primo numero: "))
n2 = int(input("Inserisci il secondo numero: "))
n3 = int(input("Inserisci il terzo numero: "))

# Verifica se almeno due numeri sono uguali
if n1 == n2 or n1 == n3 or n2 == n3:
    print("Ci sono almeno due numeri uguali.")
else:
    # confronto ciascuno con gli altri e trovo max
    if n1 > n2 and n1 > n3:
        massimo = n1
    elif n2 > n1 and n2 > n3:
        massimo = n2
    else:
        massimo = n3

    print(f"Non ci sono numeri uguali. Il numero più grande è {massimo}.")
