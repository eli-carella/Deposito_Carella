"""
Crea una classe chiamata Libro. 
Questa classe dovrebbe avere: Tre attributi: titolo, autore e pagine. 
Un metodo descrizione che restituisca una stringa del tipo "Il libro 'titolo' è stato scritto da 'autore' e ha 'pagine' pagine.".
"""

class Libro:
    def __init__(self, titolo:str, autore:str, pagine:int):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine

    def descrizione(self):
        return f"Il libro {self.titolo} è stato scritto da {self.autore} e ha {self.pagine} pagine."

libro_OBJ = Libro("Divina Commedia", "Dante Alighieri", 700)
print(libro_OBJ.descrizione())