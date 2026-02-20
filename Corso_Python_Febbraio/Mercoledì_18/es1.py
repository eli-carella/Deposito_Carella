'''
Trasformate il programma che abbiamo creato in
precedenza per la gestione dei voti degli alunni in un
programma per la gestione di una classe che utilizza un
file come database:
All’avvio il programma chiede se si vuole leggere l’elenco
degli alunni e i loro voti e medie, se si vuole aggiungere un
alunno o un voto
'''
import os

FILE_DB = "studenti.txt"

# Funzione per salvare il dizionario su file
def salva_file(diz_studenti):
    listaC = []
    for nome, info in diz_studenti.items():
        voti_str = [str(v) for v in info["voti"]]
        listaC.append(",".join([nome] + voti_str))
    stringaF = "\n".join(listaC)
    with open(FILE_DB, "w") as file:
        file.write(stringaF)

# Funzione per caricare dati dal file
def carica_file():
    diz_studenti = {}
    if os.path.exists(FILE_DB):
        with open(FILE_DB, "r") as file:
            righe = file.readlines()
            for riga in righe:
                elementi = riga.strip().split(",")
                nome = elementi[0]
                voti = [float(v) for v in elementi[1:]] if len(elementi) > 1 else []
                diz_studenti[nome] = {"voti": voti, "media": 0}
    return diz_studenti

# Calcola medie
def calcola_medie(diz_studenti):
    for nome in diz_studenti:
        voti = diz_studenti[nome]["voti"]
        diz_studenti[nome]["media"] = sum(voti)/len(voti) if voti else 0

# Carico dati esistenti
diz_studenti = carica_file()
calcola_medie(diz_studenti)

# Menu principale
while True:
    print("\n--- Gestione Classe ---")
    print("1. Leggere l'elenco degli alunni e voti/medie")
    print("2. Aggiungere un nuovo alunno")
    print("3. Aggiungere un voto a un alunno")
    print("4. Esci")

    scelta = input("Scegli un'opzione (1-4): ")

    if scelta == "1":
        calcola_medie(diz_studenti)
        opzione = input("Vuoi stampare 'media' o tutti i 'voti'? ")
        if opzione.lower() == "media":
            print("\nMedie degli alunni:")
            for nome in diz_studenti:
                print(f"{nome}: {diz_studenti[nome]['media']}")
        elif opzione.lower() == "voti":
            print("\nTutti i voti:")
            for nome in diz_studenti:
                print(f"{nome}: {diz_studenti[nome]['voti']}")
        else:
            print("Opzione non valida.")

    elif scelta == "2":
        nome = input("Inserisci il nome dell'alunno: ")
        if nome in diz_studenti:
            print("Alunno già presente!")
        else:
            diz_studenti[nome] = {"voti": [], "media": 0}
            salva_file(diz_studenti)
            print(f"Alunno {nome} aggiunto.")

    elif scelta == "3":
        nome = input("Inserisci il nome dell'alunno: ")
        if nome not in diz_studenti:
            print("Alunno non trovato!")
        else:
            try:
                voto = float(input("Inserisci il voto: "))
                diz_studenti[nome]["voti"].append(voto)
                calcola_medie(diz_studenti)
                salva_file(diz_studenti)
                print(f"Voto aggiunto a {nome}.")
            except ValueError:
                print("Valore del voto non valido!")

    elif scelta == "4":
        print("Uscita dal programma.")
        break

    else:
        print("Opzione non valida. Riprova.")
