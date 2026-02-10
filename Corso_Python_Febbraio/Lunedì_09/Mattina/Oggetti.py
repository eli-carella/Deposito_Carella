'''
class Persona():
    #ha construttore intrinseco nascosto all'interno
    pass

#oggetto
eli_OBJ = Persona()


class Persona():
    x = 10 # variabile in tutti gli oggetti persona
    def __init__(self):  #self è il  placeholder del nome dell'oggetto
        pass

#oggetto
eli_OBJ = Persona()

print(eli_OBJ.x)

eli_OBJ.x = 17

print(eli_OBJ.x)
print(elisa_OBJ.x)
'''


class Automobile: # dichiaro la classe
    numero_di_ruote = 4 # attributo di classe
    def __init__(self, marca, modello): # metodo costruttore
        self.marca = marca # attributo di istanza
        self.modello = modello # attributo di istanza
    def stampa_info(self): # metodo di istanza
        print("L'automobile è una", self.marca, self.modello)

#tipi basilari
print(type(10))
print(type(3.14))
print(type("tipo"))
print(type([]))


#Tipi non basilari
class MioOggetto:
    def __init__(slef):
        pass

    def __str__(self): 
        return "Ciao TO_STRING sono un metodo speciale"

obj = MioOggetto()
print(type(obj))

print(obj)


### esempio metodo statico

class Calcolatrice:
    @staticmethod
    def somma(a, b):
        return a + b

# Uso del metodo statico senza creare un'istanza
risultato = Calcolatrice.somma(5, 3)
print(risultato)
# Output: 8


class Contatore:

    numero_istanze = 0 # Attributo di classe

    def __init__(self):
        Contatore.numero_istanze += 1

    @classmethod
    def mostra_numero_istanze(cls):
        print(f"Sono state create {cls.numero_istanze} istanze.")

# Creazione di alcune istanze
c1 = Contatore()
c2 = Contatore()
Contatore.mostra_numero_istanze()
# Output: Sono state create 2 istanze.