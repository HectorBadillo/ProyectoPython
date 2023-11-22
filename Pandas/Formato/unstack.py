import pandas as pd

tabla = pd.read_csv('C:\\Users\\psbad\\OneDrive\\Documentos\\Visual Studio Code\\Proyecto Python\\Pandas\\VentasPorProveedor.csv', skiprows = 5, sep=';')

cat = (tabla[(tabla.Vendedor == "Sarah Bond") & ((tabla.Categoría == "Vestimenta")) | (tabla.Categoría == "Comestibles")])
print(cat)

c = (cat.groupby(["Artículo", "Categoría", "Región"]).size())
print(c)

df = c.unstack("Región")
print(df.unstack("Categoría"))