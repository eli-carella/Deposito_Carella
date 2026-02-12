"""
creare una classe base MetodoPagamento e diverse classi derivate che rappresentano diversi metodi di pagamento. Questo scenario permetterà di vedere il polimorfismo in azione, permettendo alle diverse sottoclassi di implementare i loro specifici comportamenti di pagamento, pur aderendo all'interfaccia comune definita dalla classe base.

Classe MetodoPagamento:
Metodi:
effettua_pagamento(importo): un metodo che ogni sottoclasse dovrà implementare.
Classi Derivate:
CartaDiCredito:
Metodi come effettua_pagamento(importo) che simula un pagamento tramite carta di credito.
PayPal:
Metodi come effettua_pagamento(importo) che simula un pagamento tramite PayPal.
BonificoBancario:
Metodi come effettua_pagamento(importo) che simula un pagamento tramite bonifico bancario.
GestorePagamenti:
Una classe che usa un'istanza di MetodoPagamento per effettuare pagamenti, senza preoccuparsi del dettaglio del metodo di pagamento.
"""
#calsse base
class MetodoPagamento():
    def effettua_pagamento(self, importo):
        pass

# Classe derivata: Carta di Credito
class CartaDiCredito(MetodoPagamento):
    # Overriding di metodo effettua_pagamento
    def effettua_pagamento(self, importo):
        print(f"Pagamento di €{importo:.2f} effettuato con Carta di Credito")


# Classe derivata: PayPal
class PayPal(MetodoPagamento):
    # Overriding di metodo effettua_pagamento
    def effettua_pagamento(self, importo):
        print(f"Pagamento di €{importo:.2f} effettuato tramite PayPal")


# Classe derivata: Bonifico Bancario
class BonificoBancario(MetodoPagamento):
    # Overriding di metodo effettua_pagamento
    def effettua_pagamento(self, importo):
        print(f"Pagamento di €{importo:.2f} effettuato tramite Bonifico Bancario")


# Classe che utilizza il polimorfismo
class GestorePagamenti:

    def __init__(self, metodo_pagamento: MetodoPagamento):
        self.metodo_pagamento = metodo_pagamento #attribito oggetto di tipo metodoPagamento

    #metodo polimorfico:  utilizzo sempre lo stesso metodo 
    # ma l'implementazione è diversa in base all'oggetto reale
    def esegui_pagamento(self, importo):
        self.metodo_pagamento.effettua_pagamento(importo)


# main con menu con 3 scelte

while True:
        print("====== MENU PAGAMENTI ======")
        print("1. Paga con Carta di Credito")
        print("2. Paga con PayPal")
        print("3. Paga con Bonifico Bancario")
        print("4. Esci")
        print("============================")

        scelta = input("Seleziona un'opzione: ")

        if scelta == "1":
            importo = float(input("Inserisci l'importo da pagare: €"))
            gestore = GestorePagamenti(CartaDiCredito())
            gestore.esegui_pagamento(importo)

        elif scelta == "2":
            importo = float(input("Inserisci l'importo da pagare: €"))
            gestore = GestorePagamenti(PayPal())
            gestore.esegui_pagamento(importo)

        elif scelta == "3":
            importo = float(input("Inserisci l'importo da pagare: €"))
            gestore = GestorePagamenti(BonificoBancario())
            gestore.esegui_pagamento(importo)

        elif scelta == "4":
            print("Uscita dal programma...")
            break
        
        else:
            print("Scelta non valida!\n")
            continue