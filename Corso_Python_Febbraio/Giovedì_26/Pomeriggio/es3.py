'''
1.  Generazione dei Dati: Utilizzare NumPy per generare una serie temporale
di 365 giorni di dati, simulando il numero di visitatori giornalieri in
un parco. Assumere che il numero medio di visitatori sia 2000 con una
deviazione standard di 500. Inoltre, aggiungere un trend crescente nel
tempo per simulare l'aumento della popolarità del parco.
2.  Creazione del DataFrame: Creare un DataFrame pandas con le date come
indice e il numero di visitatori come colonna.
3.  Analisi dei Dati: Calcolare il numero medio di visitatori per mese e la
deviazione standard.
4.  Visualizzazione dei Dati:
Creare un grafico a linee del numero di visitatori giornalieri.
Aggiungere al grafico la media mobile a 7 giorni per mostrare la
tendenza settimanale.
Creare un secondo grafico che mostri la media mensile dei visitatori.
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

giorni = 365
media = 2000
dev_std = 500

# Generazione da distr normale
visitatori = np.random.normal(media, dev_std, giorni)

trend = 1 + 0.01 * np.arange(giorni) # crescita 1% al giorno
visitatori_trend = visitatori * trend

np.arange(365)
