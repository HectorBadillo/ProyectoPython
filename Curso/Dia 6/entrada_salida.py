mi_archivo = open("prueba.txt")

print(mi_archivo.read())

mi_archivo.close()

print('-------------------------')

mi_archivo = open("prueba.txt")
una_linea = mi_archivo.readline()
print(una_linea)

mi_archivo.close()

print('-------------------------')

mi_archivo = open("prueba.txt")

una_linea = mi_archivo.readline()
print(una_linea.upper())

una_linea = mi_archivo.readline()
print(una_linea.rstrip())

una_linea = mi_archivo.readline()
print(una_linea)

mi_archivo.close()

print('-------------------------')

mi_archivo = open("prueba.txt")

for linea in mi_archivo:
    print("Aqui dice :" + linea)

mi_archivo.close()

print('-------------------------')

mi_archivo = open("prueba.txt")

todas = mi_archivo.readlines()

print(todas)

todas = todas.pop()
print(todas)

mi_archivo.close()

