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
        #  se presente aggiorna solo quanità se ne no aggiungilo
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


#creo oggetto fabbrica
fabbrica = Fabbrica()

# oggetti di Prodotti 
telefono = Elettronica("Smartphone", 300, 600, 2)
maglietta = Abbigliamento("T-shirt", 5, 20, "Cotone")

#aggiunta a fabbrica
fabbrica.aggiungi_prodotto(telefono, 10)
fabbrica.aggiungi_prodotto(maglietta, 50)

# menu di scelta con 4 azioni
while True:
    print("\n--- MENU FABBRICA ---")
    print("1. Aggiungi prodotto")
    print("2. Vendi prodotto")
    print("3. Reso prodotto")
    print("4. Visualizza inventario")
    print("0. Esci")

    scelta = input("Seleziona un'opzione: ")

    # aggiunta prodotti
    if scelta == "1":
        nome = input("Nome prodotto: ")
        quantita = int(input("Quantità: "))

        if nome in fabbrica.inventario:
            prodotto = fabbrica.inventario[nome]["prodotto"]
            fabbrica.aggiungi_prodotto(prodotto, quantita)
            print("Quantità aggiornata.")
        else:
            print("Tipo prodotto:")
            print("1. Elettronica")
            print("2. Abbigliamento")
            tipo = input("Scelta: ")

            costo = float(input("Costo di produzione: "))
            prezzo = float(input("Prezzo di vendita: "))

            if tipo == "1":
                garanzia = int(input("Anni di garanzia: "))
                prodotto = Elettronica(nome, costo, prezzo, garanzia)

            elif tipo == "2":
                materiale = input("Materiale: ")
                prodotto = Abbigliamento(nome, costo, prezzo, materiale)

            else:
                print("Tipo di prodotto non valido.")
                continue

            fabbrica.aggiungi_prodotto(prodotto, quantita)
            print("Nuovo prodotto aggiunto all'inventario.")

    # vendita prodotti
    elif scelta == "2":
        nome = input("Nome prodotto da vendere: ")
        quantita = int(input("Quantità da vendere: "))
        fabbrica.vendi_prodotto(nome, quantita)

    # reso prodotto
    elif scelta == "3":
        nome = input("Nome prodotto restituito: ")
        quantita = int(input("Quantità resa: "))
        fabbrica.resi_prodotto(nome, quantita)
        print("Reso registrato.")

    # stampa inventario
    elif scelta == "4":
        print("\n--- INVENTARIO ---")
        for nome, dati in fabbrica.inventario.items():
            print(f"{nome}: {dati['quantità']} pezzi")

    # uscita
    elif scelta == "0":
        print("Uscita dal programma.")
        break

    else:
        print("Scelta non valida.")