'''
Descrizione: Gli studenti dovranno generare un DataFrame di vendite che
include i seguenti campi: "Data", "Città", "Prodotto" e "Vendite". 
I dati devono essere generati per un periodo di un mese, con vendite registrate
per tre diverse città e tre tipi di prodotti.
1. Generazione dei Dati: Utilizzare numpy per creare un set di dati casuali.
2. Creazione della Tabella Pivot: Creare una tabella pivot per analizzare
le vendite medie di ciascun prodotto per città.
3. Applicazione di GroupBy: Utilizzare il metodo groupby per calcolare le
vendite totali per ogni prodotto.
'''

import numpy as np
import pandas as pd

start = np.datetime64('2026-02-01')
end = np.datetime64('2026-03-01')

dates = np.arange(start, end, dtype='datetime64[D]')
#print(dates)

citta = np.array(["Roma", "Milano", "Napoli"])
prodotti = np.array(["Laptop", "Smartphone", "Tablet"])

n = len(dates)

citta_random = np.random.choice(citta, n)
prodotti_random = np.random.choice(prodotti, n)
vendite = np.random.randint(10, 100, n)

#dizionario con colonne np array create
dataset_diz = {
'Prodotto': prodotti_random,
'Vendite': vendite,
'Città': citta_random,
'Data': dates
}

df = pd.DataFrame(dataset_diz)
print("\nDataframe\n")
print(df)

# Creazione della tabella pivot
pivot_table = df.pivot_table(index='Prodotto', columns='Città', values='Vendite', aggfunc='mean')
print("\nPivot table\n")
print(pivot_table)

grouped_df  = df.groupby("Prodotto")["Vendite"].sum()
print("\nDataframe grouped\n")
print(grouped_df)