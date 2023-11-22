import pandas as pd

class Persona:
    def __init__(self, nombre: str, apellido: str) -> None:
        self.nombre = nombre
        self.apellido = apellido

# Leer el DataFrame desde el archivo CSV
df = pd.read_csv("C:\\Users\\psbad\\OneDrive\\Documentos\\Visual Studio Code\\Proyecto Python\\Pandas\\prueba.csv")

# Crear una lista de objetos Persona a partir de las filas del DataFrame
personas_lista = []
for index, row in df.iterrows():
    persona = Persona(row['Nombre'], row['Apellido'])
    personas_lista.append(persona)

# Crear un diccionario de objetos Persona a partir de las filas del DataFrame
personas_diccionario = {}
for index, row in df.iterrows():
    persona = Persona(row['Nombre'], row['Apellido'])
    personas_diccionario[index] = persona

# Mostrar la lista de personas
for persona in personas_lista:
    print(f"Nombre: {persona.nombre}, Apellido: {persona.apellido}")

# Mostrar el diccionario de personas
for key, persona in personas_diccionario.items():
    print(f"ID: {key}, Nombre: {persona.nombre}, Apellido: {persona.apellido}")
