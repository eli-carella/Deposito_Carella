from datetime import datetime
"""
Classe ControlloAccessi: serve a gestire la logica di ingresso,
e verificare se un utente può entrare e salvare un log degli accessi.
"""

class ControlloAccessi:
    def __init__(self):
        self._log = []  # attributo lista privata di accessi, inizializzato con vuota

    #"Verifica se un utente può accedere con il livello richiesto e registra il log
    def verifica_accesso(self, utente, livello_richiesto):  #metodo polimorfico, passo oggetto utente e fa 2 cose diverse a seconda sei casi
        if utente.livello_accesso() >= livello_richiesto:
            self.registra_log(utente, "ACCESSO CONSENTITO")
            return True
        else:
            self.registra_log(utente, "ACCESSO NEGATO")
            return False

    #Salva nel log una riga con: data e ora nome utente esito (consentito/negato)
    def registra_log(self, utente, esito):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        voce = f"{timestamp} - {utente.get_nome()} - {esito}"
        self._log.append(voce) #aggiungee questa voce 

    #stampa tutta la lista log
    def mostra_log(self):
        print("\n - LOG ACCESSI -")
        for voce in self._log:
            print(voce)
