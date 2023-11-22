import pandas as pd

tabla = pd.read_csv('C:\\Users\\psbad\\OneDrive\\Documentos\\Visual Studio Code\\Proyecto Python\\Pandas\\VentasPorProveedor.csv', skiprows = 5, sep=';')

print(tabla.groupby("Región").size())

print(tabla.groupby(["Región","Vendedor", "Ganancia"]).agg({"Región": ["min","max","count"]}))

print(tabla.loc[tabla.Vendedor == "Sarah Bond"].groupby("Vendedor").agg({"Ganancia": ["min","max"]}))