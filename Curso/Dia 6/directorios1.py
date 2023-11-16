import os

ruta = os.getcwd()
print(ruta)
print("_______________________________________________\n")

ruta = os.chdir('C:\\Users\\psbad\\OneDrive\\Documentos\\Visual Studio Code\\Proyecto Python\\Curso\\Dia 1')
archivo = open("Prueba_Dia_6.txt")
print(archivo.read())
print("________________________________________________\n")
"""#Crea una nueva carpeta
ruta = os.makedirs("C:\\Users\\psbad\\OneDrive\\Documentos\\Visual Studio Code\\Proyecto Python\\Curso\\Dia 1\\Prueba")
"""

ruta = "C:\\Users\\psbad\\OneDrive\\Documentos\\Visual Studio Code\\Proyecto Python\\Curso\\Dia 6\\prueba.txt"

elemento = os.path.basename(ruta)
print(elemento)
elemento = os.path.dirname(ruta)
print(elemento)
elemento = os.path.split(ruta)
print(elemento)

"""Eliminar carpeta
os.rmdir('C:\\Users\\psbad\\OneDrive\\Documentos\\Visual Studio Code\\Proyecto Python\\Curso\\Dia 1\\Prueba')
"""

print("_______________________________________________\n")
otro_archivo = open("C:\\Users\\psbad\\OneDrive\\Documentos\\Visual Studio Code\\Proyecto Python\\Curso\\Dia 1\\Prueba_Dia_6.txt")
print(otro_archivo.read())
print("_______________________________________________\n")

elemento = os.path.basename(ruta)
print(elemento)
elemento = os.path.dirname(ruta)
print(elemento)
elemento = os.path.split(ruta)
print(elemento)

