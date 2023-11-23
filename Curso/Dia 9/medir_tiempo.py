


def prueba_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista


def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista

print(prueba_while(20))
print(prueba_for(20))
print("-" * 50 + "\n")

import time

inicio = time.time()
prueba_while(20000000)
final = time.time()
print(f"While: {final - inicio}")

inicio = time.time()
prueba_for(20000000)
final = time.time()
print(f"For: {final - inicio}")
print("-" * 50)
print("-" * 50 + "\n")

import timeit

declaracion2 = '''
prueba_while(10)
'''
mi_setup2 ='''
def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista
'''
duracion_while = timeit.timeit(declaracion2, mi_setup2, number= 10000000)
print(f"While: {duracion_while}")

declaracion = '''
prueba_for(10)
'''
mi_setup = '''
def prueba_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista
'''
duracion_for = timeit.timeit(declaracion, mi_setup, number=10000000)
print(f"For: {duracion_for}")


