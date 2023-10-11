"""Escribe una función que requiera una cantidad indefinida de
argumentos. Lo que hará esta función es devolver True si en
algún momento se ha ingresado al numero cero repetido dos
veces consecutivas.
Por ejemplo:
(5,6,1,0,0,9,3,5) >>> True
(6,0,5,1,0,3,0,1) >>> False"""

def cero_consecutivo(*args):
    lista = list(args)
    for i,numero in enumerate(lista):
        if numero == 0:
            if i < len(lista) - 1:
                if lista[i+1] == 0:
                    return True
    return False


print(cero_consecutivo(5,6,1,0,4,0,0,40,9))