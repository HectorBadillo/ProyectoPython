"""
    De una pagina de venta de libros
    con mas de 1000 titulos,
    se va a extraer el titulo de todos 
    los libros con 4 o mas estrellas
"""

import bs4
import requests

# Crear una url sin numero de pagina
url = 'http://books.toscrape.com/catalogue/page-{}.html'

# Lista de titulos con 4 o 5 estrellas
titulos = []

# Iterar paginas
for pagina in range(1,51):

    # Crear sopa en cada pagina
    url_pagina = url.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

    # Seleccion datos de los libros
    libros = sopa.select('.product_pod')

    # Iterar libros
    for libro in libros:

        # Validar 4 o 5 estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:

            # Guardar titulo
            titulo_libro = libro.select('a')[1]['title']

            # Agregar libro a la lista
            titulos.append(titulo_libro)

# Ver los titulos
for t in titulos:
    print(t)

