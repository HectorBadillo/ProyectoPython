import pandas as pd

tabla = pd.read_csv('C:\\Users\\psbad\\OneDrive\\Documentos\\Visual Studio Code\\Proyecto Python\\Pandas\\VentasPorProveedor.csv', skiprows = 5, sep=';')

print(tabla.iloc[231])

print(tabla.iloc[[231,49,162,101]])

print(tabla.iloc[7:14])