'''
Dataset: Utilizzare un dataset che registra le vendite di prodotti in diverse
città, includendo le colonne Prodotto, Quantità, Prezzo Unitario e Città.
1. Caricare i dati in un DataFrame.
2. Aggiungere una colonna "Totale Vendite" che sia il risultato del prodotto tra Quantità e Prezzo Unitario.
3. Raggruppare i dati per Prodotto e calcolare il totale delle vendite per ciascun prodotto.
4. Trovare il prodotto più venduto in termini di Quantità.
5. Identificare la città con il maggior volume di vendite totali.
6. Creare un nuovo DataFrame che mostri solo le vendite superiori a un certo valore (es., 1000 euro).
7. Ordinare il DataFrame originale per la colonna "Totale Vendite" in ordine decrescente.
8. Visualizzare il numero di vendite per ogni città.
'''
import pandas as pd

file_path='dataset2.csv'
df = pd.read_csv(file_path)

df["Totale Vendite"] = df["Prezzo Unitario"] * df["Quantità"]

#vendite per prodotto
vendite_per_prodotto = df.groupby("Prodotto")["Totale Vendite"].sum()
print("Totale vendite per prodotto:")
print(vendite_per_prodotto)

# Trovare il prodotto più venduto in termini di Quantità.
df=df.sort_values(by='Quantità', ascending=False)
print(df['Prodotto'][0])

# Città con il maggior volume di vendite totali
citta_top=df.groupby("Città")["Totale Vendite"].sum().idxmax()
print("Città con maggior volume di vendite totali:", citta_top)
print("\n")

# Nuovo DataFrame con vendite superiori a 1000 euro
df_new = df[df["Totale Vendite"] > 1000]

print("Vendite superiori a 1000 euro:")
print(df_new)
print("\n")

# Ordinare il DataFrame per "Totale Vendite" in ordine decrescente
df_ordinato = df.sort_values(by="Totale Vendite", ascending=False)

print("DataFrame ordinato per Totale Vendite (decrescente):")
print(df_ordinato)
print("\n")

# Numero di vendite per ogni città
numero_vendite_citta = df["Città"].value_counts()

print("Numero di vendite per città:")
print(numero_vendite_citta)