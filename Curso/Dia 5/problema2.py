"""Escribe una función (puedes ponerle cualquier nombre que
quieras) que reciba cualquier palabra como parámetro, y que
devuelva todas sus letras únicas (sin repetir) pero en orden
alfabético.
Por ejemplo si al invocar esta función pasamos la palabra
"entretenido"
, debería devolver ['d','e','i','n','o','r','t']"""

def orden_alfabetico(palabra):
    lista = list(palabra.lower())
    lista_sin_repetidos = set(lista)
    lista_ordenada = sorted(lista_sin_repetidos)
    return lista_ordenada

prueba = str(input("Escribe una palabra: "))
ordenada = orden_alfabetico(prueba)
print(ordenada)