'''L'obiettivo di questo esercizio è generare un set di dati di serie temporali
utilizzando NumPy, analizzarli con pandas e visualizzare i risultati usando
Matplotlib. Gli studenti dovranno eseguire le seguenti operazioni:


Generazione dei Dati: Utilizzare NumPy per generare una serie temporale
di 365 giorni di dati, simulando il numero di visitatori giornalieri in
un parco. Assumere che il numero medio di visitatori sia 2000 con una
deviazione standard di 500. Inoltre, aggiungere un trend crescente nel
tempo per simulare l'aumento della popolarità del parco.

Creazione del DataFrame: Creare un DataFrame pandas con le date come
indice e il numero di visitatori come colonna.

Analisi dei Dati: Calcolare il numero medio di visitatori per mese e la
deviazione standard.

Visualizzazione dei Dati:

Creare un grafico a linee del numero di visitatori giornalieri.

Aggiungere al grafico la media mobile a 7 giorni per mostrare la
tendenza settimanale.

Creare un secondo grafico che mostri la media mensile dei visitatori'''
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
date_2024 = pd.date_range(start='2024-01-01', end='2024-12-31')
giorni=np.arange(1,367)
#print(giorni)
'''
nvisitatori=np.random.normal(2000,500,len(giorni))
#print(nvisitatori)
incremento=0.1
nvisitatori=nvisitatori*(1+incremento*giorni)
'''
num_giorni = len(giorni)#365
nvisitatori = np.random.normal(2000, 500, num_giorni)
incremento = 0.1  # +10% nell'anno

# Fattore giorno per giorno da 1 a 1+incremento
fattore = 1 + incremento * (np.arange(num_giorni)/num_giorni)
nvisitatori_trend = nvisitatori * fattore

'''df=pd.DataFrame({
    'giorni': giorni,
    'nvisitatori':nvisitatori
})'''

nvisitatori = nvisitatori.astype(int)
print(nvisitatori.dtype)
print(nvisitatori)

dfcontrend = pd.DataFrame({
    "Visitatori": nvisitatori
}, index=date_2024)
#media_mensile = dfcontrend.resample("ME").mean()
dfcontrend["Mese"] = dfcontrend.index.month
media_mensile = dfcontrend.groupby("Mese")["Visitatori"].mean().reset_index()
standard = dfcontrend.groupby("Mese")["Visitatori"].std().reset_index()
#dev_std_mensile = dfcontrend.resample("ME").std()

print("Media mensile visitatori:")
print(media_mensile)
print("\nDeviazione standard mensile:")
print(standard)

dfcontrend["Media Mobile 7gg"] = dfcontrend["Visitatori"].rolling(window=7).mean()


sns.set(style="whitegrid")
plt.figure(figsize=(12,5))
sns.lineplot(data=dfcontrend, x=dfcontrend.index, y="Visitatori", label="Visitatori giornalieri")
sns.lineplot(data=dfcontrend, x=dfcontrend.index, y="Media Mobile 7gg", label="Media Mobile 7gg", color="red")
plt.title("Visitatori Giornalieri con Media Mobile a 7 Giorni")
plt.xlabel("Giorno")
plt.ylabel("Numero di Visitatori")
plt.legend()
plt.show()



sns.set(style="whitegrid")
plt.figure(figsize=(10,4))
sns.lineplot(data=media_mensile, x="Mese", y="Visitatori", marker="o")
plt.title("Media Mensile dei Visitatori")
plt.xlabel("Mese")
plt.ylabel("Numero Medio Visitatori")
plt.xticks(range(1,13))
plt.show()