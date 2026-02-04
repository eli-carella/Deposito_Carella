## Esercizio 2
# scrivi un programma che chieda all'utente di inserire due numeri e un'operazione da eseguire 
# tra addizione, sottrazione, moltiplicazione, e divisione.
# Il programma dovrebbe poi eseguire l'operazione e stampare il risultato. 
# Tuttavia, se l'utente tenta di dividere per zero il programma
# dobrebbe stampare "Errore: divisione per zero"
# Se l'operezione inserita non è riconosciuta dovrebbe stampare "operazione non valida"

num1 = float(input("Inserisci il primo numero: "))
num2 = float(input("Inserisci il secondo numero: "))
operazione = input("Inserisci l'operazione (+, -, *, /): ")

match operazione:
    case "+":
        print("Risultato:", num1 + num2)
    case "-":
        print("Risultato:", num1 - num2)
    case "*":
        print("Risultato:", num1 * num2)
    case "/":
        if num2 == 0:
            print("Errore: Divisione per zero")
        else:
            print("Risultato:", num1 / num2)
    case _:
        print("Operazione non valida")