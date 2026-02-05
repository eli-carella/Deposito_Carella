conteggio=0

while conteggio <5:
    print(conteggio)
    conteggio += 1


controllore = True
while controllore:
    print("oh no")

    esci = input("Vuoi uscire - Sì o NO")
    if esci.lower() == "sì":
        controllore = False
    else:
        controllore = True


numeri = [1, 2, 3, 4, 5]
for numero in numeri:
    print(numero)

stringa = "elisabetta"
for l in stringa:
    print(l)

for i in range(5):
    print(i)

for c in range(0, 21, 2):
    print(c)

for c in range(0, 21, 1):
    print(c)

limite = int(input("scegli il tuo limite che non viene raggiunto"))
for i in range(limite):
    print(i)

#break
numeri = [1, 2, 3, 4, 5]
for numero in numeri:
    if numero == 3:
        break
    print(numero)

#continue
numeri = [1, 2, 3, 4, 5]
for numero in numeri:
    if numero == 3:
        continue
    print(numero)

#pass
for i in range(5):
    if i == 3:
        pass
    print(i)

#splat
numeri = [*range(1, 11)]
print(numeri)
# output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]