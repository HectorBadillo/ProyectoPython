from pathlib import Path, PureWindowsPath
#Para cualquier sistema operativo
carpeta = Path("C:/Users/psbad/OneDrive/Documentos/Visual Studio Code/Proyecto Python/Curso/Dia 1/Prueba_Dia_6.txt")

print(carpeta.read_text())
print("____________________________________\n")

print(carpeta.name)
print("____________________________________\n")

print(carpeta.suffix)
print("____________________________________\n")

print(carpeta.stem)
print("____________________________________\n")

if not carpeta.exists():
    print("Este archivo no existe")
else:
    print("Genial, existe")
print("____________________________________\n")

ruta_windows = PureWindowsPath(carpeta)
print(ruta_windows)