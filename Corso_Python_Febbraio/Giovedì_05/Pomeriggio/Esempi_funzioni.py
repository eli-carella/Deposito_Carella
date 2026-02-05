"""
PANORAMICA COMPLETA SULLE FUNZIONI IN PYTHON
- Definizione e chiamata
- Parametri e return
- Parametri opzionali
- Scope (locale / globale)
- Funzioni con condizioni
- Funzioni con cicli
- Funzioni che lavorano con liste e dizionari
- Funzioni come "mattoni" di un programma
"""

# ==============================================================
# 1. FUNZIONE SEMPLICE (SENZA PARAMETRI, SENZA RETURN)
# ==============================================================

def saluta():
    print("Ciao! Questa è una funzione semplice.")

saluta()


# ==============================================================
# 2. FUNZIONE CON PARAMETRI
# ==============================================================

def saluta_persona(nome):
    print("Ciao", nome)

saluta_persona("Mario")
saluta_persona("Anna")


# ==============================================================
# 3. FUNZIONE CON RETURN
# ==============================================================

def somma(a, b):
    risultato = a + b
    return risultato

totale = somma(5, 7)
print("Risultato somma:", totale)


# ==============================================================
# 4. PARAMETRI OPZIONALI (DEFAULT)
# ==============================================================

def moltiplica(a, b=2):
    return a * b

print("Moltiplica 5 * 2:", moltiplica(5))
print("Moltiplica 5 * 4:", moltiplica(5, 4))


# ==============================================================
# 5. FUNZIONE CON CONDIZIONI
# ==============================================================

def verifica_maggiorenne(eta):
    if eta >= 18:
        return "Maggiorenne"
    else:
        return "Minorenne"

print("Età 20:", verifica_maggiorenne(20))
print("Età 15:", verifica_maggiorenne(15))


# ==============================================================
# 6. FUNZIONE CON CICLO FOR
# ==============================================================

def stampa_numeri(n):
    for i in range(1, n + 1):
        print(i, end=" ")
    print()

stampa_numeri(5)


# ==============================================================
# 7. FUNZIONE CON CICLO WHILE
# ==============================================================

def conto_alla_rovescia(n):
    while n > 0:
        print(n)
        n -= 1
    print("Via!")

conto_alla_rovescia(3)


# ==============================================================
# 8. FUNZIONE CHE LAVORA CON UNA LISTA
# ==============================================================

def somma_lista(numeri):
    totale = 0
    for n in numeri:
        totale += n
    return totale

lista = [2, 4, 6, 8]
print("Somma lista:", somma_lista(lista))


# ==============================================================
# 9. FUNZIONE CHE FILTRA UNA LISTA
# ==============================================================

def numeri_pari(numeri):
    pari = []
    for n in numeri:
        if n % 2 == 0:
            pari.append(n)
    return pari

print("Numeri pari:", numeri_pari([1, 2, 3, 4, 5, 6]))


# ==============================================================
# 10. FUNZIONE CON DIZIONARIO
# ==============================================================

def stampa_persona(persona):
    print("Nome:", persona["nome"])
    print("Età:", persona["eta"])
    print("Città:", persona["citta"])

persona = {
    "nome": "Luca",
    "eta": 35,
    "citta": "Roma"
}

stampa_persona(persona)


# ==============================================================
# 11. FUNZIONE CHE MODIFICA UN DIZIONARIO
# ==============================================================

def aumenta_eta(persona):
    persona["eta"] += 1

aumenta_eta(persona)
print("Età dopo aumento:", persona["eta"])


# ==============================================================
# 12. SCOPE: VARIABILI LOCALI E GLOBALI
# ==============================================================

x = 10  # variabile globale

def modifica_x():
    global x
    x = x + 5

print("x prima:", x)
modifica_x()
print("x dopo:", x)


# ==============================================================
# 13. FUNZIONI CHE COLLABORANO (PROGRAMMA MODULARE)
# ==============================================================

def chiedi_numero():
    return int(input("Inserisci un numero: "))

def quadrato(n):
    return n * n

def programma():
    numero = chiedi_numero()
    risultato = quadrato(numero)
    print("Il quadrato è:", risultato)

# Decommenta per test interattivo
# programma()


# ==============================================================
# 14. FUNZIONE COME VALIDATORE
# ==============================================================

def input_valido(numero):
    return numero > 0

print("Input valido (5):", input_valido(5))
print("Input valido (-3):", input_valido(-3))


# ==============================================================
# 15. FUNZIONE COME RIUSO DI LOGICA
# ==============================================================

def area_rettangolo(base, altezza):
    return base * altezza

print("Area rettangolo:", area_rettangolo(4, 6))
