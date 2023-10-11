def multiplicar(numero1 , numero2):
    return numero1 * numero2

resultado = multiplicar(75,43)
print(resultado)

def invertir_palabra(palabra):
    palabra_invertida = palabra[::-1]
    return palabra_invertida.upper()
    
palabra=invertir_palabra("Curso")
print(palabra)