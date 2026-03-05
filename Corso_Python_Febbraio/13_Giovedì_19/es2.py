'''
Create un programma python utilizzando le api
https://pokeapi.co/api/v2/pokemon/ {numero} che simula un
pokedex, quando troverete un pokemon in maniera randomica
verificherà se è presente nel vostro pokedex (pokedex.json), in caso non fosse presente vi permetterà di catturarlo salvando le caratteristiche.
(Sul sistema API sono presenti poco più di 1000 pokemon)
'''
import requests
import random
import json
import os

# Crea il pokedex se non esiste
if not os.path.exists("pokedex.json"):
    with open("pokedex.json", "w") as file:
        json.dump([], file)

while True:

    scelta_inizio = input("\nVuoi cercare un Pokémon? (s/n): ")

    if scelta_inizio.lower() == "n":
        print("Arrivederci Allenatore!")
        break

    # Carica pokedex
    with open("pokedex.json", "r") as file:
        pokedex = json.load(file)

    # Genera numero casuale
    numero = random.randint(1, 1025)

    url = f"https://pokeapi.co/api/v2/pokemon/{numero}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon = response.json()

        nome = pokemon["name"]
        altezza = pokemon["height"]
        peso = pokemon["weight"]

        print("\nHai trovato un Pokémon!")
        print("Nome:", nome)
        print("Altezza:", altezza)
        print("Peso:", peso)

        # Controllo se già presente
        presente = False
        for p in pokedex:
            if p["name"] == nome:
                presente = True
                break

        if presente:
            print("Questo Pokémon è già nel tuo Pokédex!")
        else:
            scelta = input("Vuoi catturarlo? (s/n): ")

            if scelta.lower() == "s":
                nuovo_pokemon = {
                    "name": nome,
                    "height": altezza,
                    "weight": peso
                }

                pokedex.append(nuovo_pokemon)

                with open("pokedex.json", "w") as file:
                    json.dump(pokedex, file, indent=4)

                print("Pokémon catturato!")
            else:
                print("Pokémon non catturato.")
    else:
        print("Errore nella richiesta API.")