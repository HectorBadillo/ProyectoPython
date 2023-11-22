

'''def mayuscula(texto:str):
    print(texto.upper())


def minuscula(texto:str):
    print(texto.lower())

def una_funcion(funcion):
    return funcion

una_funcion(mayuscula("Probando"))'''

'''def cambiar_letras(tipo):

    def minuscula(texto:str):
        print(texto.lower())

    def mayuscula(texto:str):
        print(texto.upper())
    
    if tipo == 'may':
        return mayuscula
    elif tipo == 'min':
        return minuscula
    
operacion = cambiar_letras('may')
operacion('palabra')'''

def decorar_saludo(funcion):
    def otra_funcion(palabra):
        print("Hola")
        funcion(palabra)
        print("Adios")
    return otra_funcion


def mayusculas(texto):
    print(texto.upper())

@decorar_saludo
def minusculas(texto):
    print(texto.lower())


minusculas("fede")
print("-" * 50)

mayusculas("FEDE")
print("-" * 50)

mayusculas_decorada = decorar_saludo(mayusculas)
mayusculas_decorada("fede")


