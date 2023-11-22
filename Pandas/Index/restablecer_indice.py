import pandas as pd

tabla = pd.read_csv('C:\\Users\\psbad\\OneDrive\\Documentos\\Visual Studio Code\\Proyecto Python\\Pandas\\VentasPorProveedor.csv', skiprows = 5, sep=';')

print(tabla.head())

print(tabla.set_index("Vendedor"))
print(tabla.head())

print(tabla.set_index("Vendedor", inplace= True))   #Se establece el indice
print(tabla.reset_index(inplace=True))

vendedor = (tabla.set_index("Vendedor"))

print(vendedor.head())
print(vendedor.reset_index(inplace=True))           #Restablecer
print(vendedor.head())