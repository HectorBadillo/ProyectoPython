def agregar_diccionarios(diccionario_objetivo, *diccionarios_a_agregar):
    for diccionario in diccionarios_a_agregar:
        print(f'Agregado: {diccionario['nombre']}')
        diccionario_objetivo[f'{diccionario['nombre']}']= diccionario

mi_dict = {}
producto1 = {'nombre': 'Leche', 'marca': 'Alpura', 'Categoria': 'Lacteos', 'Precio': 10.50}
producto2 = {'nombre': 'Fanta', 'marca': 'CocaCola', 'Categoria': 'Sodas', 'Precio': 19.50}
producto3 = {'nombre': 'Doritos', 'marca': 'Sabritas', 'Categoria': 'Papas', 'Precio': 15}

# Llamamos a la función agregar_diccionarios para agregar producto1, producto2 y producto3 a mi_dict
agregar_diccionarios(mi_dict, producto1, producto2, producto3)

# Imprimimos mi_dict
print(mi_dict)

for elemento in mi_dict:
    print(elemento)