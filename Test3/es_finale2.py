import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# set grafica in seaborn per la visualizzazione 
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)
plt.rcParams["axes.titlesize"] = 16
plt.rcParams["axes.labelsize"] = 12
plt.rcParams["figure.dpi"] = 110

np.random.seed(42)


# creazione di dataset random con 15000 righe e colonne order, data, cliente, categoria 
def genera_dataset(n=15000):
    date_range = pd.date_range("2023-01-01", "2023-12-31", freq="H")

    df = pd.DataFrame({
        "order_id": np.arange(1, n + 1),
        "data_ordine": np.random.choice(date_range, n),
        "cliente_id": np.random.randint(1, 3000, n),
        "categoria": np.random.choice(
            ["Elettronica", "Abbigliamento", "Casa", "Sport", "Libri"],
            n,
            p=[0.30, 0.25, 0.20, 0.15, 0.10]
        ),
        "canale": np.random.choice(
            ["Online", "Mobile App", "Store"],
            n,
            p=[0.6, 0.3, 0.1]
        ),
        "prezzo_unitario": np.round(np.random.uniform(10, 800, n), 2),
        "quantita": np.random.randint(1, 6, n)
    })

    df["fatturato"] = df["prezzo_unitario"] * df["quantita"]
    df["data_ordine"] = pd.to_datetime(df["data_ordine"])
    df["mese"] = df["data_ordine"].dt.month
    df["giorno_settimana"] = df["data_ordine"].dt.day_name()

    return df


# KPI PRINCIPALI
# stampa i valori principali : fatturato tot, valori medi
def stampa_kpi(df):
    print("\nKPI PRINCIPALI")
    print("Fatturato totale: €", round(df["fatturato"].sum(), 2))
    print("Ticket medio: €", round(df["fatturato"].mean(), 2))
    print("Clienti unici:", df["cliente_id"].nunique())
    print("Numero ordini:", len(df))


# ANALISI ESPLORATIVA
# grafico a barre di valore fatturato per ogni cgni categoria
def grafico_fatturato_categoria(df):
    cat_rev = df.groupby("categoria")["fatturato"].sum().sort_values()
    palette = sns.color_palette("viridis", len(cat_rev))

    plt.figure()
    plt.barh(cat_rev.index, cat_rev.values, color=palette)
    plt.title("Fatturato Totale per Categoria")
    plt.xlabel("Fatturato (€)")

    for i, v in enumerate(cat_rev.values):
        plt.text(v, i, f" {v:,.0f}", va='center')

    plt.tight_layout()
    plt.show()

# fatturato al variare del tempo
def grafico_trend_mensile(df):
    trend = df.groupby("mese")["fatturato"].sum()

    plt.figure()
    sns.lineplot(x=trend.index, y=trend.values, marker="o", linewidth=3)
    plt.title("Trend Mensile del Fatturato")
    plt.xlabel("Mese")
    plt.ylabel("Fatturato (€)")
    plt.xticks(range(1, 13))
    plt.tight_layout()
    plt.show()


#grafico della distribuzione di fatturato 
def grafico_distribuzione(df):

    media = df["fatturato"].mean()
    mediana = df["fatturato"].median()

    plt.figure(figsize=(10,6))

    sns.histplot(
        df["fatturato"],
        bins=50,
        kde=True,
        color="#2a9d8f",
        edgecolor="white",
        alpha=0.8
    )

    plt.axvline(media, color="red", linestyle="--", linewidth=2, label=f"Media: {media:.0f}€")
    plt.axvline(mediana, color="blue", linestyle="--", linewidth=2, label=f"Mediana: {mediana:.0f}€")

    plt.title("Distribuzione del Fatturato per Ordine", fontsize=16, fontweight="bold")
    plt.xlabel("Fatturato (€)")
    plt.ylabel("Frequenza")
    plt.legend()

    plt.tight_layout()
    plt.show()


# grafico pivot table di fatturato per ogni giorno e categoria
def grafico_heatmap(df):
    pivot = df.pivot_table(
        values="fatturato",
        index="giorno_settimana",
        columns="categoria",
        aggfunc="sum"
    )

    plt.figure(figsize=(12, 6))
    sns.heatmap(pivot, cmap="magma")
    plt.title("Heatmap Fatturato per Giorno e Categoria")
    plt.tight_layout()
    plt.show()

# grafico della matrice di correlazione tra prezzo, quantità, fatturato
def grafico_correlazione(df):
    corr = df[["prezzo_unitario", "quantita", "fatturato"]].corr()

    plt.figure()
    sns.heatmap(corr, annot=True, cmap="coolwarm", center=0)
    plt.title("Matrice di Correlazione")
    plt.tight_layout()
    plt.show()


def rfm_analysis(df):
    '''
    La funzione calcola per ogni cliente le metriche RFM: Recency (giorni dall’ultimo acquisto), Frequency (numero di ordini),
    Monetary (spesa totale).
    Poi assegna un punteggio basato sui quartili e segmenta i clienti in At Risk, Loyal o Top in base allo score complessivo.
    '''

    snapshot = df["data_ordine"].max() + pd.Timedelta(days=1)

    rfm = df.groupby("cliente_id").agg({
        "data_ordine": lambda x: (snapshot - x.max()).days,
        "order_id": "count",
        "fatturato": "sum"
    })

    rfm.columns = ["Recency", "Frequency", "Monetary"]

    rfm["R"] = pd.qcut(rfm["Recency"], 4, labels=[4, 3, 2, 1])
    rfm["F"] = pd.qcut(rfm["Frequency"], 4, labels=[1, 2, 3, 4])
    rfm["M"] = pd.qcut(rfm["Monetary"], 4, labels=[1, 2, 3, 4])

    rfm["Score"] = rfm[["R", "F", "M"]].sum(axis=1)

    rfm["Segmento"] = pd.cut(
        rfm["Score"],
        bins=[0, 5, 8, 12],
        labels=["At Risk", "Loyal", "Top"]
    )

    return rfm

# grafico dei fserve a visualizzare quanti clienti appartengono a ciascuna categoria: ["At Risk", "Loyal", "Top"]
def grafico_segmenti(rfm):
    segment_counts = rfm["Segmento"].value_counts()

    plt.figure()
    sns.barplot(x=segment_counts.index, y=segment_counts.values, palette="Set2")
    plt.title("Distribuzione Categoria Clienti")
    plt.xlabel("Categoria")
    plt.ylabel("Numero Clienti")
    plt.tight_layout()
    plt.show()


# genera il dataset con valori random
df = genera_dataset()
# stampa valori kpi
stampa_kpi(df)
## visualizzazione grafici
grafico_fatturato_categoria(df)
grafico_trend_mensile(df)
grafico_distribuzione(df)
grafico_heatmap(df)
grafico_correlazione(df)
# analisi clienti con grafico delle categorie
rfm = rfm_analysis(df)
grafico_segmenti(rfm)