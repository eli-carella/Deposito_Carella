'''
Hai a disposizione un dataset, che devi autogenerare,
contenuto in un DataFrame pandas con una singola colonna
temperature che rappresenta la temperatura giornaliera in
una città per un mese.
Scrivi un programma Python che calcoli e stampi le seguenti
statistiche:
La temperatura massima
La temperatura minima
La temperatura media
La mediana delle temperature
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

start = np.datetime64('2026-02-01')
end = np.datetime64('2026-03-01')

dates = np.arange(start, end, dtype='datetime64[D]')
temperature = np.random.randint(-6, 32, len(dates))


dataset_diz = {
    'Date': dates,
    'Temperature': temperature
}

df = pd.DataFrame(dataset_diz)

# Calcolo valori
temp_max = df['Temperature'].max()
temp_min = df['Temperature'].min()
temp_mean = df['Temperature'].mean()
temp_median = df['Temperature'].median()

# Stampa dei risultati
print(f"Temperatura massima: {temp_max}")
print(f"Temperatura minima: {temp_min}")
print(f"Temperatura media: {temp_mean:.2f}")
print(f"Mediana delle temperature: {temp_median}")

plt.figure(figsize=(12, 6))
# Grafico lineare delle temperature
plt.plot(df['Date'], df['Temperature'], marker='o', linestyle='-', color='tab:blue', label='Temperatura')
plt.title('Temperature giornaliere Febbraio 2026')
plt.xlabel('Data')
plt.ylabel('Temperatura (°C)')
# Griglia e legenda
plt.grid(linestyle='--', alpha=0.6)
plt.legend()
plt.xticks(rotation=45) #rotazione etichetta data
# Mostra il grafico
plt.tight_layout()
plt.savefig('scatter_plot.png')
plt.show()


### Istogramma
plt.figure(figsize=(10, 6))
# Creazione dell'istogramma
plt.hist(df['Temperature'], bins=15, color='skyblue', edgecolor='black')  # bins = numero di intervalli
# Titolo e etichette
plt.title('Distribuzione delle temperature Febbraio 2026')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Frequenza')
# Griglia
plt.grid(axis='y', linestyle='--', alpha=0.7)
# Linee verticali per le statistiche
plt.axvline(temp_max, color='red', linestyle='--', linewidth=1, label=f'Max: {temp_max}')
plt.axvline(temp_min, color='blue', linestyle='--', linewidth=1, label=f'Min: {temp_min}')
plt.axvline(temp_mean, color='orange', linestyle='-', linewidth=1, label=f'Media: {temp_mean:.2f}')
plt.axvline(temp_median, color='green', linestyle='-', linewidth=1, label=f'Mediana: {temp_median}')
plt.legend()
plt.savefig('histo.png')
plt.show()