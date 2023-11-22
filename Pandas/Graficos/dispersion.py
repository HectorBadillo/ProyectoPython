import pandas as pd

tabla = pd.read_csv('C:\\Users\\psbad\\OneDrive\\Documentos\\Visual Studio Code\\Proyecto Python\\Pandas\\VentasPorProveedor.csv', skiprows = 5, sep=';')

import matplotlib.pyplot as plt

tabla.plot(kind="scatter", x='Unidades', y='Ganancia')
plt.show()