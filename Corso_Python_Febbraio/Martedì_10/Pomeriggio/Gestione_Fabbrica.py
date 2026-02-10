"""
Classe Prodotto:
Attributi:
nome (stringa che descrive il nome del prodotto)
costo_produzione (costo per produrre il prodotto)
prezzo_vendita (prezzo a cui il prodotto viene venduto al pubblico)
Metodi:
calcola_profitto: restituisce la differenza tra il prezzo di vendita e il costo di produzione.
Classi parallele:
Creare almeno due classi parallele a Prodotto, per esempio Elettronica e Abbigliamento.
Aggiungere attributi specifici per ciascun tipo di prodotto, come materiale per Abbigliamento e garanzia per Elettronica.
Classe Fabbrica:
Attributi:
inventario: un dizionario che tiene traccia del numero di ogni tipo di prodotto in magazzino.
Metodi:
aggiungi_prodotto: aggiunge prodotti all'inventario.
vendi_prodotto: diminuisce la quantità di un prodotto in inventario e stampa il profitto realizzato dalla vendita.
resi_prodotto: aumenta la quantità di un prodotto restituito in inventario.
"""

class Prodotto:
    def __init__(self, nome, costo_produzione, prezzo_vendita):
        # costruttore con 3 attributi nome, costo, prezzo vendita
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita

    
    def calcola_profitto(self):
        #calcolo profitto
        return self.prezzo_vendita - self.costo_produzione

#classe figlia Elettronica che eredita da prodotto
class Elettronica(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita, garanzia_anni):
        super().__init__(nome, costo_produzione, prezzo_vendita) #costruttore padre 
        self.garanzia_anni = garanzia_anni # attributo aggiuntivo

#classe figlia Abbibliamento che eredita da prodotto
class Abbigliamento(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita, materiale):
        super().__init__(nome, costo_produzione, prezzo_vendita) #costruttore padre 
        self.materiale = materiale # attributo aggiuntivo


