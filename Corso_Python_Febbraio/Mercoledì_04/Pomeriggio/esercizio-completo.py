'''
# ES 1
# Scrivere un programma che prende in input un numero e stampa:
# Pari se il numero è pari
# Dispari se il numero è dispari

numero = int(input("Inserisci un numero: "))

if numero % 2 == 0:
    print("Pari")
else:
    print("Dispari")


# ES 2
# Scrivere un programma che prende in input un numero intero positivo n 
# e stampa tutti i numeri da n a 0 (compreso), decrementando di 1.
n = int(input("Inserisci un numero positivo: "))

while n>=0:
    print(n)
    n=n-1

## ES 3 
testo = input("Inserisci numeri separati da spazio: ")
parti = testo.split()

for p in parti:
    print(int(p)**2)

'''

# ES 4
# Il programma deve:
# controllare se la lista è vuota
# trovare il numero massimo
# contare quanti numeri ci sono
# if controlla se la lista è vuota
# for trova il massimo
# while conta gli elementi

testo = input("Inserisci numeri separati da spazio: ")

numeri = []

controllo = "si"
while controllo == "si":
    valore = int(input("Inserisci un numero: "))
    numeri.append(valore)
    controllo = input("Vuoi inserire un altro numero? (si/no): ")

if len(numeri) == 0:
    print("Lista Vuota")
else:
    massimo = numeri[0]

    for n in numeri:
        if n > massimo:
            massimo = n

    i = 0
    count = 0
    while i < len(numeri):
        count = count + 1
        i = i + 1

    print("Numero massimo:", massimo)
    print("Numero di elementi:", count)
