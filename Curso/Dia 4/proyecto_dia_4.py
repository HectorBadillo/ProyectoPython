from random import *

print("ADIVINA EL NUMERO\n")
nombre = input("Nombre: ")
print("\nReglas del juego:\n")
print("1.El programa generara un numero del 0 al 100\n")
print("2.El usuario tendra 8 intentos para adivinar el numero\n")
print("3.El programa proporcionara pistas para que el usuario adivine el numero\n")
print("Intentos: ")

numero_secreto = randint(0,100)
numero_intentos =1

numero_ingresado = int(input(f"{numero_intentos}.-Digite un numero: "))
if numero_ingresado == numero_secreto:
    print(f"\nEl numero {numero_ingresado} era el numero secreto\nGANASTE {nombre.upper()}\nNumero de intentos: {numero_intentos}")
    exit
else:
    while numero_intentos <= 8:
        numero_intentos = numero_intentos + 1
        if((numero_ingresado < 0) or (numero_ingresado > 100)):
            print(f"{numero_intentos}.-El numero ingresado no es valido")
        elif(numero_ingresado < numero_secreto):
            print(f"{numero_intentos}.-El numero ingresado es menor al numero secreto")
        elif(numero_ingresado > numero_secreto):
            print(f"{numero_intentos}.-El numero ingresado es mayor al numero secreto")
        elif(numero_ingresado == numero_secreto):
            print(f"\nEl numero {numero_ingresado} era el numero secreto\nGANASTE {nombre.upper()}\nNumero de intentos: {numero_intentos-1}")
            break
        numero_ingresado = int(input("Digite un numero: "))
        if((numero_intentos == 8) and (numero_ingresado != numero_secreto)):
            print(f"\nNo lograste adivinar\nPERDISTE\nEl numero era: {numero_secreto}")