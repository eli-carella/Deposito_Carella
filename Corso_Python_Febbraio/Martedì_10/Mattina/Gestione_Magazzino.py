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
        self.pacchi = {}  # dizionario di pacchi

    #aggiunge il pacco al dizionario
    def aggiungi_pacco(self, pacco):
        self.pacchi[pacco.codice] = pacco

    #cerca pacco con key codice 
    def cerca_pacco(self, codice):
        return self.pacchi.get(codice)

    # ritorna pacchi con un certo stato
    def pacchi_per_stato(self, stato):
        if p.stato == stato:
            for p in self.pacchi.values():
                return p
