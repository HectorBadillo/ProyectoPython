def burbuja(lista):
    n = len(lista)
    
    for i in range(n):
        # Últimos 'i' elementos ya están en su posición correcta
        for j in range(0, n-i-1):
            # Intercambia si el elemento encontrado es mayor que el siguiente elemento
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

arreglo_desordenado = [42, 17, 8, 33, 55, 20, 1, 99, 10, 5]
arreglo_ordenado = burbuja(arreglo_desordenado)
print(arreglo_ordenado)