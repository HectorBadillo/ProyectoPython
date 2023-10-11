def quickshort(lista):
    #Caso base para detener la recursividad
    if len(lista) <= 1:
        return lista
    
    #Se obtiene un pivote (puede ser aleatorio)
    pivote = lista[ len(lista)//2 ]

    #Se separa y aplica el metodo
    izquierda = [x for x in lista if x < pivote]
    centro = [x for x in lista if x == pivote]
    derecha = [x for x in lista if x > pivote]
    return quickshort(izquierda) + centro + quickshort(derecha)

arreglo_desordenado = [42, 17, 8, 33, 55, 20, 1, 99, 10, 5]
arreglo_ordenado = quickshort(arreglo_desordenado)
print(arreglo_ordenado)

