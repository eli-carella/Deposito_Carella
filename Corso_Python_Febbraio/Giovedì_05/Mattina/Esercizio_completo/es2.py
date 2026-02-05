'''
2.Intermedio/ Numeri primi in un intervallo :
Chiedi all'utente di inserire due numeri che definiscono un intervallo (es 10 e 50). Il programma dovrebbe stampare tutti i numeri primi compresi in quell'intervallo o i numeri non primi o entrambi divisi a tua scelta, salvandoli in due aggregazioni differenti e chiedere se deve ripetere
'''
while True:
    inizio = int(input("Inserisci il primo numero dell'intervallo: "))
    fine = int(input("Inserisci il secondo numero dell'intervallo: "))

    pari = []
    dispari = []

    for num in range(inizio, fine + 1):
        if num % 2 == 0:
            pari.append(num)
        else:
            dispari.append(num)

    print("\nNumeri pari nell'intervallo:")
    print(pari)

    print("\nNumeri dispari nell'intervallo:")
    print(dispari)

    ripeti = input("\nVuoi ripetere? (s/n): ").lower()
    if ripeti != "s":
        print("Programma terminato.")
        break
