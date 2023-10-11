"No hay repeticiones,no puedes poner listas ni diccionarios"
mi_set = set([1, 2, 3, 4, 5, 1, 2, 2])
print(type(mi_set))
print(mi_set)

otro_set= {1,2,3}
print(type(otro_set))
print(otro_set)

print(len(mi_set))
print(2 in mi_set)

set1 = {1,2,3}
set2 = {3,4,5}
set3 = set1.union(set2)
print(set3)

set1.add(4)
set1.add(2)
print(set1)

set1.remove(3)
print(set1)

set1.discard(6)

set1.pop()
print(set1)

set1.clear()
print(set1)