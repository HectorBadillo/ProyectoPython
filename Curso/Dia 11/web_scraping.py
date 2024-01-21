import bs4
import requests

"""resultado = requests.get("https://escueladirecta-blog.blogspot.com/2021/10/encapsulamiento-pilares-de-la.html")

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')"""

"""parrafo_especial = sopa.select('p')[3].getText()
print(parrafo_especial)"""

"""columna_lateral = sopa.select('.snippet-item.r-snippetized')
for p in columna_lateral:
    print(p.getText())
    print("\n")"""

"""nuevo_sitio_web = requests.get("https://www.escueladirecta.com/courses/")
nueva_sopa = bs4.BeautifulSoup(nuevo_sitio_web.text, 'lxml')

imagenes = nueva_sopa.select('.course-box-image')[0]['src']
print(imagenes)

imagen_curso = requests.get(imagenes)
f = open('mi_imagen.jpg', 'wb')
f.write(imagen_curso.content)
f.close()"""
