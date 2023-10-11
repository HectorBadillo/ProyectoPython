serie = 'N-021'

match serie:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case _:
        print("No existe este producto")

cliente = {'nombre': 'Federico',
            'edad':45,
            'ocupacion':'instructor'}

pelicula = {'Titulo':'Matrix', 
            'ficha_tecnica':{'protagonista':'Keanu Reeves', 
                             'Director':'Lana y Lilly'}}

elementos = [cliente, pelicula, 'libro']

for e in elementos:
    match e:
        case {'nombre':nombre,
              'edad':edad,
              'ocupacion':ocupacion}:
            print("Es un cliente")
            print(nombre, edad, ocupacion)
        
        case {'Titulo':titulo,
              'ficha_tecnica':{'protagonista':protagonista,
                               'Director': director}}:
            print("Es una pelicula")
            print(titulo, protagonista, director)
        
        case _:
            print("No se que es esto")