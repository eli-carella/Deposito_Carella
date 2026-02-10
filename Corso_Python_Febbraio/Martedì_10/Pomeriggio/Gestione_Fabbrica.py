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


class Fabbrica:
    def __init__(self):
        self.inventario = {} # dizionario di prodotti

    def aggiungi_prodotto(self, prodotto, quantità): 
        #controllo se è già presente nell'inventario ovvero nel dizionario,
        #  se presente aggiorna quanità se ne no aggiungilo
        if prodotto.nome in self.inventario:
            self.inventario[prodotto.nome]["quantità"] += quantità
        else:
            self.inventario[prodotto.nome] = {
                "prodotto": prodotto,
                "quantità": quantità
            }

    # funzione vendi prodotto
    def vendi_prodotto(self, nome_prodotto, quantità):
        #se il nome non è in inventario oppure è di quantità insufficiente 
        # esci dalla funzione con None
        #altrimenti scala la quantità passata nell'inventario e calcola il profitto
        if nome_prodotto not in self.inventario:
            print("Prodotto non presente in inventario.")
            return
        elif self.inventario[nome_prodotto]["quantità"] < quantità:
            print("Quantità insufficiente in magazzino.")
            return
        else:
            prodotto = self.inventario[nome_prodotto]["prodotto"]
            self.inventario[nome_prodotto]["quantità"] -= quantità

            profitto = prodotto.calcola_profitto() * quantità
            print(f"Venduti {quantità} {nome_prodotto}. Profitto: {profitto} €")

    # calcola resi prodotto 
    def resi_prodotto(self, nome_prodotto, quantità):
        #se prodotto è nell'inventario aggiungi la quantità passata 
        if nome_prodotto in self.inventario:
            self.inventario[nome_prodotto]["quantità"] += quantità
        else:
            print("Prodotto non presente in inventario.")

