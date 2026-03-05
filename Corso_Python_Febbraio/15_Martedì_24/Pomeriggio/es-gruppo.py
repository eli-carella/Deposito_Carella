import numpy as np
import os

def load_file(filename):
    if not os.path.exists(filename):
        print("File non trovato.")
        return None
    
    if filename.endswith(".csv"):
        data = np.loadtxt(filename, delimiter=",")
    elif filename.endswith(".txt"):
        data = np.loadtxt(filename)
    else:
        print("Formato non supportato.")
        return None
    
    return data

def save_results(results, output_name, file_type):
    with open(f"{output_name}.{file_type}", "w") as f:
        for key, value in results.items():
            f.write(f"{key}: {value}\n")

def analyze_1D(arr):
    results = {}

    print("\nAnalisi disponibili per array 1D:")
    print("1 - Statistiche di base")
    print("2 - Analisi posizionale")
    print("3 - Tutte")

    choice = input("Scelta: ")

    if choice in ["1", "3"]:
        results["min"] = np.min(arr)
        results["max"] = np.max(arr)
        results["media"] = np.mean(arr)
        results["deviazione_std"] = np.std(arr)

    if choice in ["2", "3"]:
        results["indice_min"] = np.argmin(arr)
        results["indice_max"] = np.argmax(arr)
        results["mediana"] = np.percentile(arr, 50)
        x = float(input("Valore per searchsorted: "))
        results["posizione_inserimento"] = np.searchsorted(np.sort(arr), x)

    return results

def analyze_2D(matrix):
    pass


while True:
    filename = input("\nInserisci nome file (.txt o .csv): ")
    data = load_file(filename)

    if data is None:
        continue

    print(f"Dimensione dati: {data.ndim}D")

    if data.ndim == 1:
        results = analyze_1D(data)
    else:
        results = analyze_2D(data)

    print("\nRisultati:")
    for k, v in results.items():
        print(k, ":\n", v)

    output_name = input("\nNome file output (senza estensione): ")
    file_type = input("Formato output (txt/csv): ")

    if file_type not in ["txt", "csv"]:
        file_type = "txt"

    save_results(results, output_name, file_type)

    repeat = input("\nVuoi eseguire un'altra analisi? (s/n): ")
    if repeat.lower() != "s":
        break

