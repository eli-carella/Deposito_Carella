import math
import time

# DECORATORI

# Ripete l'esecuzione del programma
def ripeti_programma(func):
    def wrapper():
        while True:
            func()
            scelta = input("\nVuoi ripetere il programma? (s/n): ").lower()
            if scelta != "s":
                print("Programma terminato.")
                break
    return wrapper


# Misura il tempo di esecuzione
def misura_tempo(func):
    def wrapper(*args, **kwargs):
        inizio = time.time()
        risultato = func(*args, **kwargs)
        fine = time.time()
        print(f"\nTempo di esecuzione: {fine - inizio:.4f} secondi")
        return risultato
    return wrapper


# Formatta l'output del titolo
def stampa_titolo(func):
    def wrapper(*args, **kwargs):
        print("\n" + "=" * 40)
        print(func.__name__.upper())
        print("=" * 40)
        return func(*args, **kwargs)
    return wrapper


# FUNZIONI

# inserimento dati in lista temperature
def inserisci_temperature():
    giorni = int(input("Inserisci il numero dei giorni: "))
    temperature = []

    for i in range(giorni):
        t = float(input(f"Inserisci la temperatura del giorno {i+1}: "))
        temperature.append(t)

    return temperature

# calcolo valore medio
def calcola_media(lista):
    somma = 0
    for valore in lista:
        somma += valore
    return somma / len(lista)

# calcolo deviazione standard
def deviazione_standard(lista, media):
    somma = 0
    for valore in lista:
        somma += (valore - media) ** 2
    return math.sqrt(somma / len(lista))


# FUNZIONI DECORATE
#confronto valori con la media
@stampa_titolo
def confronto_con_media(lista, media):
    for i in range(len(lista)):
        if lista[i] > media:
            stato = "sopra la media"
        elif lista[i] < media:
            stato = "sotto la media"
        else:
            stato = "uguale alla media"

        print(f"Giorno {i+1}: {lista[i]}°C → {stato}")

# classificazioni giorni in 3 fasce in base a media e deviazione standard 
@stampa_titolo
def classifica_giorni(lista, media, dev_std):
    for i in range(len(lista)):
        if lista[i] > media + dev_std:
            stato = "molto alta"
        elif lista[i] < media - dev_std:
            stato = "molto bassa"
        else:
            stato = "normale"

        print(f"Giorno {i+1}: {lista[i]}°C → {stato}")


# FUNZIONE PRINCIPALE
# Main in cui ci sono i calcoli tramite le funzioni 
@ripeti_programma
@misura_tempo
def main():
    temperature = inserisci_temperature()

    media = calcola_media(temperature)
    dev_std = deviazione_standard(temperature, media)

    print("\nTemperature inserite:")
    for t in temperature:
        print(t, "°C")

    print(f"\nTemperatura media: {media:.2f} °C")
    print(f"Deviazione standard: {dev_std:.2f} °C")

    confronto_con_media(temperature, media)
    classifica_giorni(temperature, media, dev_std)

#esecuzione programma main
main()
