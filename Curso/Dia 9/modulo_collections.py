from collections import Counter

print("-" * 50 + "\n")
numeros = [2,3,4,6,5,4,3,5,7,1,2,4,6,9,7,5,4,2,5]
print(Counter(numeros))
print("-" * 50 + "\n")

print(Counter("mississippi"))
print("-" * 50 + "\n")

frase = "al pan pan y al vino vino"
print(frase.split())
print("-" * 50 + "\n")

serie =  Counter([2,3,4,6,5,4,3,5,7,1,2,4,6,9,7,5,4,2,5])
print(serie.most_common(2))
print("-" * 50 + "\n")

print(list(serie))
print("-" * 50)
print("-" * 50 + "\n")


from collections import defaultdict

mi_dict = defaultdict(lambda: "nada")
mi_dict["uno"] = "verde"
print(mi_dict["dos"])
print(mi_dict)

print("-" * 50 )
print("-" * 50 + "\n")

from collections import namedtuple

Persona = namedtuple('Persona', ["Nombre", "Altura", "Peso"])

ariel = Persona("Ariel",1.76,79)

print(ariel.Nombre)
print(ariel[2])
print("-" * 50 )
print("-" * 50 + "\n")

from collections import deque

# Lista inicial
lista_ciudades = ["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"]

# Crear una deque a partir de la lista
deque_ciudades = deque(lista_ciudades)

# Imprimir la deque
print("Deque inicial:", deque_ciudades)

# Agregar elementos por la izquierda
deque_ciudades.appendleft("Barcelona")
deque_ciudades.appendleft("Ámsterdam")

# Imprimir la deque después de agregar elementos por la izquierda
print("Deque después de agregar por la izquierda:", deque_ciudades)
