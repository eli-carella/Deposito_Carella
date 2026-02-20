'''
Scrivete un programma che prenda i nomi degli alunni di una
classe e i loro voti, quando l’utente scrive media il programma
andrà a stampare i nomi di tutti gli alunni e per ogni alunno la
media dei voti.
Esempio:
Nome: Giovanni , Media: 7.5
Nome: Alfredo , Media: 9
Nome: Michela, Media 10
'''

diz_studenti = {}

while True:
    nome = input("inserisci nome: ")
    voto = float(input("inserisci voto: "))

    # Se il nome non è ancora nel dizionario lo aggiungo
    if nome not in diz_studenti:
        diz_studenti[nome] = {"voti": [], "media": 0}

    # Aggiungo il voto alla lista dello studente
    diz_studenti[nome]["voti"].append(voto)

    scelta = input("vuoi uscire? (s/n) ")
    if scelta == 's':
        break

# Calcolo media
for nome in diz_studenti:
    voti = diz_studenti[nome]["voti"]
    diz_studenti[nome]["media"] = sum(voti) / len(voti)


# Scelta finale visualizzare tutti o media
scelta_finale = input("Vuoi stampare 'media' o visualizzare 'tutti' i valori? ")

if scelta_finale == "media":
    print("\n Medie degli alunni")
    for nome in diz_studenti:
        print(f"Nome: {nome} , Media: {diz_studenti[nome]['media']}")

elif scelta_finale == "tutti":
    print("\n Tutti i voti")
    for nome in diz_studenti:
        print(f"Nome: {nome}")
        print(f"Voti: {diz_studenti[nome]['voti']}")


