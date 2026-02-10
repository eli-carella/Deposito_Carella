'''
Requisiti:
1.Definizione della Classe:
Creare una classe chiamata Ristorante.
La classe dovrebbe avere un costruttore __init__ che accetta due parametri: nome (nome del ristorante) e
tipo_cucina (tipo di cucina offerta).
Definire un attributo aperto che indica se il ristorante è aperto o chiuso. Questo attributo deve essere
impostato su False di default (cioè, il ristorante è chiuso).
Un dizionario menu dove dentro ci sono i piatti e prezzi che ha il ristorante
2.Metodi della Classe:
descrivi_ristorante(): Un metodo che stampa una frase descrivendo il ristorante, includendo il nome e il
tipo di cucina.
stato_apertura(): Un metodo che stampa se il ristorante è aperto o chiuso.
apri_ristorante(): Un metodo che imposta l'attributo aperto su True e stampa un messaggio che indica che
il ristorante è ora aperto.
chiudi_ristorante(): Un metodo che imposta l'attributo aperto su False e stampa un messaggio che indica
che il ristorante è ora chiuso.
aggiungi_al_menu(): Un metodo per aggiungere piatti al menu
togli_dal_menu(): Un metodo per togliere piatti al menu
stampa_menu(): Un metodo per stampare il menu
3.Testare la Classe:
Creare un'istanza della classe Ristorante, passando i valori appropriati al costruttore.
Testare tutti i metodi creati per assicurarsi che funzionino come previsto.
'''

class Ristorante:

    #metodo costruttore
    def __init__(self, nome:str, tipo_cucina:str):
        self.nome = nome
        self.tipo_cucina = tipo_cucina
        self.aperto = False
        self.menu={}

    #descrizione ristorante
    def descrivi_ristorante(self):
        return f"Il ristorante {self.nome} è e fa cucina {self.tipo_cucina}."

    # aperto true
    def apri_ristorante(self):
        self.aperto = True
        print(f"Il ristorante {self.nome} è ora aperto")

    #aperto false
    def chiudi_ristorante(self):
        self.aperto = False
        print(f"Il ristorante {self.nome} è ora chiuso.")

    #print stato aperto/chiuso
    def stato_apertura(self):
        if(self.aperto==True):
            print("Il ristorante è aperto")
        else:
            print("Il ristorante è chiuso")

    # aggiungi piatto al dict vuoto menu chiave nome piatto valore prezzo
    def aggiungi_al_menu(self, piatto, prezzo):
        self.menu[piatto] = prezzo
        print(f"'{piatto}' aggiunto al menu al prezzo di {prezzo} €.")

    #ciclo su dict menu ed elimino l'item con chiave passata da argomento
    def togli_dal_menu(self, piatto):
        if piatto in self.menu:
            del self.menu[piatto]
            print(f"'{piatto}' rimosso dal menu.")
        else:
            print(f"'{piatto}' non è presente nel menu.")

    #stampa menu, se non è vuoto ciclo su chiave - valore di dict menu e stampo piatto e prezzo corrispondente
    def stampa_menu(self):
        if not self.menu:
            print("Il menu è vuoto.")
        else:
            print("Menu del ristorante:")
            for piatto, prezzo in self.menu.items():
                print(f"{piatto}: {prezzo} €")

    # extra applica sconto sul prezzo del menu, ciclo su valori di dict menu e cambio il valore del prezzo moltiplicandolo per la percentuale
    def applica_sconto(self, percentuale):
        if self.aperto:
            for piatto in self.menu:
                self.menu[piatto] *= (1 - percentuale / 100)



#creo oggetto
ristorante_OBJ = Ristorante("La rustica", "italiana")

#utilizzo funzioni 
print(ristorante_OBJ.descrivi_ristorante())
ristorante_OBJ.stato_apertura()
ristorante_OBJ.apri_ristorante()

ristorante_OBJ.aggiungi_al_menu("Pizza Margherita", 5)
ristorante_OBJ.aggiungi_al_menu("Pasta Carbonara", 8)

ristorante_OBJ.stampa_menu()

ristorante_OBJ.togli_dal_menu("Pizza Margherita")
ristorante_OBJ.stampa_menu()

ristorante_OBJ.chiudi_ristorante()

ristorante_OBJ.apri_ristorante()
ristorante_OBJ.applica_sconto(15)
ristorante_OBJ.stampa_menu()
