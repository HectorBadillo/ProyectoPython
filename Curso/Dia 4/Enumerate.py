lista = ['a','b','c']
indice =0

for item in lista:
    print(indice,item)
    indice += 1

for item in enumerate(lista):
    print(item)

for indice,item in enumerate(lista):
    print(indice,item)

lista = ['a','b','c']
mis_tuples = list(enumerate(lista))
print(mis_tuples)
print((mis_tuples[1][0]))

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice,nombres in enumerate(lista_nombres):
    if(nombres.startswith('M')):
        print(indice)