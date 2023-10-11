def prueba(num1 , num2 , *args , **kwargs):

    print(f"El primer valor es {num1}")
    print(f"El segundo valor es {num2}")

    for argumento in args:
        print(f"argumento = {argumento}")


    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")

args = [100,200,300,400]
kwargs= {'x':'uno','y':'dos','z':'tres'}

prueba(15,50,100,200,300,400,x='uno',y='dos',z='tres')

prueba(14,59,*args,**kwargs)

def describir_persona(nombre,**kwargs):
    print(f"Características de {nombre}")
    for nombre_argumento,valor_argumento in kwargs.items():
        print(f"{nombre_argumento}: {valor_argumento}")

describir_persona("María", color_ojos="azules", color_pelo="rubio")