'''
1: non puoi guidare perchè sei minorenne
2: non puoi guidare perchè non hai la patente
3: non puoi guidare perchè hai bevuto
4: puoi guidare
'''

eta = 32
ha_patente = True
ha_bevuto = False

if eta < 18:
    messaggio = f"Non puoi guidare perché sei minorenne"
elif not ha_patente:
    messaggio = f"Non puoi guidare perché non hai la patente"
elif ha_bevuto:
    messaggio = f"Non puoi guidare perché hai bevuto"
else:
    messaggio = f"Puoi guidare"

print(messaggio)

'''
operatore ternario per restiture output senza troppe righe di codice
'''

print("maggiorenne " if eta>=18 else "minorenne")

var = "maggiorenne" if eta>=18 else "minorenne"



if eta < 18:
    messaggio = f"Non puoi guidare perché sei minorenne"
else:
    pass


'''
ciclo while
'''
lista = []
num1 = input("Inserisci un numero:")
lista.append(num1)

num2 = input("Inserisci un numero:")
lista.append(num2)

num3 = input("Inserisci un numero:")
lista.append(num3)
'''
counter = 0

while counter<3: #finchè counter è vero il programma continua
    num = input("Inserisci un numero:")
    lista.append(num)
    counter+=1

'''

#ciclo for sappiamo quante volte far girare un programma mentre while quando non è definito

#ciclo infinto, esco con break

while True:
    uscita= input("Vuoi uscire?")
    if uscita == "si":
        break
    print("Continua ciclo")

#continue salta tutto quello che c'è dopo e riparte da sopra
'''
bitcoin = "salita"
while True:
    if bitcoin == "discesa":
        continue

    print("invest")
'''

##liste
lista =[1,1.4, "stringa", ["zero", "uno", "due"]]
print(lista[0])
print(lista[-1][1]) # perchè lista in una lista, -1 ultimo elemento

#slicing per creare una sotto lista ovvero sottoinsieme per manipolare le liste
lista = ["zero", "uno", "due", "tre", "quattro", "cinque"]
lista2 = lista[1:5] #indice iniziale fino indice escluso
lista2 = lista[:5]  #con elemento iniziale sottintendo
lista2 = lista[1:]  #fino ultimo elemento
lista2 = lista[::-1]  #passo -1 , inverto lista
lista2 = lista[1:5:2]   #passo di 2

lista = ["zero", "uno", "due", "tre", "quattro", "cinque"]
#lista.append()
lista.insert(1, "altro") #inserisco altro in indice 1, spostando
lista[1] ="altro" #sovrascrivo in indice 1

#estende
lista2=[1,2,3]
#lista.extend(lista2)
#print(lista) 

#ordinamento
lista.sort(reverse=True) #ordina gli elementi
lista.reverse() #li restituisce al contrario
print(lista)

#index per sapere l'indice di un elemento
print(lista.index("tre"))

#per rimuovere elemento
#lista.remove("tre")
#del lista[3]
lista.pop()  #elimina ultimo elemento
lista.pop() #elimina elemento in indice 3
print(lista)

#verifica inizio stringa
var="ciao a tutti"
var.startswith("ci")
var.endsswith("tutti")

#controllo se possiede tutti numeri
print(var.isisalnum()) #controllo se possiede tutti numeri
print(var.isisalpha()) #solo caratteri alfabetici
print(var.isdecimal()) #controllpo valori decimali 

#converto valori tutto maiuscolo o tutto minuscolo
var ="CiAO"
var.lower()
var.upper()

#replace di parola
var = "ciao a tutti"
var2 = var.replace("tutti", "qualcuno")

#conteggio occorrenze di sottostringhe all'interno di una stringa
print(var.count("i"))

nomi = "tommaso michele alfredo teresa"
nomiL = nomi.split()
len(nomiL)

lista = ['tommaso', 'michele', 'alfredo', 'teresa']
nome1,nome2,nome3,nome4 = lista
nome1,_,_,_ = lista  #_segnaposto

#join
lista = ['tommaso', 'michele', 'alfredo', 'teresa']
sep="-"
stringa = sep.join(lista)   #contrario di split, prend elementi di lista e li unisce con il separatore

#slicing
stringa = "ciao a tutti"
stringa2 = stringa[1:5]
print(stringa2)

#operatori di appenteneza in 
print("ciao" in stringa)
#nella lista elem separati la virgola, in stringa elementi vicini

#ciclo for
lista = ['tommaso', 'michele', 'alfredo', 'teresa']
stringa = "ciao a tutti"
for name in lista:
    print(name)

for char in stringa:
    print(char)

print('dopo', char) #ultimo carattere

##for 
count=0
while count<3:
    print("ciao")
    count+=1

lista =[1,2,3]
for el in lista:
    print("ciao")

for el in range(3): #iterabile con numero di elementi che voglio
    print("ciao")

print(list(range(1,10,2)))
print(list(range(10,1,-1))) #iter all'indietro

#while quando non so in anticipo quante iter fa il programma

lista = ['tommaso', 'michele', 'alfredo', 'teresa']
for nome in lista:
    print(nome)

index=0
while index<len(lista):
    print(lista[index])
    index+=1

#list comprension
lista = ['tommaso', 'michele', 'alfredo', 'teresa']
lista2 = []

for nome in lista:
    if "a" in nome:
        lista2.append(nome)

print(lista2)
# primo elem cosa mettere in lista, inserisci questo per ogni elementoi in lista se inizia con a
lista3=[nome for nome in lista if "a" in nome]  #list comprension

### tupla
lista=[1,2,3]
tupla =(1,2,3) #immutabili
set1={1,2,3}
set1.add("add") #per aggiungere elementi

#dizionari
#metodi per archiviare dati 
cliente1 ={"nome":"tommaso", "cognome":"muraca", "eta":39}
cliente2 ={"nome":"eli", "cognome":"carella", "eta":32}
for key in cliente1:
    print(key)

clienti ={1:cliente1, 2:cliente2}

#richiamare tutti i nomi
for key in clienti:
    print(clienti[key]["nome"])

for key, value in clienti.items():
    print(key, value) # dict items


print(cliente1.items())
print(cliente1.keys())
print(cliente1.values())
print(cliente1.get("nome", "elemento non trovato")) #cerco elemento e se non trova dà indicazione
print(cliente1.setdefault("indirizzo", "elemento non trovato"))#cerca elemento se non trova aggiunge quello come chiave e come secondo il value

#funzione iterabile max, sum, min, enumerate, 
lista =["tommaso", "alfredo", "teresa"]
for i, nome in enumerate(lista):
    print(f"indice:{i}, nome:{nome}")

#sorted ordina un iterabile dal più piccolo al più grande, 
tupla =(5,1,12,7,3)
print(sorted(tupla, reverse=True))

diz1={nome:1 for nome in lista if "a" in nome}  #aggiunge valori in lista come chiavi
print(diz1)
