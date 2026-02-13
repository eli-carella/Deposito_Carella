import Controlli
import Utenti

def main():
    # Creazione oggetti utenti
    dip1 = Utenti.Dipendente("Lucia Rossi", "B123", "Produzione")
    man1 = Utenti.Manager("Anna Bianchi", "M456", "Direzione")

    # Creazione oggetto sistema di controllo
    sistema = Controlli.ControlloAccessi()

    # tentativi di accessi con metodo verifica_accessi
    print("Tentativo accesso area livello 1:")
    sistema.verifica_accesso(dip1, 1)

    print("Tentativo accesso area livello 2:")
    sistema.verifica_accesso(dip1, 2)

    print("Tentativo accesso area livello 2:")
    sistema.verifica_accesso(man1, 2)

    # Stampa log con cronologia accessi
    sistema.mostra_log()


if __name__ == "__main__":
    main()

