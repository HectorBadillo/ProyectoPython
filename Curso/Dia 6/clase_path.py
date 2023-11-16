from pathlib import Path

guia = Path("Barcelona", "Sagrada_Familia")
print(guia)

print("___________________________________\n")
base = Path.home()
print(base)

print("___________________________________\n")
guia = Path(base,"Europa","España", Path("Barcelona", "Sagrada_Familia.txt"))
guia2 = guia.with_name("La_Pedrera.txt")
print(guia)
print(guia2)

print("___________________________________\n")
guia = Path(base,"Europa","España", Path("Barcelona", "Sagrada_Familia.txt"))
print(guia.parent)
print(guia.parent.parent)

print("___________________________________\n")
"""guia = Path(Path.home(), "AppData") Todos los txt en AppData
for txt in Path(guia).glob("**/*.txt"):
    print(txt)"""

guia = Path("Europa","España","Barcelona","Sagrada_Familia.txt")
en_europa = guia.relative_to(Path("Europa"))
en_espana = guia.relative_to(Path("Europa","España","Barcelona"))
print(en_europa)
print(en_espana)

ruta = Path('C:/Users/Usuario/Desktop/Curso Python') / 'Cuestionario Día 6' / 'Pregunta 1'
carpeta = ruta.parents[3]
print(carpeta)