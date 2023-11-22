import pandas as pd

class Persona:
    def __init__(self, nombre: str, apellido: str) -> None:
        self.nombre = nombre
        self.apellido = apellido

# Crear 5 instancias de la clase Persona
persona1 = Persona("Juan", "Pérez")
persona2 = Persona("María", "Gómez")
persona3 = Persona("Carlos", "López")
persona4 = Persona("Ana", "Martínez")
persona5 = Persona("Pedro", "Rodríguez")

# Crear un DataFrame con la información de las personas
data = {'Nombre': [persona1.nombre, persona2.nombre, persona3.nombre, persona4.nombre, persona5.nombre],
        'Apellido': [persona1.apellido, persona2.apellido, persona3.apellido, persona4.apellido, persona5.apellido]}

df = pd.DataFrame(data)

# Guardar el DataFrame en un archivo CSV
df.to_csv("C:\\Users\\psbad\\OneDrive\\Documentos\\Visual Studio Code\\Proyecto Python\\Pandas\\prueba.csv", index= False)

print("Datos guardados en prueba.csv")

# Crear una nueva persona
nueva_persona = Persona("Laura", "García")

# Agregar la nueva persona al DataFrame
nueva_fila = pd.DataFrame({'Nombre': [nueva_persona.nombre], 'Apellido': [nueva_persona.apellido]})
df = pd.concat([df, nueva_fila], ignore_index=True)

# Guardar el DataFrame actualizado en el mismo archivo CSV
df.to_csv("C:\\Users\\psbad\\OneDrive\\Documentos\\Visual Studio Code\\Proyecto Python\\Pandas\\prueba.csv", index=False)

print("Nueva persona agregada y datos actualizados en prueba.csv")