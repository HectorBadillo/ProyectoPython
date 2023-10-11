x = 5==2

if (x):
    print('Es correcto')
else:
    print("Es incorrecto")

mascota = "conejo"
if (mascota == 'gato'):
    print("Tienes un gato")
elif mascota=="perro":
    print("Tienes un perro")
elif mascota=='pez':
    print("Tienes un pez")
else:
    print("No se que animal tienes")

edad=16
calificacion = 9

if (edad<18):
    print("Eres menor de edad")
    if (calificacion>=7):
        print("Aprobado")
    else:
        print("No aprobado")
else:
    print("Eres adulto")