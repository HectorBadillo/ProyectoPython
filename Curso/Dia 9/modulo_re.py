'''
\d digito numerico
\w alfanumerico
\s espacio en blanco

\D no digito
\W No alfanumerico
\S No espacio en blanco

+ 1 o mas veces
{n} se repite n veces
{n,m} se repite de n a m veces
{n,} se repite desde n hacia arriba
* 0 o mas
? 1 o 0 veces
'''

texto = "Si necesitas ayuda llama al (658)-598-997 las 24 horas al servicio de ayuda online"

palabra = 'ayuda' in texto
print(palabra)
print("-" * 50 + "\n")

import re

patron = 'ayuda'
busqueda = re.search(patron,  texto)
print(busqueda)
print("-" * 50 + "\n")

busqueda = re.findall(patron,  texto)
print(busqueda)
for hallazgo in re.finditer(patron,texto):
    print(hallazgo.span())
print("-" * 50 + "\n")


texto = "Llama al 564-525-6588 ya mismo"
#patron = r"\d\d\d-\d\d\d-\d\d\d\d"
patron = r"\d{3}-\d{3}-\d{4}"
resultado = re.search(patron, texto)
print(resultado)
print(resultado.group())
print("-" * 50 + "\n")

patron = re.compile(r"(\d{3})-(\d{3})-(\d{4})")
resultado = re.search(patron, texto)
print(resultado)
print(resultado.group(1))
print(resultado.group(2))
print("-" * 50 + "\n")


'''clave = input("Clave: ")
patron =  r"\D{1}\w{7}"
chequear = re.search(patron, clave)
print(chequear)
print("-" * 50 + "\n")'''

texto = "No atendemos los lunes por la tarde"
buscar = re.search(r"lunes|martes",texto)
print(buscar)

buscar = re.search(r"...demos....",texto)
print(buscar)

buscar = re.search(r"^\D",texto) #Comienzo
print(buscar)

buscar = re.search(r"\D$",texto) #Final
print(buscar)

buscar = re.findall(r"[^\s]+",texto) #Excluir
print(buscar)
print("-" * 50 )
print("-" * 50 + "\n")


def verificar_email(email):
    patron = r'\w{1,}@\w+\.com'
    verificar = re.search(patron,email)
    if verificar:
        print("Ok")
    else:
        print("La dirección de email es incorrecta")

verificar_email("chelito@gmail.com")

def verificar_saludo(frase):
    patron = r'^Hola'
    verificar = re.search(patron,frase)
    if verificar:
        print("Ok")
    else:
        print("No has saludado")