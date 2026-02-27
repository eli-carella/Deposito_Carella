ANALISI DATI E-COMMERCE

DESCRIZIONE DEL PROGETTO


Questo progetto ha l’obiettivo di analizzare i dati di vendita
di un e-commerce al fine di estrarre insight utili per il business.

Il dataset, generato artificialmente tramite NumPy, simula
15.000 ordini effettuati nel corso del 2023, includendo
informazioni su:

- Cliente
- Data ordine
- Categoria prodotto
- Canale di vendita
- Prezzo unitario
- Quantità acquistata
- Fatturato generato


OBIETTIVI PRINCIPALI

1. Calcolare i principali KPI aziendali:
   - Fatturato totale
   - Ticket medio
   - Numero clienti unici
   - Numero totale ordini

2. Analizzare la distribuzione del fatturato:
   - Studio della variabilità degli ordini
   - Identificazione di eventuali outlier
   - Valutazione dell’asimmetria della distribuzione

3. Analizzare la performance per categoria:
   - Confronto tra categorie
   - Identificazione dei driver di fatturato

4. Studiare l’andamento temporale:
   - Trend mensile del fatturato
   - Analisi della stagionalità
   - Distribuzione per giorno della settimana

5. Analizzare le relazioni tra variabili:
   - Correlazione tra prezzo, quantità e fatturato
   - Comprensione dei fattori che influenzano il revenue


METODO
Fasi di Data Analysis:

1. Data Generation (simulazione dati realistici)
2. Data Cleaning e Feature Engineering
3. Calcolo KPI
4. Analisi Esplorativa (EDA)
5. Visualizzazione avanzata dei dati
6. Interpretazione e insight strategici


LIBRERIE UTILIZZATE

- NumPy: generazione dati e calcoli numerici
- Pandas: manipolazione e analisi dati
- Matplotlib: visualizzazioni base
- Seaborn: visualizzazioni avanzate e styling

RISULTATI:
 PERFORMANCE PER CATEGORIA

Dal grafico del fatturato per categoria emerge che alcune
categorie contribuiscono in modo predominante al revenue totale.

In particolare:
- La categoria con fatturato più alto rappresenta il driver principale del business.
- Le categorie minori hanno un peso inferiore ma contribuiscono alla diversificazione.

Questo suggerisce possibili strategie:
- Rafforzare marketing e promozioni sulle categorie più redditizie
- Ottimizzare assortimento nelle categorie meno performanti


1) TREND TEMPORALE

L’analisi mensile mostra una variazione del fatturato nel tempo,
con possibili picchi negli ultimi mesi dell’anno.

La presenza di stagionalità suggerisce la possibilità
di pianificare strategie commerciali mirate nei mesi ad alta domanda.


2) DISTRIBUZIONE DEL FATTURATO

La distribuzione del fatturato per ordine risulta asimmetrica,
con una coda verso destra.

Questo indica:
- La maggior parte degli ordini ha valore medio-basso
- Una minoranza di ordini presenta valori elevati (possibili outlier)

La differenza tra media e mediana conferma la presenza
di una distribuzione non simmetrica.


3) CORRELAZIONI TRA VARIABILI

La matrice di correlazione mostra una forte relazione tra:
- Prezzo unitario
- Quantità acquistata
- Fatturato totale

Non emergono anomalie nei pattern osservati.


4) RFM ANALYSIS E SEGMENTAZIONE CLIENTI

L’analisi RFM ha permesso di segmentare i clienti in base a tre metriche chiave:

- Recency (R): giorni dall’ultimo acquisto → misura l’attività recente del cliente.
- Frequency (F): numero di ordini effettuati → indica la fedeltà del cliente.
- Monetary (M): spesa totale → rappresenta il valore economico del cliente.

Attraverso il calcolo dei quartili, ogni cliente ha ricevuto un punteggio R, F e M, che sommato forma uno score complessivo.

Successivamente, i clienti sono stati suddivisi in tre segmenti strategici:

- Top: clienti più preziosi, fedeli e recenti, che generano la maggior parte del fatturato.
- Loyal: clienti regolari, con comportamento positivo ma non top.
- At Risk: clienti meno attivi o con bassa spesa, potenzialmente a rischio di abbandono.

Il grafico a barre evidenzia la distribuzione dei clienti nei tre segmenti. 
Serve per:
Identificare i clienti Top permette di pianificare campagne di fidelizzazione mirate.  
I clienti At Risk potrebbero essere incentivati con promozioni o reminder per riattivare gli acquisti.  
I segmenti Loyal sono una base stabile.  

Questa analisi serve quindi indicazioni concrete per ottimizzare marketing, promozioni e strategia commerciale.
