#librerie della standard library, es random
import random as rd  #importa tutta la libreria
print(rd.random)

from random import randint, choice #import singole librerie

print(randint(1, 100))

lista=[1,2,23,100]
print(choice(lista))

#librerie esterne
import funzioni
funzioni.somma(10, 12)
funzioni.divisione(10, 2)

import lib.funzioni
lib.funzioni.somma(10, 12)

## libreria datetime in stardard library 
import datetime

print(datetime.time(15,40,00))
print(datetime.datetime(2026,2,17, 15,40,00))
print(datetime.datetime.now()) #data odierna
print(datetime.datetime.now().month)
print(datetime.datetime.now().year)

#pip list
#pip install pandas
#pip unistall pandas







