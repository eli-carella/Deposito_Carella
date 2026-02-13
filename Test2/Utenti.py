from abc import ABC, abstractmethod

"""
Classe base astratta Utente e classi figlie Dipendente e manager 
"""

#classe base utente
class Utente(ABC):
    def __init__(self, nome, badge_id): #costruttore con attributi iniziali
        # INCAPSULAMENTO: attributi protetti nella superclasse
        self._nome = nome
        self._badge_id = badge_id

    # metodi Getter degli attributi
    def get_nome(self):
        return self._nome
    
    def get_badge_id(self):
        return self._badge_id

    # Metodo astratto che verrà poi implementato nelle classi derivate
    @abstractmethod # qui ho polimorfismo perchè classi figlie implementano la loro versione
    def livello_accesso(self):
        pass

    #metodo to string
    def __str__(self):
        return f"{self._nome} (Badge: {self._badge_id})"


# classe derivata: dipendente

class Dipendente(Utente): 
    #qui polimorfismo, dipendente eredita costruttore da utente 
    #e aggiunge attributo in più reparto
    def __init__(self, nome, badge_id, reparto):
        super().__init__(nome, badge_id) # con super richiamo init utente
        self._reparto = reparto #aggiunta attributo

    def livello_accesso(self):
        return 1  # accesso base con livello 1

    # metodo get di reparto
    def get_reparto(self):
        return self._reparto

#classe derivata manager
class Manager(Utente):
    def __init__(self, nome, badge_id, area): #eredita init da padre e aggiunge area come extra attributo
        super().__init__(nome, badge_id)
        self._area = area

    def livello_accesso(self):
        return 2  # accesso più alto con livello 2

    def get_area(self):
        return self._area
