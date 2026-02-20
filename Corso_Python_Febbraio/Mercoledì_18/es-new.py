
NOME_FILE = "voti.csv"


def scriviFile(nome_file, diz_studenti):
    stringa_totale = convertiDictToStr(diz_studenti)
    with open(nome_file, "w") as file:
        file.write(stringa_totale)


def leggFile(nome_file):
    with open(nome_file, "r") as file:
        contenuto = file.read()
    dizionario_totale = convertiStrToDict(contenuto)
    return dizionario_totale


def convertiDictToStr(dizionario):
    strg = ""                                   #Stringa
    for chiave, valore in dizionario.items():
        strg += f"{chiave},{"-".join(valore)}\n" # "-".join(valore) = "-".join(map(str, valore))
    #print(strg.strip("\n"))
    return strg.strip("\n")


def convertiStrToDict(stringa):
    diz = {}
    lista_strg = stringa.split("\n")            #Stringa
    for riga in lista_strg:
        parti = riga.split(",")                     #Stringa
        chiave = parti[0]                           #Stringa
        valore = parti[1]                           #Stringa
        elementi = valore.split("-")                #Lista di Stringhe Numeriche
        numeri = list(map(int, elementi))           #Lista di Interi
        diz[chiave] = numeri
    #print(diz)
    return diz


# MAIN
studenti = {}

'''
try:
    with open(f"{NOME_FILE}", "r") as file:
        studenti = file.read()
        convertiDictToStr(stu)
except FileNotFoundError:
    print("Errore, file non trovato!")
'''
while True:
    print("Menu")
    print("1. Aggiungi Alunno")
    print("2. Aggiungi Voto")
    print("3. Stampa Studenti e Medie")
    scelta = input("Cosa vuoi fare? ")

    match scelta:
        case "1":
            if type(studenti) == str:
                studenti = convertiStrToDict(studenti)
            while True:
                nome = input("Inserisci studente: ").lower()
                if nome not in studenti.keys():
                    print("Studente Inserito!")
                    break
                print("Studente già presente!")
            studenti[nome] = []
            scriviFile(NOME_FILE, studenti)
        case "2":
            if type(studenti) == str:
                studenti = convertiStrToDict(studenti)
            nome = input("Inserisci studente: ").lower()
            if nome in studenti.keys():
                voto = input("Inserisci il voto: ")
                if len(studenti[nome]) == 0:
                    studenti[nome] = [voto]
                else:
                    studenti[nome].append(voto)
                scriviFile(NOME_FILE, studenti)
                print("Voto Inserito!")
            else:
                print("Studente non in elenco!")
        case "3":
            studenti = leggFile(NOME_FILE)
            if len(studenti) != 0:
                for nome, voti in studenti.items():
                    # Filtra eventuali stringhe vuote
                    voti_numerici = [v for v in voti if v != ""]
                    
                    # Controlla che ci siano voti validi
                    if len(voti_numerici) > 0:
                        media = sum(voti_numerici) / len(voti_numerici)
                        print(f"Nome: {nome}, Media: {media}")
                    else:
                        print(f"Nome: {nome}, Nessun voto inserito")
            else:
                print("Nessuno studente trovato!")
        case _:
            print("Input Errato")
    print("")