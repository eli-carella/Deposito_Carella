#gestione errori
numero = input("inserisci un numero")
print(int(numero)+5)
print("eseguo programma")

#try except per gestire gli errori, prova a fare questo codice se c'è un errore allora fai questo
try:
    print(int(numero)+5)
except ValueError as e:   #intercetta value error 
    print("numero non valido", e)   # riporta errore contenuto di valueerror
except TypeError as e:   #intercetta type error 
    print("tipo non valido", e)
except:
    print("errore!") #altri tipi di errore
print("eseguo programma")