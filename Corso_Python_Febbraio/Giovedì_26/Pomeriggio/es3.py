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




# 3. Analisi dei dati: media e deviazione standard mensile
media_mensile = df.resample("M").mean()
dev_std_mensile = df.resample("M").std()

print("Media mensile visitatori:")
print(media_mensile)
print("\nDeviazione standard mensile:")
print(dev_std_mensile)

# 4. Visualizzazione dei dati

# 🔹 Calcolo media mobile a 7 giorni
df["Media Mobile 7gg"] = df["Visitatori"].rolling(window=7).mean()

# Grafico 1: Visitatori giornalieri + media mobile
plt.figure(figsize=(12, 5))
plt.plot(df.index, df["Visitatori"], label="Visitatori giornalieri")
plt.plot(df.index, df["Media Mobile 7gg"], color='red', linewidth=2, label="Media mobile 7 giorni")
plt.title("Visitatori Giornalieri con Media Mobile")
plt.xlabel("Data")
plt.ylabel("Numero di visitatori")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Grafico 2: Media mensile dei visitatori
plt.figure(figsize=(10, 4))
plt.plot(media_mensile.index, media_mensile["Visitatori"], marker='o', linestyle='-')
plt.title("Media Mensile dei Visitatori")
plt.xlabel("Mese")
plt.ylabel("Numero medio di visitatori")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
