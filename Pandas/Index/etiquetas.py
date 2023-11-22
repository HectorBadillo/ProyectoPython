import pandas as pd

tabla = pd.read_csv('C:\\Users\\psbad\\OneDrive\\Documentos\\Visual Studio Code\\Proyecto Python\\Pandas\\VentasPorProveedor.csv', skiprows = 5, sep=';')


tabla.set_index("Vendedor", inplace=True)
print(tabla.loc["Sarah Bond"])
tabla.reset_index(inplace=True)
print(tabla.head())

print(tabla.loc[tabla.Vendedor == "Sarah Bond"])