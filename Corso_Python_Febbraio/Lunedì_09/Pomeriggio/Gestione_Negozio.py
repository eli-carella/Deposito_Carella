'''
Lo scopo di questo esercizio è implementare un sistema di gestione per un negozio che deve interagire con clienti, 
gestire l'inventario e permettere agli amministratori di supervisionare le operazioni. 
Il sistema sarà strutturato in tre parti principali: 
1.Gestione Clienti: I clienti possono visualizzare gli articoli disponibili in inventario. 
I clienti possono selezionare e acquistare articoli dall'inventario. 
Il sistema tiene traccia degli acquisti dei clienti. 
2.Gestione dell'Inventario: Gli articoli in magazzino sono elencati con il nome, il prezzo e la quantità. 
È possibile aggiungere nuovi articoli all'inventario. 
Gli articoli possono essere rimossi o aggiornati (ad es., cambiare prezzo o quantità). 
3.Amministrazione: Gli amministratori possono visualizzare un rapporto delle vendite. 
Gli amministratori possono visualizzare lo stato corrente dell'inventario. 
Il sistema tiene traccia dei guadagni totali. 
Puoi pre inserire gli amministratori non i clienti Il sistema dovrebbe permettere di simulare un'interazione base tra il cliente e il negozio dopo un login e una registrazione, 
nonché fornire gli strumenti necessari per la manutenzione e l'analisi del negozio da parte degli amministratori.
'''

#classe utente
class Utente:
    def __init__(self, nome, budget):
        self.nome = nome
        self.budget = budget
        self.acquisti = [] # lista degli acquisti effettuati, (articolo, quantita, costo)

    def mostra_budget(self):
        print("Budget disponibile:", self.budget)

# classe negozio
class Negozio:
    def __init__(self):
        self.inventario = {}  # inventario vuoto   dizionario chiave = nome articolo, valore = dizionario con prezzo e quantità
        self.guadagni = 0  
        self.vendite = [] # lista di tuple (cliente, articolo, qta, totale)

    # stampa dizionario inventario
    def mostra_inventario(self):
        print("\n--- INVENTARIO ---")
        if not self.inventario:
            print("Inventario vuoto")
        else:
            #ciclo su elementi di dict inventario
            for nome, dati in self.inventario.items():
                print(nome, "- Prezzo:", dati["prezzo"], "- Quantità:", dati["quantita"])

    # riempie dizionario inventario con nuovi articoli
    def aggiungi_articolo(self, nome, prezzo, quantita):
        self.inventario[nome] = {"prezzo": prezzo, "quantita": quantita}
        print("Articolo aggiunto")

    #metodo per vendere
    def vendi(self, utente, articolo, quantita):
        if articolo in self.inventario and quantita > 0:
            #se l'articolo è presente nell'inventario allora calcolo il costo totale
            prezzo = self.inventario[articolo]["prezzo"]
            costo = prezzo * quantita # costo totale

            #puoi vendere se la quantità nell'inventario è superiore a quella richiesta dall'utente
            if self.inventario[articolo]["quantita"] >= quantita:
                #puoi vendere se budget è superiore al costo
                if utente.budget >= costo:
                    # aggiorna utente, scalando il budget e aggiungendo oggetti alla lista acquisti
                    utente.budget -= costo
                    utente.acquisti.append((articolo, quantita, costo))

                    # aggiorna negozio, scalando la quantità dall'inventario, aggiungendo il guadagno e aggiungendo alla lista vendite
                    self.inventario[articolo]["quantita"] -= quantita
                    self.guadagni += costo
                    self.vendite.append((utente.nome, articolo, quantita, costo))

                    print("Vendita completata. Totale:", costo)
                else:
                    print("Budget insufficiente")
            else:
                print("Quantità non disponibile")
        else:
            print("Articolo non valido")

    
    def report_vendite(self):
        print("\n--- REPORT VENDITE ---")
        #stampa lista vendite: utente articolo quantità toot 
        for v in self.vendite:
            print("Utente:", v[0], "| Articolo:", v[1],
                  "| Quantità:", v[2], "| Totale:", v[3])
        print("Guadagni totali:", self.guadagni)


#main
#oggetto negozio
negozio = Negozio()

# riempimento inventario dopo la creazione
negozio.aggiungi_articolo("Pane", 1.5, 20)
negozio.aggiungi_articolo("Latte", 1.2, 15)
negozio.aggiungi_articolo("Pasta", 2.0, 10)

# programma ripetibile con 2 livelli di while
while True:
    #primo menu di scelta con cliente, negozio, esci
    print("\n--- MENU PRINCIPALE ---")
    print("1 - Cliente")
    print("2 - Negozio")
    print("0 - Esci")

    scelta = input("Scelta: ")

    # scelta CLIENTE
    if scelta == "1":
        nome = input("Nome cliente: ")
        budget = float(input("Budget: "))
        #crea oggetto utente con nome e budget da input
        utente = Utente(nome, budget)

        #secondo while per gestire le operazioni del cliente
        while True:
            print("\n--- MENU CLIENTE ---")
            print("1 - Mostra inventario")
            print("2 - Compra articolo")
            print("3 - Mostra budget")
            print("4 - I miei acquisti")
            print("0 - Torna indietro")

            scelta_cliente = input("Scelta: ")

            if scelta_cliente == "1":
                negozio.mostra_inventario()

            elif scelta_cliente == "2":
                #input nome articolo e quantità richiesta
                articolo = input("Articolo: ")
                quantita = int(input("Quantità: "))
                #funzione negozio.vendi
                negozio.vendi(utente, articolo, quantita)

            elif scelta_cliente == "3":
                utente.mostra_budget()

            elif scelta_cliente == "4":
                print("\nStorico acquisti:")
                #stampa elementi lista acquisti
                for a in utente.acquisti:
                    print(a)

            elif scelta_cliente == "0":
                break

    # scelta NEGOZIO
    elif scelta == "2":
        #secondo while per gestire le operazioni dell'amministratore del negozio
        while True:
            print("\n--- MENU NEGOZIO ---")
            print("1 - Mostra inventario")
            print("2 - Aggiungi articolo")
            print("3 - Report vendite")
            print("0 - Torna indietro")

            scelta_neg = input("Scelta: ")

            if scelta_neg == "1":
                negozio.mostra_inventario()

            elif scelta_neg == "2":
                #aggiungi articoli con nome prezzo e quantità da input
                nome_art = input("Nome articolo: ")
                prezzo = float(input("Prezzo: "))
                quantita = int(input("Quantità: "))
                negozio.aggiungi_articolo(nome_art, prezzo, quantita)

            elif scelta_neg == "3":
                #stampa report vendite
                negozio.report_vendite()

            elif scelta_neg == "0":
                break

    elif scelta == "0":
        print("Programma terminato")
        break