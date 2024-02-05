import cv2
import face_recognition as fr
import os
import numpy
from datetime import datetime

# Crear base de datos
ruta = 'Empleados'
mis_imagenes = []
nombres_empleados = []
lista_empleados = os.listdir(ruta)

for nombre in lista_empleados:
    imagen_actual = cv2.imread(f'{ruta}/{nombre}')
    mis_imagenes.append(imagen_actual)
    nombres_empleados.append(os.path.splitext(nombre)[0])

print(nombres_empleados)

# Codificar imagenes
def codificar(imagenes):
    # Crear una lista nueva
    lista_codificada = []
    # Pasar todas las imagenes a RGB
    for img in imagenes:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # Codificar
        codificado = fr.face_encodings(img)[0]
        # Agregar a la lista
        lista_codificada.append(codificado)

    #Devolver lista codificada
    return lista_codificada

# Registrar los ingresos
def registrar_ingresos(persona):
    f = open('registro.csv', 'r+')
    lista_datos = f.readlines()
    nombres_registro = []
    for linea in lista_datos:
        ingreso = linea.split(',')
        nombres_registro.append(ingreso[0])
    if persona not in nombres_registro:
        ahora = datetime.now()
        string_ahora = ahora.strftime('%H:%M:%S')
        f.writelines(f'\n{persona}, {string_ahora}')

lista_empleados_codificada = codificar(mis_imagenes)

# Tomar una imagen de camara
captura = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Leer la imagen de la camara
exito, imagen = captura.read()

if not exito:
    print("No se ha podido tomar la captura")
else:
    # Reconocer cara en captura
    cara_captura = fr.face_locations(imagen)

    # Codificar cara
    cara_captura_codificada = fr.face_encodings(imagen, cara_captura)

    # Buscar coincidencias
    for cara_codi, cara_ubi in zip(cara_captura_codificada, cara_captura):
        coincidencias = fr.compare_faces(lista_empleados_codificada, cara_codi)
        distancias = fr.face_distance(lista_empleados_codificada, cara_codi)

        print(distancias)
        indice_coincidencia = numpy.argmin(distancias)

        # Mostrar coincidencia 
        if distancias[indice_coincidencia] > 0.6:
            print("No coincide con ninguno")
        else:
            # Buscar el nombre del empleado encontrado
            nombre = nombres_empleados[indice_coincidencia]

            y1, x2, y2, x1 = cara_ubi
            cv2.rectangle(imagen, (x1, y1), (x2,y2), (0,255,0), 2 )
            cv2.rectangle(imagen, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(imagen, nombre, (x1+ 6, y2 -6), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255),2)

            registrar_ingresos(nombre)

            # Mostar imagen
            cv2.imshow('Imagen web', imagen)

            # Mantener ventana
            cv2.waitKey(0)
