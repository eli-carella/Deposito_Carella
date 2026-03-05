import requests

def ottieni_coordinate(citta):
    """
    Riceve il nome di una città e restituisce una tupla (latitudine, longitudine).
    In caso di errore o città non trovata, restituisce (None, None).
    """

    url = f"https://geocoding-api.open-meteo.com/v1/search?name={citta}&count=1&language=it&format=json"

    try:
        response = requests.get(url)

        data = response.json()
        if "results" in data and len(data["results"]) > 0:
            lat = data["results"][0]["latitude"]
            lon = data["results"][0]["longitude"]
            return lat, lon
        else:
            print(f"Città '{citta}' non trovata.")
            return None, None

    except Exception as e:
        print(f"Errore durante la ricerca: {e}")
        return None, None

def ottieni_dati(lat, lon, giorni,scelta):
    url = (f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m,wind_speed_10m,precipitation&forecast_days={giorni}")
    # url = (f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily={parametri_daily}&timezone=auto&forecast_days={giorni}")
    
    response = requests.get(url)
    data = response.json()
    print(data)
    previsioni = data["hourly"]

    for i in range(len(previsioni["time"])):
        if scelta == "1": # solo temperatura
            print(f"giorno {previsioni["time"][i]} temperatura:{previsioni["temperature_2m"][i]}")
        elif scelta == "2": # temp e vento
            print(f"giorno {previsioni["time"][i]} temperatura:{previsioni["temperature_2m"][i]} velocità del vento:{previsioni["wind_speed_10m"][i]}")
        elif scelta == "3": # temp e precipitaz
            print(f"giorno {previsioni["time"][i]} temperatura:{previsioni["temperature_2m"][i]} precipitazioni: {previsioni["precipitation"][i]}")
        else: # tutto
            print(f"giorno {previsioni["time"][i]} temperatura:{previsioni["temperature_2m"][i]} velocità del vento:{previsioni["wind_speed_10m"][i]} precipitazioni: {previsioni["precipitation"][i]}")

    


while True:

    nome_citta = input("Inserisci il nome della città: ")
    lat, lon = ottieni_coordinate(nome_citta)
    if not lat or not lon:
        continue
    giorni = input("Per quanti giorni vuoi visualizzare le previsioni? 1, 3 o 7? ")
    if giorni not in ["1","3","7"]:
        print("Errore")
    else:
        giorni = int(giorni)
        scelta = input("Cosa vuoi visualizzare?\n1) Solo temperatura\n2) Temperatura e velocità del vento\n3) Temperatura e possibili precipitazioni\n4) Tutte le informazioni\n")
        if scelta not in ["1","2","3","4"]:
            print("Scelta selezionata non valida")
            continue
        else:
            print(f"Coordinate di {nome_citta}:")
            print(f"Latitudine: {lat}")
            print(f"Longitudine: {lon}")
            ottieni_dati(lat,lon,giorni,scelta)
    
    w
    continuare = input("Vuoi continuare? (si/no)")
    if continuare == "no":
        break