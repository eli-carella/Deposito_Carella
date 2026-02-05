'''
Avanzato/ Fattori comuni Descrizione:
Chiedi all'utente di inserire due numeri. 
Il programma dovrebbe determinare e stampare i fattori comuni di entrambi i numeri. 
Se non ci sono fattori comuni oltre 1, dovrebbe stampare "I numeri sono coprimi". 
La stessa cosa ma anche per due stringhe (.equal ) e chiedere se deve ripetere ma sono “ complementari” solo se hanno tutte le lettere in comune (es:abs/ sab)
'''

while True:
    a = int(input("Inserisci il primo numero: "))
    b = int(input("Inserisci il secondo numero: "))

    fattori_comuni = []

    limite = min(a, b)

    for i in range(2, limite + 1):
        if a % i == 0 and b % i == 0:
            fattori_comuni.append(i)

    if len(fattori_comuni) == 0:
        print("I numeri sono coprimi")
    else:
        print("Fattori comuni:", fattori_comuni)

    ripeti = input("Vuoi ripetere?")
    if ripeti == "no":
        break


