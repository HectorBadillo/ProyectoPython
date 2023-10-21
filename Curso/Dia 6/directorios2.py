from pathlib import Path
#Para cualquier sistema operativo
carpeta = Path("/Users/psbad/OneDrive/Documentos/Visual Studio Code/Proyecto Python/Curso/Dia 1")
archivo = carpeta / "Prueba_Dia_6.txt"

mi_archivo = open(archivo)
print(mi_archivo.read())