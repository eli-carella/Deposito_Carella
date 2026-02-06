'''
Analisi delle temperature:
1. Crea una variabile giorni da input per stabilire per quanti giorni si vuole misurare la temperatura
2. Crea una lista delle temperature da aggiungere ogni volta da input dall'utente (una per ogni giorno) e salva in una lista
3. Funzione per calcolare la media e per la deviazione standard
4. Restiture per ogni giorno se la temperatura è superiore, inferiore, uguale alla media5. 
5. Classificare ogni giorno in tre fasce (temperatura normale, molto alta, molto bassa) in base alla deviazione standard
'''

import math

# variebile input giorni
giorni = int(input("Inserisci il numero dei giorni: \n"))

# inserimento dati in lista temperature
temperature = []
for i in range(giorni):
    t = float(input(f"Inserisci la temperatura del giorno {i+1}: "))
    temperature.append(t)


# calcolo media
def calcola_media(lista):
    somma = 0
    for valore in lista:
        somma += valore
    return somma / len(lista)

#calcolo deviazione standard
def deviazione_standard(lista, media):
    somma = 0
    for valore in lista:
        somma += (valore - media) ** 2
    return math.sqrt(somma / len(lista))

#confronto valori con la media
def confronto_con_media(lista, media):
    for i in range(len(lista)):
        if lista[i] > media:
            print(f"Giorno {i+1}: {lista[i]}°C → sopra la media")
        elif lista[i] < media:
            print(f"Giorno {i+1}: {lista[i]}°C → sotto la media")
        else:
            print(f"Giorno {i+1}: {lista[i]}°C → uguale alla media")

#classificazioni giorni in base a media e deviazione standard
def classifica_giorni(lista, media, dev_std):
    for i in range(len(lista)):
        if lista[i] > media + dev_std:
            stato = "molto alta"
        elif lista[i] < media - dev_std:
            stato = "molto bassa"
        else:
            stato = "normale"

        print(f"Giorno {i+1}: {lista[i]}°C → {stato}")


# chiamata funzioni
media = calcola_media(temperature)
dev_std = deviazione_standard(temperature, media)

# stampa output
print("\nTemperature inserite:")
for t in temperature:
    print(t, "°C")

print("\nTemperatura media:", media, "°C")
print("Deviazione standard:", dev_std, "°C")

print("\nConfronto con la media:")
confronto_con_media(temperature, media)

print("\nClassificazione dei giorni:")
classifica_giorni(temperature, media, dev_std)