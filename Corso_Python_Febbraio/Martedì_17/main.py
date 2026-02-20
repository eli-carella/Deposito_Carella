#map applica funzione a tutti gli ele di un iterabile

lista = [1,2,3,4]
def triplica(n):
    return n*3

lista=list(map(triplica, lista))

#filter filtra elem di iterabile sulla base di una funzione

def pari(n):
    return n%2 == 0  #True se pari, False dispari
#con filter la funzione deve ritornare true / false
lista = list(filter(pari, lista))


#gestione errori
numero = input("inserisci numero")
try:  #testa codice se ho problemi entra in except
    print((int(numero)+5))
    print(5/(int(numero)))
except ValueError as e:
    print("non hai inserito un  numero", e)
except ZeroDivisionError as e:
    print("stai divedendo per 0", e)
except:
    print("errore generico")
finally:
    print("esegui sempre")


#file csv ha struttura con valori separati da , 
#r lettura
#w scrittura o sovrascrittura
#a scrittura o aggiunta
#x creare il file
#with crea gestione del contesto, chiude file quando esci da questo contesto ovvero identazione
with open("file.txt", "r") as file:
    contenuto = file.read()

print(contenuto)

with open("filecsv2.txt", "w") as file:
    file.write("il mio primo file\nseconda riga")

#con append se esiste già il file aggiunge il testo
with open("filecsv2.txt", "a") as file:
    file.write("il mio primo file\nseconda riga")

righe=contenuto.split("\n") #lista 
print(righe)

matrice1 = []
for riga in righe:
    matrice1.append(riga.split(","))

print(matrice1)

for riga in range(1, len(matrice1)):
    if matrice1[riga][0] == "teresa":
        matrice1[riga][1] = "blu"
#list comprension
#matrice=[riga.split(",") for riga in righe]

listaStringhe = []
for riga in matrice1:
    listaStringhe.append(",".join)

strigaFinale = "\n".join(listaStringhe)

with open("filecsv.txt", "w") as file:
    file.write(strigaFinale)
