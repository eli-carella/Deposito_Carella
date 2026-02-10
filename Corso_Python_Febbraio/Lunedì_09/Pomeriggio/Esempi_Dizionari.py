studente = {
"nome": "Alice",
"età": 20,
"sesso": "Femmina"
}

print(studente["nome"]) # Output: "Alice"
print(studente["età"]) # Output: 20

studente["età"] = 21
print(studente) # Output:{'nome': 'Alice', 'età': 21, 'sesso':'Femmina'}

studente["città"] = "Roma"
print(studente) # Output:{'nome': 'Alice','età': 21,'sesso':'Femmina', 'città': 'Roma'}

