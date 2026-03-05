'''
Obiettivo: Familiarizzare con le operazioni di base per l'esplorazione dei dati usando pandas.
Dataset: Utilizzare un dataset di esempio che include le seguenti informazioni su
un gruppo di persone: Nome, Età, Città e Salario.
1. Caricare i dati in un DataFrame autogenerandoli casualmente .
2. Visualizzare le prime e le ultime cinque righe del DataFrame.
3. Visualizzare il tipo di dati di ciascuna colonna.
4. Calcolare statistiche descrittive di base per le colonne numeriche (media,
mediana, deviazione standard).
5. Identificare e rimuovere eventuali duplicati.
6. Gestire i valori mancanti sostituendoli con la mediana della rispettiva
colonna.
7. Aggiungere una nuova colonna chiamata "Categoria Età" che classifica le
persone come "Giovane", "Adulto" o "Senior" basandosi sull'età (es., 0-18
anni: Giovane, 19-65 anni: Adulto, oltre 65 anni: Senior).
8. Salvare il DataFrame pulito in un nuovo file CSV.
'''
import pandas as pd
file_path='dataset.csv'
df = pd.read_csv(file_path)
#stampa prime 5 e ultime 5
print(df.head())
print(df[-5:])

#stampa dtype di ogni colonna
print(df.dtypes)
print(df['Nome'].dtype)

#stampa media,mediana, 
print('Media età: ', df['Età'].mean())
print('Mediana età: ', df['Età'].median())
print('Std età: ', df['Età'].std())
print('Media salario: ', df['Salario'].mean())
print('Mediana salario: ', df['Salario'].median())
print('Std salario: ', df['Salario'].std())

#rimozione duplicati
df = df.drop_duplicates()

#gestire valori mancanti con sostituzione mediana
df['Età'].fillna(df['Età'].median(), inplace=True)
df['Salario'].fillna(df['Salario'].median(), inplace=True)


# funzione che divide in 3 categorie
def categoria_eta(eta):
    if eta <= 18:
        return "Giovane"
    elif eta <= 65:
        return "Adulto"
    else:
        return "Senior"

# Crea la nuova colonna applicando la funzione
df["Categoria Età"] = df["Età"].apply(categoria_eta)

# salva su file csv index=False per evitare di salvare la colonna dell'indice
df.to_csv("dataset_pulito.csv", index=False)