import datetime

mi_hora = datetime.time(17, 35, 50)
print(type(mi_hora))
print(mi_hora)
print(mi_hora.minute)
print("-" * 50 + "\n")

mi_dia = datetime.date(2023, 11, 23)
print(mi_dia)
print(mi_dia.year)
print(mi_dia.ctime())
print(mi_dia.today())
print("-" * 50 + "\n")


from datetime import datetime
mi_fecha = datetime(2023,5,15,22,10,15)
print(mi_fecha)
mi_fecha = mi_fecha.replace(month=11)
print(mi_fecha.ctime())
print("-" * 50 + "\n")

from datetime import date
nacimiento = date(1995, 3, 5)
fallecio = date(2095, 6, 19)
vida = fallecio - nacimiento
print(vida)

despierta = datetime(2022,10,5,7,30)
dormir = datetime(2022,10,5,23,45)

tiempo = dormir - despierta
print(tiempo)