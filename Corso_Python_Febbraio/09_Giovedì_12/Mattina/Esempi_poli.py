# duck typing

class Cane:
    def parla(self):
        return "Bau!"

class Gatto:
    def parla(self):
        return "Miao!"

#funzione polimorfica
def fai_parlare(animale):
    # Non importa di che tipo sia l'animale,
    print(animale.parla())

cane = Cane()
gatto = Gatto()

fai_parlare(cane) # Output: Bau!
fai_parlare(gatto) # Output: Miao!