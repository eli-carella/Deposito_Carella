"""
Andiamo a creare un sistema ripetibile che simuli un teatro:

Classe Base: Posto
Attributi privati:
    _numero (intero): il numero del posto.
    _fila (stringa): la fila in cui si trova il posto.
    _occupato (booleano): stato del posto, se è occupato (True) o libero (False).
Metodi:
    __init__(numero, fila): inizializza il posto impostando _occupato a False.
    prenota(): prenota il posto se non è già occupato; in caso contrario, segnala che il posto è già occupato.
    libera(): libera il posto se è occupato; altrimenti segnala che il posto non era prenotato.
    Getter: per recuperare il numero, la fila e lo stato (occupato/libero).
------------------------------
Classi Derivate
PostoVIP:
    Attributi aggiuntivi: servizi_extra (ad es. una lista di servizi come “Accesso al lounge”, “Servizio in posto”).
    Metodi:
        Sovrascrive il metodo prenota() per gestire, oltre alla prenotazione, l’attivazione dei servizi extra.
PostoStandard:
    Attributi aggiuntivi:
        costo (un valore numerico che rappresenta il costo della prenotazione, ad esempio per prenotazione online).
    Metodi:
        Può sovrascrivere prenota() per includere la visualizzazione del costo o altre particolarità della prenotazione.
------------------------------
Classe Teatro
    Attributi:
        _posti: una lista contenente tutti gli oggetti posti (sia VIP che Standard).
    Metodi:
        aggiungi_posto(posto): per aggiungere un nuovo posto alla lista.
        prenota_posto(numero, fila): cerca nella lista il posto corrispondente al numero e alla fila indicati e, se lo trova, invoca il metodo prenota() sul posto.
        stampa_posti_occupati(): stampa tutti i posti che risultano occupati.

"""
#classe base posto
class Posto:
    def __init__(self, numero, fila):
        # costruttore con attributi numero, file, occupato (di default messo uguale a False)
        self._numero = numero
        self._fila = fila
        self._occupato = False

    # Metodo prenotazione 
    def prenota(self):
        if not self._occupato:
            self._occupato = True
            print(f"Posto {self._fila}{self._numero} prenotato con successo.")
        else:
            print(f"Posto {self._fila}{self._numero} già occupato!")

    # Metodo per liberare il posto
    def libera(self):
        # cambia attributo occupato, mette False se era True, altrimenti il posto è già libero
        if self._occupato:
            self._occupato = False
            print(f"Posto {self._fila}{self._numero} è stato liberato.")
        else:
            print(f"Posto {self._fila}{self._numero} non era prenotato.")

    # Getter: metodi che mostrano numero, fila, occupato
    def get_numero(self):
        return self._numero

    def get_fila(self):
        return self._fila

    def get_occupato(self):
        return self._occupato
    

# classe derivata posto standard
class PostoStandard(Posto):
    def __init__(self, numero, fila, costo):
        #costruttore eredita numero e fila da posto e aggiunge costo
        super().__init__(numero, fila)
        self.costo = costo

    # metodo per prenotare
    def prenota(self):
        #se get occupato = False utilizza prenota di classe base posto
        if not self.get_occupato():
            super().prenota()
            #stampa attributo costo
            print(f"Costo della prenotazione: €{self.costo:.2f}")
        else:
            print(f"Posto Standard {self.get_fila()}{self.get_numero()} già occupato!")

#classe derivata posto vip
class PostoVIP(Posto):
    def __init__(self, numero, fila, servizi_extra):
        #costruttore eredita attributi numero e fila da posto e aggiunge servizi_extra
        super().__init__(numero, fila)
        self.servizi_extra = servizi_extra  #lista

    def prenota(self):
        #se get occupato = False utilizza metodo prenota di classe base posto
        if not self.get_occupato():
            super().prenota()
            #stampa lista servizi in più con for su lista servizi_extra
            print("Servizi extra attivati:")
            for servizio in self.servizi_extra:
                print(f"- {servizio}")
        else:
            print(f"Posto VIP {self.get_fila()}{self.get_numero()} già occupato!")


# CLASSE TEATRO
class Teatro:
    def __init__(self):
        self.__posti = [] #lista di oggetti posti, inzializzata con vuota

    #metdo per aggiungere oggetto posto a lista 
    def aggiungi_posto(self, posto):
        self.__posti.append(posto)

    #metodo per prenotare
    def prenota_posto(self, numero, fila):
        #ciclo su lista posti 
        for posto in self.__posti:
            #se numero e fila passati corrispondono ai valori dei posti salvati puoi prenotare
            if posto.get_numero() == numero and posto.get_fila() == fila:
                posto.prenota()
                print("Posto prenotato")
                return
        print("Posto non trovato")

    #metodo per stampare i posti occupati
    def stampa_posti_occupati(self):
        print("\nPosti occupati:")
        #ciclo su lista posti e se occupato=True stampa attributi fila e numero 
        for posto in self.__posti:
            if posto.get_occupato():
                print(f"Fila {posto.get_fila()} Numero {posto.get_numero()}")


#main

#creo oggetto teatro
teatro = Teatro()

# Aggiunta posti con metodo aggiungi_posto a cui passo oggetti posti
teatro.aggiungi_posto(PostoVIP(1, "A", ["Accesso bar", "Servizio al posto"]))
teatro.aggiungi_posto(PostoStandard(2, "A", 25.00))
teatro.aggiungi_posto(PostoStandard(3, "B", 20.00))
teatro.aggiungi_posto(PostoVIP(4, "B", ["Drink omaggio", "Area riservata"]))

#menu di scelta
while True:
    print("\n--- GESTIONALE TEATRO ---")
    print("1. Prenota un posto")
    print("2. Visualizza posti occupati")
    print("3. Esci")
    
    scelta = input("Seleziona un'opzione: ")

    if scelta == "1":
        try:
            fila = input("Inserisci la lettera della fila (es. A): ").upper()
            numero = int(input("Inserisci il numero del posto: "))
            #prenota posto con metodo prenota_posto
            teatro.prenota_posto(numero, fila)
        except ValueError:
            print("Errore: Inserisci un numero valido per il posto.")

    elif scelta == "2":
        #stampa lista con metodo stampa_posti_occupati
        teatro.stampa_posti_occupati()

    elif scelta == "3":
        print("Chiusura del programma")
        break
    
    else:
        print("Opzione non valida")