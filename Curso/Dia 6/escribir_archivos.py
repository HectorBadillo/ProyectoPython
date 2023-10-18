archivo = open("prueba1.txt", 'w')#El 'w' sobre escribe el archivo

archivo.write('''Soy el nuevo texto
y  esto es un salto
de linea
''')
archivo.write('_________________________\n')

archivo.writelines(['Hola','Mundo','Aqui','Estoy\n'])

archivo.write('_________________________\n')

lista = ['Hola','Mundo','Aqui','Estoy']
for palabra in lista:
    archivo.write(palabra + '\n')

archivo.close()

archivo = open("prueba1.txt",'a')#El 'a' añade al final de archivo

archivo.write('___________________\n')
archivo.write('Bienvenido')

archivo.close()