"""Crea una función llamada devolver_distintos() que reciba 3
integers como parámetros.
Si la suma de los 3 numeros es mayor a 15, va a devolver el
número mayor.
Si la suma de los 3 numeros es menor a 10, va a devolver el
número menor.
Si la suma de los 3 números es un valor entre 10 y 15
(incluidos) va a devolver el número de valorintermedio."""

def devolver_distintos(a,b,c):
    suma = a+b+c
    numeros = [a,b,c]
    numeros_odernados = sorted(numeros)

    if (suma > 15):
        return numeros_odernados[2]
    elif (suma < 10):
        return numeros_odernados[0]
    else:
        return numeros_odernados[1]
        

print(devolver_distintos(3,2,5))