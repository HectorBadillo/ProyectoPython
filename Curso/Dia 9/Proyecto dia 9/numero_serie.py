import os
from pathlib import Path
import re
import datetime
import time

ruta = Path('C:/Users/psbad/OneDrive/Documentos/Visual Studio Code/Proyecto Python/Curso/Dia 9/Proyecto_descomprimido/Mi_Gran_Directorio')
formato = r"N\D{3}-\d{5}"


def busqueda(ruta,formato):
    contador = 0
    for carpeta, subcarpeta, archivos in os.walk(ruta):
        for archivo in archivos:
            ruta_completa = Path(carpeta, archivo)
            with open(ruta_completa, 'r') as archivo_txt:
                contenido = archivo_txt.read()
                busqueda = re.findall(formato, contenido)
                if busqueda:
                    print(f"{ruta_completa.name}: \t\t{busqueda}")
                    contador += 1
    print(f"\nNúmeros encontrados: {contador}")

hoy = datetime.date.today()
print("-" * 45 + "\n")
print(f"Fecha de búsqueda: {hoy}\n")
print("ARCHIVO\t\t\tNUMERO DE SERIE")
print("-------\t\t\t---------------")
inicio = time.time()
busqueda(ruta,formato)
final = time.time()
print(f"\nDuracion de la busqueda: {final-inicio}\n")
print("-" * 45 + "\n")

