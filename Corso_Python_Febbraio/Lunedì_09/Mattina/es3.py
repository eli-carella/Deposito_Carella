'''
Crea una classe biblioteca
che permetta di creare un
libro e stamparlo
'''

class Libro:
    #metodo costruttore con 3 attributi
    def __init__(self, titolo:str, autore:str, pagine:int):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine

    #metodo istanza per stampare stringa
    def descrizione(self):
        return f"Il libro {self.titolo} è stato scritto da {self.autore} e ha {self.pagine} pagine."

class Biblioteca:
    #metodo costruttore con attributo lista libri vuota
    def __init__(self):
        self.libri = []

    #metodo per aggiunere oggetto libro in list libria 
    def aggiungi_libro(self, libro):
        self.libri.append(libro)

    #metodo per stampare i libri disponibili tramite metodo descrizione dell'oggetto libri 
    def stampa_libri(self):
        if not self.libri:
            print("La biblioteca è vuota.")
        else:
            for libro in self.libri:
                print(libro.descrizione())

#oggetto biblioteca
biblioteca = Biblioteca()

#oggetto libri
libro1 = Libro("Il piccolo principe", "Antoine de Saint-Exupéry", 96)
libro2 = Libro("Divina Commedia", "Dante Alighieri", 700)

#metodi aggiungi libri
biblioteca.aggiungi_libro(libro1)
biblioteca.aggiungi_libro(libro2)

#metodo stampa tutti i libri che ci sono
biblioteca.stampa_libri()
