print("\tANALIZADOR DE TEXTO")
texto = input("Ingresa un texto: ")
texto = texto.upper()
letras = []
letras.append(input("Ingresa la primera letra: ").upper())
letras.append(input("Ingresa la segunda letra: ").upper())
letras.append(input("Ingresa la tercera letra: ").upper())

"Parte 1: Cuantas veces aparecieron las letras ingresadas."
print("\nCUANTAS VECES SE REPITEN LAS LETRAS")
conteol1= texto.count(letras[0])
conteol2= texto.count(letras[1])
conteol3= texto.count(letras[2])
print("La letra '{}' se repite: {}".format(letras[0],conteol1))
print("La letra '{}' se repite: {}".format(letras[1],conteol2))
print("La letra '{}' se repite: {}".format(letras[2],conteol3))

"Parte 2: Decirle al usuario cuantas palabras hay"
print("\nCUANTAS PALABRAS TIENE EL TEXTO")
numero_palabras= texto.split()
print("El numero de palabras en tu texto es: {}".format(len(numero_palabras)))

"Parte 3: Decir cual es la primera letra del texto y la ultima"
print("\nPRIMERA Y ULTIMA LETRA DEL TEXTO")
print("La primera letra del texto es: '{}'".format(texto[0]))
print("La ultima letra del texto es: '{}'".format(texto[-1]))

"Parte 4: Mostrar el texto con el orden de las palabras invertidos"
numero_palabras.reverse()
texto_inverso = " ".join(numero_palabras)
print("\nEl texto con el orden de las palabras invertido es: " + texto_inverso.lower())

"Parte 5: Mostrar si la palabra Python aparece en el texto"
conteo= 'PYTHON' in texto
conteo = str(conteo)
evaluacion = {'True':'La palabra Pyton si aparece en el texto.', 'False':'La palabra Python no aparece en el texto'}
print("\n" + evaluacion[conteo])