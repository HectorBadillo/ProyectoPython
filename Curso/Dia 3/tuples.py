mi_tuple = (1,2,3,4)
print(type( mi_tuple))
print(mi_tuple[2])

mi_tuple= (1,2,(10,20),4)
print((mi_tuple[2][0]))

mi_tuple= list(mi_tuple)
print(type(mi_tuple))

t= (1,2,3)
x,y,z= t
print(x,y,z)

t=(1,2,3,1)
print(len(t))
print(t.count(1))
print(t.index(2))