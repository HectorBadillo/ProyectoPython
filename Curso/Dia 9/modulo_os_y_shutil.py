import os
import shutil


'''print("-" * 50 + "\n")
print(os.getcwd())

print("-" * 50 + "\n")
archivo = open("dia_9.txt", "w")
archivo.write("texto de prueba de dia 9")
archivo.close()

print(os.listdir())'''

'''print("-" * 50 + "\n")
shutil.move("dia_9.txt", "C:\\Users\\psbad\\OneDrive\\Escritorio")
'''

import send2trash

'''send2trash.send2trash("dia_9.txt")
#Lo manda a la papelera'''

ruta = "C:\\Users\\psbad\\OneDrive\\Documentos\\Visual Studio Code\\Proyecto Python\\Curso\\Dia 8" 

for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f"En la carpeta: {carpeta}")
    print("Las subcarpetas son :")
    for sub in subcarpeta:
        print(f"\t{sub}")
    print("Los archivos son:")
    for arch in archivo:
        print(f"\t{arch}")
    print("\n")