"""
creare una classe base MembroSquadra e diverse classi figlie che rappresentano ruoli specifici all'interno della squadra di calcio, come Giocatore, Allenatore, e Assistente. 
L'esercizio consente di esplorare come differenti membri della squadra possono ereditare attributi comuni dalla classe base, ma anche come possono differire nei loro comportamenti e responsabilità. 
Classe MembroSquadra: 
Attributi: nome (stringa) età (intero) Metodi: descrivi() (stampa una descrizione generale del membro della squadra) 
Classi Derivate:
Giocatore:

Attributi aggiuntivi come ruolo (e.g., attaccante, difensore) e numero_maglia
Metodi come gioca_partita() che possono includere azioni specifiche del giocatore
Allenatore:
Attributi aggiuntivi come anni_di_esperienza
Metodi come dirige_allenamento() che dettagliano come l'allenatore conduce gli allenamenti
Assistente:
Attributi aggiuntivi come specializzazione (e.g., fisioterapista, analista di gioco)
Metodi specifici del ruolo, come supporta_team() che può descrivere varie forme di supporto al team

Crea due squadre e falle giocare contro.

"""
import random

# Classe base
class MembroSquadra:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    def descrivi(self):
        return f"{self.nome}, {self.eta} anni, membro della squadra."
    

# Classe Giocatore
class Giocatore(MembroSquadra):
    def __init__(self, nome, eta, ruolo, numero_maglia, abilita):
        #eredita nome ed eta da membro squadra e aggiunge 3 attributi ruolo, numero maglia e abilità
        super().__init__(nome, eta)
        self.ruolo = ruolo
        self.numero_maglia = numero_maglia
        self.abilita = abilita  # valore numerico per simulare la forza del giocatore da 1 a 10

    def descrivi(self):
        return f"{self.nome} (#{self.numero_maglia}) - {self.ruolo}, {self.eta} anni."

    def gioca_partita(self):
        #Simula quanto bene gioca un calciatore in una partita e restituisce un numero che rappresenta la sua prestazione.
        # aggiunge ad abilità numero casuale che rappresenta la forma del giorno del giocatore:
        abilita_del_giorno = random.randint(1, 10)
        prestazione = abilita_del_giorno + self.abilita
        print(f"{self.nome} gioca la partita con prestazione {prestazione}")
        return prestazione
    
# Classe Allenatore
class Allenatore(MembroSquadra):
    def __init__(self, nome, eta, anni_di_esperienza):
        #eredita da mebro squadra e aggiunge attributo anni di esperienza
        super().__init__(nome, eta)
        self.anni_di_esperienza = anni_di_esperienza

    def dirige_allenamento(self):
        print(f"L'allenatore {self.nome} dirige l'allenamento con {self.anni_di_esperienza} anni di esperienza.")

    def descrivi(self):
        return f"Allenatore {self.nome}, {self.anni_di_esperienza} anni di esperienza."
    
    def bonus(self):
        return self.anni_esperienza  # bonus alla squadra inm base ad anni di esperienza
    

# Classe Assistente
class Assistente(MembroSquadra):
    def __init__(self, nome, eta, specializzazione):
        #eredita da mebro squadra e aggiunge attributo tipo di specializazione
        super().__init__(nome, eta)
        self.specializzazione = specializzazione

    def supporta_team(self):
        print(f"{self.nome} supporta il team come {self.specializzazione}.")

    def descrivi(self):
        return f"Assistente {self.nome}, specializzato in {self.specializzazione}."
    
    def bonus(self):
        return 5  # bonus fisso alla squadra
    

class Squadra:
    def __init__(self, nome, max_giocatori):
        self.nome = nome
        self.max_giocatori = max_giocatori
        self.giocatori = []

    def aggiungi_giocatore(self, giocatore):
        if len(self.giocatori) < self.max_giocatori:
            self.giocatori.append(giocatore)
            print("Giocatore aggiunto!")
        else:
            print("Numero massimo di giocatori raggiunto!")

    def forza_totale(self):
        totale = 0
        for g in self.giocatori:
            totale += g.gioca_partita()
        return totale
    
