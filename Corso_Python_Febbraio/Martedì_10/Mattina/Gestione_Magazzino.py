"""
l sistema deve includere una classe Pacco con: codice (stringa), peso (numero) e stato (es. "in magazzino", "in consegna", "consegnato"), con un metodo per mostrare le info e un metodo per cambiare stato.

Deve esserci una classe Magazzino che contiene una lista (o dizionario) di pacchi e permette di aggiungere un pacco, cercarlo per codice, e mostrare tutti i pacchi in un certo stato.

Deve esserci infine una classe GestorePacchi che usa il magazzino per mettere un pacco “in consegna”, segnare un pacco come “consegnato” e calcolare il peso totale dei pacchi ancora non consegnati.

Nel programma principale crea almeno 5 pacchi, inseriscili nel magazzino, cambia lo stato di alcuni pacchi (almeno una consegna avviata e una consegna completata) e stampa: elenco pacchi “in magazzino”, elenco pacchi “in consegna” e il peso totale dei pacchi non ancora consegnati.
"""
#classe pacco
class Pacco:
    def __init__(self, codice:str, peso:float, stato="in magazzino"):
        #costruttore con 3 attributi codice, peso, stato
        self.codice = codice
        self.peso = peso
        self.stato = stato

    def mostra_info(self):
        print(f"Pacco {self.codice} - Peso: {self.peso} kg - Stato: {self.stato}")

    def cambia_stato(self, nuovo_stato):
        #modifica stato
        self.stato = nuovo_stato

#classe magazzino 
class Magazzino:
    def __init__(self):
        self.pacchi = {}  # dizionario di pacchi, codice -> Pacco

    #aggiunge il pacco al dizionario
    def aggiungi_pacco(self, pacco):
        self.pacchi[pacco.codice] = pacco

    #cerca pacco con key codice 
    def cerca_pacco(self, codice):
        return self.pacchi.get(codice)

    # ritorna elenco pacchi con un certo stato
    def pacchi_per_stato(self, stato):
        return [p for p in self.pacchi.values() if p.stato == stato]



# classe gestore pacchi
class GestorePacchi:
    def __init__(self, magazzino):
        self.magazzino = magazzino  #inizializzo con attributo magazzino

    # cerca pacco nel dizionario con key codice e modifica stato del pacco in consegna
    def metti_in_consegna(self, codice):
        pacco = self.magazzino.cerca_pacco(codice)
        if pacco:
            pacco.cambia_stato("in consegna")

    # cerca pacco nel dizionario con key codice e modifica stato del pacco consegnato
    def segna_consegnato(self, codice):
        pacco = self.magazzino.cerca_pacco(codice)
        if pacco:
            pacco.cambia_stato("consegnato")

    #calcolo peso totale pacchi che non sono consegnati
    def peso_totale_non_consegnati(self):
        totale = 0
        # ciclo sui valori di pacchi del dizionario, 
        for pacco in self.magazzino.pacchi.values():
            # se lo stato non è consegnato aggiunge il peso al contatore 
            if pacco.stato != "consegnato":
                totale += pacco.peso
        return totale

#creo oggetto magazzino e gestore 
magazzino = Magazzino()
gestore = GestorePacchi(magazzino)

# Creo 5 pacchi con codice e peso e stato di dafault in magazzino
p1 = Pacco("P001", 2.0)
p2 = Pacco("P002", 1.5)
p3 = Pacco("P003", 4.2)
p4 = Pacco("P004", 3.1)
p5 = Pacco("P005", 5.0)

# Inserimento nel magazzino
for pacco in [p1, p2, p3, p4, p5]:
    magazzino.aggiungi_pacco(pacco)

# Cambi di stato:  2 in consegna, 1 consegnato
gestore.metti_in_consegna("P002")
gestore.metti_in_consegna("P003")
gestore.segna_consegnato("P003")

# Stampa pacchi in magazzino
print("\nPacchi in magazzino:")
for pacco in magazzino.pacchi_per_stato("in magazzino"):
    pacco.mostra_info()

# Stampa pacchi in consegna
print("\nPacchi in consegna:")
for pacco in magazzino.pacchi_per_stato("in consegna"):
    pacco.mostra_info()

# Peso totale pacchi non consegnati
print("\nPeso totale pacchi non consegnati:",
      gestore.peso_totale_non_consegnati(), "kg")
