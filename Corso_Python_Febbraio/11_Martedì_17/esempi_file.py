### gestione file
#file csv   comma separeted value 
#formato standard tabellare serve per gestire file ad esempio da un gestionale, oppure scaricare file da sito web
#molto leggero e può archiviare file in modo strutturato perchè è una tabella strutturata
#pandas ha funzione per leggere file csv

#con with significa che finchè sei dentro il file è aperto, quando si esce da with il file è chiuso
# r leggere, 
# a appendere ovvero aggiungere alla fine, 
# w write sovrascivere, 
# x solo per creare il file

def leggifile():
    with open("file.txt", "r") as file:
        contenuto = file.read()  #leggo tutto file
    return contenuto

cont = leggifile()
print(cont)

def scrivifile():
    with open("file2.txt", "w") as file: #w se file già esistente sovrascrive
        file.write("ciao")  #scrivo nel file

def scrivifile():
    with open("file2.txt", "a") as file: #qui se è già presente file aggiungi e scrive
        file.write("ciao")  #scrivo nel file

scrivifile()

listaR = cont.split("\n")   #per separare righe con spazio a capo e avere lista con per ogni riga
print(listaR)
matrice=[x.split(",") for x in listaR]  #lista di liste
print(matrice) 

for riga in range(len(matrice)):
    if matrice[riga][1] == "rossi":
        matrice[riga][1] == "verdi"

print(matrice)

for riga in range(1,len(matrice)): #salta intestazione
    if matrice[riga][1] == "rossi":
        matrice[riga][1] == "verdi"

#con join inverso di spit unisce in un'unica 
listaC=[]

for riga in matrice:
    listaC.append(",".join(riga))

listaC2 = [",".join(x) for x in matrice]
print(listaC2)

stringaF = "\n".join(listaC2)
print(stringaF)

#con matrice posso troavre elementi con matrice[][]

def scrivifile(stringa):
    with open("file2.txt", "w") as file:  #sovrascrive con quella stringa
        file.write(stringa)

scrivifile(stringaF)
