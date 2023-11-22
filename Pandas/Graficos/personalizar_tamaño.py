import pandas as pd

tabla = pd.read_csv('C:\\Users\\psbad\\OneDrive\\Documentos\\Visual Studio Code\\Proyecto Python\\Pandas\\VentasPorProveedor.csv', skiprows = 5, sep=';')

import matplotlib.pyplot as plt

alimentos = tabla[tabla.Categoría == "Comestibles"]
alimentos.Artículo.value_counts().plot(kind="line", figsize= (10,5))
plt.show()