import pandas as pd

tabla = pd.read_csv('C:\\Users\\psbad\\OneDrive\\Documentos\\Visual Studio Code\\Proyecto Python\\Pandas\\VentasPorProveedor.csv', skiprows = 5, sep=';')

print(list(tabla.groupby("Región")))

for group_key, group_value in tabla.groupby("Región"):
    print(group_key)
    print(group_value)