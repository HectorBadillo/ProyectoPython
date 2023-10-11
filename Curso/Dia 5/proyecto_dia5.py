#Hacer el juego del ahorcado

from random import *

def palabra_secreta():
    palabras = [
    "Computadora",
    "Elefante",
    "Dinosaurio",
    "Universidad",
    "Estudiante",
    "Guitarra",
    "Biblioteca",
    "Tortuga",
    "Helicoptero",
    "Astronomia",
    "Abecedario",
    "Camioneta",
    "Pintura",
    "Jirafa",
    "Refrigerador",
    "Cocodrilo",
    "Chocolate",
    "Triciclo",
    "Montaña",
    "Robot"
            ]
    palabra = choice(palabras)
    #print(palabra)
    return palabra.lower()

def letras_palabra(palabra):
    lista = list(palabra.lower())
    lista_sin_repetidos = set(lista)
    letras = sorted(lista_sin_repetidos)
    return letras

def casillas(palabra):
    intento = []
    for letra in palabra:
        intento.append('_')
    print(intento)
    return intento

def validacion_letra(letras,palabra,intento,lista):
    j=0
    nueva_lista=[]
    if intento in letras:
        for i in lista:
            if palabra[j] == intento:
                nueva_lista.append(intento)
            else:
                nueva_lista.append(lista[j])
            j += 1
        return nueva_lista
    else:
        return lista
    
def validacion_frase(letras,intento):
    for letra in intento:
        if letra not in letras:
            return False
    return True


    


print("\n\tJUEGO DEL AHORCADO\n")
print("Instrucciones:")
print("*Tienes 7 intentos para adivinar la palabra secreta")
print("*Puedes ingresar una o mas letras")
print("*Ingresar mas de una letra cobrara 2 intentos\n")

palabra = palabra_secreta()
letras = letras_palabra(palabra)
lista = casillas(palabra)

estado = False
i = 0
while (i<7 and estado == False):
    print(f"Intento {i+1}")
    intento = input("Ingrese un intento: ")
    if len(intento) == 1:
        lista = validacion_letra(letras,palabra,intento,lista)
        print(lista)
        print('\n')
    else:
        i += 1
        if validacion_frase(letras,intento) == True:
            j=0
            for k in range(len(intento)):
                lista = validacion_letra(letras,palabra,intento[j],lista)
                j += 1
            print(lista)
            print('\n')
        else:
            continue
    if lista == list(palabra):
        estado = True
    i += 1
if estado == True:
    print('FELICIDADES HAS GANADO')
else:
    print('LO LAMENTO HAS PERDIDO')
    print(f"La palabra secreta era: {palabra}")