'''
Parte UNO:
Scrivere un Sistema che utilizza NumPy per gestire una matrice 2D.
Il programma deve presentare un menu interattivo che consente all'utente di eseguire varie operazioni sulla matrice. 
Le operazioni disponibili includono, ogni volta che il sistema conclude un calcolo va salvato su un file txt:
1. Creare una nuova matrice 2D di dimensioni specificate da utente con numeri casuali.
2. Estrarre e stampare la sotto-matrice centrale.
3. Trasporre la matrice e stamparla.
4. Calcolare e stampare la somma di tutti gli elementi della matrice.
5. Uscire dal programma o ripetere .
'''
import numpy as np

FILE_NAME = "risultati_matrice.txt"

#salva su file i risultati
def salva_su_file(testo):
    with open(FILE_NAME, "a") as file:
        file.write("\n" + "="*50 + "\n")
        file.write(testo + "\n")

#crea una matrice con numeri random con righe e colonne da input
def crea_matrice():
    righe = int(input("Inserisci numero di righe: "))
    colonne = int(input("Inserisci numero di colonne: "))
    
    matrice = np.random.randint(0, 100, size=(righe, colonne))
    print("\nMatrice creata:\n", matrice)
    
    salva_su_file("Matrice creata:\n" + str(matrice))
    return matrice

# prende sottomatrice centrale 3X3
def sottomatrice_centrale(matrice):
    righe, colonne = matrice.shape
    
    centro_r = righe // 2
    centro_c = colonne // 2
    
    sotto = matrice[centro_r-1:centro_r+2, centro_c-1:centro_c+2]
    
    print("\nSottomatrice centrale:\n", sotto)
    salva_su_file("Sottomatrice centrale:\n" + str(sotto))

#calcolo matrice trasposta
def trasponi_matrice(matrice):
    trasposta = matrice.T
    print("\nMatrice trasposta:\n", trasposta)
    salva_su_file("Matrice trasposta:\n" + str(trasposta))

#calcola somma di tutti gli elementi della matrice
def somma_elementi(matrice):
    somma = np.sum(matrice)
    print("\nSomma di tutti gli elementi:", somma)
    salva_su_file("Somma elementi: " + str(somma))

def moltiplicazione_matrici(matrice):
    righe, colonne = matrice.shape
    
    print("\nCreazione seconda matrice delle stesse dimensioni.")
    seconda = np.random.randint(0, 100, size=(righe, colonne))
    
    print("\nSeconda matrice:\n", seconda)
    
    risultato = matrice * seconda
    
    print("\nRisultato moltiplicazione element-wise:\n", risultato)
    
    salva_su_file(
        "Seconda matrice:\n" + str(seconda) +
        "\n\nRisultato moltiplicazione element-wise:\n" + str(risultato)
    )

#calcolo media matrice
def calcolo_media(matrice):
    media = np.mean(matrice)
    print("\nMedia:", media)
    salva_su_file("Media: " + str(media))

#calcolo determinante
def calcolo_determinante(matrice):

    #controllo matrice quadrata
    if matrice.shape[0] != matrice.shape[1]:
        print("Errore: La matrice deve essere quadrata!")
    else:
        det = np.linalg.det(matrice)
        print("\nDeterminante:", det)
        salva_su_file("Determinante: " + str(det))


matrice = None
    
while True:
    print("\n===== MENU =====")
    print("1. Creare nuova matrice 2D casuale")
    print("2. Estrarre sottomatrice centrale")
    print("3. Trasporre la matrice")
    print("4. Somma di tutti gli elementi")
    print("5: Moltiplicazione con una seconda matrice")
    print("6: Calcolo media")
    print("7: Calcolo determinante")
    print("8. Uscire")
    
    scelta = input("Scegli un'opzione: ")
    
    if scelta == "1":
        matrice = crea_matrice()

    elif scelta == "2":
        if matrice is not None:
            sottomatrice_centrale(matrice)
        else:
            print("Devi prima creare una matrice.")

    elif scelta == "3":
        if matrice is not None:
            trasponi_matrice(matrice)
        else:
            print("Devi prima creare una matrice.")

    elif scelta == "4":
        if matrice is not None:
            somma_elementi(matrice)
        else:
            print("Devi prima creare una matrice.")

    elif scelta == "5":
        if matrice is not None:
            moltiplicazione_matrici(matrice)
        else:
            print("Devi prima creare una matrice.")

    elif scelta == "6":
        if matrice is not None:
            calcolo_media(matrice)
        else:
            print("Devi prima creare una matrice.")

    elif scelta == "7":
        if matrice is not None:
            calcolo_determinante(matrice)
        else:
            print("Devi prima creare una matrice.")

    elif scelta == "8":
        print("Uscita dal programma.")
        break

    else:
        print("Scelta non valida. Riprova.")