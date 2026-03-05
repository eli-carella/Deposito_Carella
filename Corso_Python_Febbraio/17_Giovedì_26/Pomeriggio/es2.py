'''
Creato un DataFrame pandas con tre colonne: altezza, peso e età di un gruppo
di persone, normalizza i dati di altezza e peso usando la normalizzazione min-
max (ridimensiona i valori in modo che varino tra 0 e 1).
Assicurati di lasciare inalterata la colonna età; mostra il DataFrame
originale e quello modificato.
Fornisci un codice che:
1. Carichi il DataFrame (puoi assumere che i dati siano già disponibili in un
DataFrame chiamato df).
2. Applichi la normalizzazione min-max alle colonne altezza e peso.
3. Stampa sia il DataFrame originale sia quello modificato per compararli.
'''
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

altezza = np.random.randint(150, 190, 100)
peso = np.random.randint(18, 80, 100)
eta = np.random.randint(45, 95, 100)

data = {
    'Altezza': altezza,
    'Peso': peso,
    'Eta': eta
}

df = pd.DataFrame(data)
print("DataFrame originale:")
print(df)

#copia primo dataframe
df_norm = df.copy()
# normalizzazione dei dati  (x-x_min)/(x_max-x_min) valori compresi tra 0-1
df_norm['Altezza'] = (df['Altezza'] - df['Altezza'].min()) / (df['Altezza'].max() - df['Altezza'].min())
df_norm['Peso'] = (df['Peso'] - df['Peso'].min()) / (df['Peso'].max() - df['Peso'].min())
print("\nDataFrame nuovo:")
print(df_norm)

# istogramma
axes = df.hist(bins=10, figsize=(10, 6), edgecolor='black')

for ax, colonna in zip(axes.flatten(), df.columns):
    
    valori = df[colonna]
    
    media = valori.mean()
    mediana = valori.median()
    minimo = valori.min()
    massimo = valori.max()
    
    ax.axvline(media, linestyle='-', linewidth=2, label='Media')
    ax.axvline(mediana, linestyle='--', linewidth=2, label='Mediana')
    ax.axvline(minimo, linestyle=':', linewidth=2, label='Min')
    ax.axvline(massimo, linestyle='-.', linewidth=2, label='Max')
    
    ax.legend()

plt.suptitle("Distribuzione di Altezza, Peso ed Età")
plt.tight_layout()
plt.show()