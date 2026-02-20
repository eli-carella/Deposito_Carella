#esempi funzioni

def somma():
    print(5+5)
somma()


def somma(a, b):
    print(a+b)
somma(1,2)

def somma(a, b=0):
    print(a+b)
somma(10)  # b=0 di default

def somma(a=False, b=0, c=1):
    print(a+b/c)
somma(15, c=5)

#trasformo elementi passati in un dizionario
def somma(**a):
    print(type(a))
    print(a["num1"]+1)
somma(num1=15,num2=5,num3=10)

def somma(a,b):
    print(a+b)
val = somma(5,10)
print(val)  #None perchè funzione non ha return


def somma(a,b):
    val=a+b
    print(val)
val = somma(5,10)
print(val)  #qui ritorna val

eta=18
def aumentaEtà(eta): # variabile locale eta
    eta = eta+1

print(eta)
aumentaEtà(eta)
print(eta) #eta non cambia perchè eta è variabile locale nella funzione

eta=18
def aumentaEtà(): # variabile locale eta
    global eta
    eta = eta+1

print(eta)
aumentaEtà()
print(eta) #eta cambia perchè eta è variabile globale nella funzione

numero=15
def funzMy(a):
    print(a+numero) #funziona perchè serve solo il valore
funzMy(10)

def funzMy():
    val=15
funzMy()
print(val)  #non funziona perchè è esterna alla funzione, 


numeri = [1,2,3,4,5]
numeri2=[]
for n in numeri:
    numeri2.append(n*3)
print(numeri2)


def moltiplica(a):
    return a*3

numeri22=[]
for n in numeri:
    numeri22.append(moltiplica(n))
print(numeri22)

## funzione map
numeri = list(map(moltiplica, numeri)) #applica ad ogn el di numeri la funzione moltiplica e lo converte in lista

def pari(n):
    return n%2 ==0

numeri = [1,2,3,4,5]
numeri2=[]
for n in numeri:
    n2 = pari(n)
    if n:
        numeri2.append(n)
print(numeri2)

### filter
numeri = list(filter(pari, numeri))
print(numeri)


## lambda function funzione temporanea
def doppioNumero(x):
    return x*x

lambda x:x*x

numeri=[1,2,3,4,5]

numeri = list(map(lambda x: x*3, numeri))


