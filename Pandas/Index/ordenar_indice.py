import pandas as pd

tabla = pd.read_csv('C:\\Users\\psbad\\OneDrive\\Documentos\\Visual Studio Code\\Proyecto Python\\Pandas\\VentasPorProveedor.csv', skiprows = 5, sep=';')

vendedor = (tabla.set_index("Vendedor"))
vendedor.sort_index(inplace=True, ascending=False)
print(vendedor.head())
