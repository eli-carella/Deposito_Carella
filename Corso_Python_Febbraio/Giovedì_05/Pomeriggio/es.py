while True:
    #1. inserisci intero positivo n
    n = int(input("Inserisci un numero intero positivo n: "))
    
    if n <= 0:
        print("Il numero deve essere positivo. Riprova.")
        continue
    else:
        #2. Inserimento valori lista
        lista_numeri = []
        for i in range(n):
            valore = int(input(f"Inserisci il valore {i+1} di {n}: "))
            lista_numeri.append(valore)
        
        print(f"\nLista generata: {lista_numeri}")

        #3. Somma dei numeri pari
        somma_pari = 0
        for num in lista_numeri:
            if num % 2 == 0:
                somma_pari += num
        print(f"Somma dei numeri pari nella lista: {somma_pari}")

        #4. Stampa numeri dispari
        print("Numeri dispari nella lista: ", end="")
        for num in lista_numeri:
            if num % 2 != 0:
                print(num, end=" ")

        #5-6: Stampa numeri primi della lista
        print("Numeri primi: ", end="")
        for num in lista_numeri:
            if num < 2:
                continue
            
            primo = True
            for i in range(2, num):
                if num % i == 0:
                    primo = False
                    break
            
            if primo:
                print(num, end=" ")
        print()

        #7. Verifica se la somma totale è un numero primo
        somma_totale = 0
        for num in lista_numeri:
            somma_totale += num
        
        somma_is_primo = True
        if somma_totale < 2:
            somma_is_primo = False
        else:
            for i in range(2, somma_totale):
                if somma_totale % i == 0:
                    somma_is_primo = False
                    break
        
        print(f"Somma totale ({somma_totale}): ", end="")
        if somma_is_primo:
            print("è un numero primo.")
        else:
            print("non è un numero primo.")

        break