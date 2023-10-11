texto = "Este es el texto de Federico"
resultado = texto.upper()
print(resultado)

texto = "Este es el texto de Federico"
resultado = texto.lower()
print(resultado)

texto = "Este es el texto de Federico"
resultado = texto.split()
print(resultado)

texto = "Este es el texto de Federico"
resultado = texto.split("t")
print(resultado)


a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = "-".join([a,b,c,d])
print(e)

texto = "Este es el texto de Federico"
resultado = texto.find("e")
print(resultado)

texto = "Este es el texto de Federico"
resultado = texto.replace("Federico","Hector")
print(resultado)

texto = "Este es el texto de Federico"
resultado = texto.replace("e","x")
print(resultado)