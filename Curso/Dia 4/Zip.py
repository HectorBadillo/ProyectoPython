nombres = ['Ana', 'Hugo', 'Valeria']
edades  = [65, 29, 42]

combinados= list(zip(nombres,edades))
print(combinados)

nombres = ['Ana', 'Hugo', 'Valeria']
edades  = [65, 29, 42, 33]
ciudades = ['Lima', 'Madrid', 'Mexico']

combinados= list(zip(nombres,edades,ciudades))
print(combinados)

for nombres, edades, ciudades in combinados:
    print(f"{nombres} tiene {edades} años y vive en {ciudades}")