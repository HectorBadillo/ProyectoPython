print("\n\tEl programa te generara tu comision del 13% de tus ventas del mes\n")
nombre = input("Ingrese su nombre: ")
ventas = float(input("Digite sus ventas de este mes: $"))

comision = round(ventas*0.13,3)

print("{} Tu comision del mes es de: ${}".format(nombre,comision))
