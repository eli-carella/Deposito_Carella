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