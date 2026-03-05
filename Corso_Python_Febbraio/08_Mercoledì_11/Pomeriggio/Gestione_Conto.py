"""
L'obiettivo è utilizzare l'incapsulamento per prevenire accessi non autorizzati o modifiche inappropriate al saldo del conto.

Classe ContoBancario:
Attributi privati:
__titolare (stringa che rappresenta il nome del titolare del conto)
__saldo (decimale che rappresenta il saldo del conto)
Metodi pubblici:
deposita(importo): aggiunge un importo al saldo solo se l'importo è positivo.
preleva(importo): sottrae un importo dal saldo solo se ci sono fondi sufficienti e l'importo è positivo.
visualizza_saldo(): restituisce il saldo corrente senza permettere la sua modifica diretta.
Gestione dei Metodi e Sicurezza:
I metodi deposita e preleva devono controllare che gli importi siano validi (e.g., non negativi).
Aggiungere metodi "getter" e "setter" per gli attributi come _titolare, applicando validazioni appropriate (e.g., il titolare deve essere una stringa non vuota).
"""


#CLASSE Conto Bancario
class ContoBancario:
    
    def __init__(self, titolare, saldo_iniziale=0.0):
        # Attributi privati
        self.__titolare = ""
        self.__saldo = 0.0
        
        # Uso del setter per assegnare il nome del titolare
        self.set_titolare(titolare)
        
        # Controllo saldo iniziale
        if saldo_iniziale >= 0:
            self.__saldo = saldo_iniziale
        else:
            raise ValueError("Il saldo iniziale non può essere negativo.")
    
    
    # metodo get che ritorna il titolare 
    def get_titolare(self):
        return self.__titolare
    
    # metodo setter per assenare il metodo privato nome del titolare
    def set_titolare(self, nome):
        # se l'argomento passato è una stringa e non vuoto allora assegno il nome all'attributo privato titolare
        if isinstance(nome, str) and nome.strip() != "":
            self.__titolare = nome
        else:
            raise ValueError("Il titolare deve essere una stringa non vuota.")
    
    
    # Metodi deposita e preleva
    def deposita(self, importo):
        # se l'importo passato è positivo aggiorna il saldo (privato) aggiungendo l'importo
        # altrimenti errore perchè negativo
        if importo > 0:
            self.__saldo += importo
            print(f"Depositati {importo:.2f}€. Nuovo saldo: {self.__saldo:.2f}€")
        else:
            print("Errore: l'importo deve essere positivo.")
    
    
    def preleva(self, importo):
        # se l'importo passato è negativo o importo < saldo stampa errore altrimenti scala dal saldo l'importo
        if importo <= 0:
            print("Errore: l'importo deve essere positivo.")
        elif importo > self.__saldo:
            print("Errore: fondi insufficienti.")
        else:
            self.__saldo -= importo
            print(f"Prelevati {importo:.2f}€. Nuovo saldo: {self.__saldo:.2f}€")
    
    #metodo get del saldo
    def get_saldo(self):
        #ritorna attributo privato __saldo
        return self.__saldo

#classe utente
class Utente:

    def __init__(self, nome, conto): # attribiti nome e oggetto conto
        self.nome = nome
        self.conto = conto


class Cliente(Utente):
    #classe cliente che eredita da utente, init ereditato da utente

    #utilizza metodo di conto per depositare
    def deposita(self, importo):
        self.conto.deposita(importo)

    #utilizza metodo di conto per prelevare
    def preleva(self, importo):
        self.conto.preleva(importo)

    #utilizza metodo di conto get per vedere il saldo
    def visualizza_saldo(self):
        print("Saldo:", self.conto.get_saldo())


class Admin(Utente):
    #classe Admin che eredita da utente, init ereditato da utente
    #può solo visualizzare
    def visualizza_saldo(self):
        print("Saldo del cliente:", self.conto.get_saldo())


# MAIN
#oggetto conto
conto_obj = ContoBancario("Elisabetta Carella", 1000)

#oggetti cliente e admin
cliente_obj = Cliente("Elisabetta Carella", conto_obj)
admin = Admin("Direttore", conto_obj)

#menu di scelta con 4 operazioni 
while True:
    print("\n--- MENU OPERAZIONI ---")
    print("1. Deposita")
    print("2. Preleva")
    print("3. Visualizza saldo (Cliente)")
    print("4. Visualizza saldo (Admin)")
    print("5. Esci")

    scelta = input("Scegli un'operazione (1-5): ")

    if scelta == "1":
        importo = float(input("Inserisci importo da depositare: "))
        cliente_obj.deposita(importo)


    elif scelta == "2":
        importo = float(input("Inserisci importo da prelevare: "))
        cliente_obj.preleva(importo)

    elif scelta == "3":
        cliente_obj.visualizza_saldo()

    elif scelta == "4":
        admin.visualizza_saldo()

    elif scelta == "5":
        print("Uscita dal programma.")
        break

    else:
        print("Scelta non valida. Riprova.")
