#Esercizio 1:
# Scrivi un program,ma che chieda all'utente l'età. 
# se l'età è inferiore a 18 anni il programma dovrebbe stampare "mi dispiace, non puoi vedere questo film"
# altrimenti dovrebbe stampare "puoi vedere questo film".

eta = int(input("Inserisci la tua età: "))

if eta < 18:
    print("Mi dispiace, non puoi vedere questo film")
else:
    print("Puoi vedere questo film")


eta = int(input("Inserisci la tua età: "))

match eta >= 18:
    case True:
        print("Puoi vedere questo film")
    case False:
        print("Mi dispiace, non puoi vedere questo film")

