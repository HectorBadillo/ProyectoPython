#librerias
#Se importa uno a uno: from random import randint
#Asi se importa toda la libreria:
from random import *

aleatorio = randint(1,50)
print(aleatorio)
print("_____________________________")
aleatorio = round(uniform(1,5),1)
print(aleatorio)

aleatorio = random() #va entre 0-1 en punto decimal
print(aleatorio)

colores = ['azul', 'rojo', 'verde', 'amarillo']
aleatorio = choice(colores)
print(aleatorio)

numeros = list(range(5,50,5))
print(numeros)
shuffle(numeros)
print(numeros)