class Squadra:
    def __init__(self, nome, max_giocatori):
        self.nome = nome
        self.max_giocatori = max_giocatori
        self.giocatori = []
        self.allenatore = None
        self.assistente = None

    def aggiungi_giocatore(self, giocatore):
        if len(self.giocatori) < self.max_giocatori:
            self.giocatori.append(giocatore)
            print("Giocatore aggiunto!")
        else:
            print("Numero massimo di giocatori raggiunto!")

    def set_allenatore(self, allenatore):
        self.allenatore = allenatore
        print("Allenatore assegnato!")

    def set_assistente(self, assistente):
        self.assistente = assistente
        print("Assistente assegnato!")

    def forza_totale(self):
        #calcola risulato totale come somma dei punteggi di ogni giocatore della lista
        # e aggiunge bonus allenatori e assistenti
        totale = 0

        for g in self.giocatori:
            totale += g.gioca_partita()

        if self.allenatore:
            totale += self.allenatore.bonus()

        if self.assistente:
            totale += self.assistente.bonus()

        return totale


# CREAZIONE SQUADRE con nomi e num max giocatori
max_giocatori = int(input("Quanti giocatori per squadra? "))

nome1 = input("Nome prima squadra: ")
nome2 = input("Nome seconda squadra: ")

squadra1 = Squadra(nome1, max_giocatori)
squadra2 = Squadra(nome2, max_giocatori)


# MENU
while True:
    print("\n--- MENU ---")
    print("1) Aggiungi giocatore Squadra 1")
    print("2) Aggiungi giocatore Squadra 2")
    print("3) Inserisci allenatore Squadra 1")
    print("4) Inserisci allenatore Squadra 2")
    print("5) Inserisci assistente Squadra 1")
    print("6) Inserisci assistente Squadra 2")
    print("7) Gioca partita")
    print("8) Esci")

    scelta = input("Scelta: ")

    # AGGIUNTA GIOCATORI
    if scelta == "1" or scelta == "2":

        nome = input("Nome giocatore: ")
        eta = int(input("Età: "))
        ruolo = input("Ruolo: ")
        numero = int(input("Numero maglia: "))
        abilita = int(input("Abilità (1-10): "))

        giocatore = Giocatore(nome, eta, ruolo, numero, abilita)

        if scelta == "1":
            squadra1.aggiungi_giocatore(giocatore)
        else:
            squadra2.aggiungi_giocatore(giocatore)

    # ALLENATORE
    elif scelta == "3" or scelta == "4":
        nome = input("Nome allenatore: ")
        eta = int(input("Età: "))
        esperienza = int(input("Anni di esperienza: "))

        allenatore = Allenatore(nome, eta, esperienza)

        if scelta == "3":
            squadra1.set_allenatore(allenatore)
        else:
            squadra2.set_allenatore(allenatore)

    # ASSISTENTE
    elif scelta == "5" or scelta == "6":
        nome = input("Nome assistente: ")
        eta = int(input("Età: "))
        spec = input("Specializzazione: ")

        assistente = Assistente(nome, eta, spec)

        if scelta == "5":
            squadra1.set_assistente(assistente)
        else:
            squadra2.set_assistente(assistente)

    # PARTITA
    elif scelta == "7":

        if (len(squadra1.giocatori) != max_giocatori or
            len(squadra2.giocatori) != max_giocatori):
            print("Le squadre non sono complete!")
        elif not squadra1.allenatore or not squadra2.allenatore:
            print("Manca un allenatore!")
        elif not squadra1.assistente or not squadra2.assistente:
            print("Manca un assistente!")
        else:
            print("\n PARTITA ")
            # calcolo punteggi con metodi forza_totale delle squadre
            punteggio1 = squadra1.forza_totale()
            punteggio2 = squadra2.forza_totale()

            print(f"\n{squadra1.nome}: {punteggio1}")
            print(f"{squadra2.nome}: {punteggio2}")

            #confronto punteggi e stampa risultato partita
            if punteggio1 > punteggio2:
                print(f"Vince {squadra1.nome}!")
            elif punteggio2 > punteggio1:
                print(f"Vince {squadra2.nome}!")
            else:
                print("Pareggio!")

    elif scelta == "8":
        print("Uscita dal programma.")
        break

    else:
        print("Scelta non valida!")