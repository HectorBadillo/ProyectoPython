mi_lista = ['a','b','c']
print(type(mi_lista))

resultado = len(mi_lista)
print(resultado)

extraer = mi_lista[0:2]
print(extraer)

mi_lista2 = ['d','e','f']
print(mi_lista + mi_lista2)

mi_lista3 = mi_lista + mi_lista2
mi_lista3[0]='alfa'
print(mi_lista3)

mi_lista3.append('g')
print((mi_lista3))

eliminado = mi_lista3.pop(3)
print(mi_lista3)
print(eliminado)

lista = ['g','o','b','m','c']
print(lista)
lista.sort()
print(lista)

lista.reverse()
print(lista)