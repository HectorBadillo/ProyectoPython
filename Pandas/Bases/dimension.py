import pandas as pd

tabla = pd.read_csv('C:\\Users\\psbad\\OneDrive\\Documentos\\Visual Studio Code\\Proyecto Python\\Pandas\\VentasPorProveedor.csv', skiprows = 4, sep=';')

print(tabla.shape)
print(tabla.shape[0])
print(tabla.shape[1])