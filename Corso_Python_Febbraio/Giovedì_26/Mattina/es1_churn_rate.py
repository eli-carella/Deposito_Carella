'''
Obiettivo: Utilizzare pandas e numpy per esplorare, pulire, trasformare e analizzare un dataset di clienti della compagnia di
telecomunicazioni. L'esercizio mira a costruire un modello predittivo di base per la churn rate e scoprire correlazioni tra
vari attributi del cliente e la loro fedeltà.
Dataset:
ID_Cliente: Identificativo unico per ogni cliente
Età: Età del cliente
Durata_Abonnamento: Quanti mesi il cliente è stato abbonato
Tariffa_Mensile: Quanto il cliente paga al mese
Dati_Consumati: GB di dati consumati al mese
Servizio_Clienti_Contatti: Quante volte il cliente ha contattato il servizio clienti
Churn: Se il cliente ha lasciato la compagnia (Sì/No)
1. Caricamento e Esplorazione Iniziale:
Caricare i dati da un file CSV.
Utilizzare info(), describe(), e value_counts() per esaminare la distribuzione dei dati e identificare colonne con
valori mancanti.
2. Pulizia dei Dati:
Gestire i valori mancanti in modo appropriato, considerando l'imputazione o la rimozione delle righe.
Verificare e correggere eventuali anomalie nei dati (es. età negative, tariffe mensili irrealistiche).
3. Analisi Esplorativa dei Dati (EDA):
Creare nuove colonne che potrebbero essere utili, come Costo_per_GB (tariffa mensile divisa per i dati consumati).
Utilizzare groupby() per esplorare la relazione tra Età, Durata_Abonnamento, Tariffa_Mensile e la Churn.
Utilizzare metodi come corr() per identificare possibili correlazioni tra le variabili.
4. Preparazione dei Dati per la Modellazione:
Convertire la colonna Churn in formato numerico (0 per "No", 1 per "Sì").
Normalizzare le colonne numeriche usando numpy per prepararle per la modellazione.
5. Analisi Statistica e Predittiva:
Implementare un semplice modello di regressione logistica usando scikit-learn per predire la probabilità di churn basata
su altri fattori.
Valutare la performance del modello attraverso metriche come l'accuratezza e l'AUC (Area Under Curve).
'''

import numpy as np
import pandas as pd

file_path='dataset.csv'
df = pd.read_csv(file_path)

# 1) esplorazioni iniziale
df.info()
df.describe()
df.value_counts()

#### 2) gestione valori mancanti

# riempio variabile numeriche con mediana e meadia
df['Età'].fillna(df['Età'].median(), inplace=True)
df['Tariffa_Mensile'].fillna(df['Tariffa_Mensile'].mean(), inplace=True)
df['Dati_Consumati'].fillna(df['Dati_Consumati'].median(), inplace=True)

# variabile categorica churn con moda per valori mancanti
df['Churn'].fillna(df['Churn'].mode()[0], inplace=True)


# filtri per colonne numeriche
df = df[(df['Età'] >= 0)]
df = df[(df['Tariffa_Mensile'] > 0) & (df['Tariffa_Mensile'] <= 200)]
df = df[df['Durata_Abbonamento'] >= 0]
df = df[df['Servizio_Clienti_Contatti'] >= 0 ]

#ricontrollo valori nulli
print(df.value_counts())


# analisi esplorativa
#costo_perGB evitando divisioni per 0
df['Costo_per_GB'] = np.where(
    df['Dati_Consumati'] == 0,
    0,
    df['Tariffa_Mensile'] / df['Dati_Consumati']
)

print('\n',df[['Tariffa_Mensile','Dati_Consumati','Costo_per_GB']].head())


# stampa valori medi in base al churn
print('\n Valori medi in base al churn')
print(
    df.groupby('Churn')[
        ['Età','Durata_Abbonamento','Tariffa_Mensile','Costo_per_GB']
    ].mean()
)

# 1 = cliente che ha abbandonato, 0 = cliente fedele.
df['Churn'] = df['Churn'].map({'No': 0, 'Sì': 1})

#correlazione con churn per capire quale feature influenza l'abbandono
corr_matrix = df.corr()
#print(corr_matrix)
print('\n Correlazione con Tasso abbandono =1')
print(corr_matrix['Churn'].sort_values(ascending=False))
# Rischio churn:
# clienti giovani, con basso consumo dati, pochi mesi di abbonamento, costi per GB alti, molti contatti con il servizio clienti.
#Costo_per_GB e Servizio_Clienti_Contatti possono essere features per churn

## colonne numeriche
numerical_cols = [
    'Età',
    'Durata_Abbonamento',
    'Tariffa_Mensile',
    'Dati_Consumati',
    'Servizio_Clienti_Contatti',
    'Costo_per_GB'
]

df[numerical_cols] = (df[numerical_cols] - df[numerical_cols].min()) / (df[numerical_cols].max() - df[numerical_cols].min())

# Correlazione di tutte le features
corr_matrix = df[numerical_cols].corr()
print('\n Matrice di correlazione features \n', corr_matrix)


### modello ML
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score

# Preparazione features e target
X = df[numerical_cols].values
y = df['Churn'].values

# Divisione train/test (70% train, 30% test) con stratificazione
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

#Creazione e training del modello
model = LogisticRegression()
model.fit(X_train, y_train)

# predizione
y_pred = model.predict(X_test)

### valutazione modello
# Accuracy pred_corrette/totale
acc = accuracy_score(y_test, y_pred)
print(f"\nAccuracy: {acc:.2f}")

# Predizione probabilità sul test set
y_prob = model.predict_proba(X_test)[:,1]  # probabilità di churn = 1

# Calcolo AUC  la capacità del modello di differenziare correttamente le due classi (churn/no churn).
auc_score = roc_auc_score(y_test, y_prob)
print(f"AUC: {auc_score:.3f}")

# Confusion Matrix
#cm = confusion_matrix(y_test, y_pred)
#print("\nConfusion Matrix:")
#print(cm)

