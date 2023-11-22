'''def suma():
    n1 = int(input("Numero 1:"))
    n2 = int(input("Numero 2:"))
    print(n1 + n2)
    print("Gracias por sumar" + n1)

try:
    suma()
except TypeError:
    print("Estas intentando concatenar tipos distintos")
except ValueError:
    print("Ese no es un numero")
else:
    print("Hiciste todo bien")
finally:
    print("Eso fue todo")
'''

'''try:
    #Codigo que queremos porbar

except:
    #Codigo a ejecutar si hay un error
else:
    #Codigo a ejecutar si no hay un error

finally:
    #Codigo que se va a ejecutar de todos modos'''

def pedir_numero():

    while True:
        try:
            numero = int(input("Dame un numero: "))
        except:
            print("Ese no es un numero")
        else:
            print(f"Ingresaste el numero {numero}")
            break
    print("Gracias")


pedir_numero()