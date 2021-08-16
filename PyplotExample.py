# Librerias importadas
# Graficar datos
from matplotlib import pyplot as plt
import numpy as np

# Lista de puntos 
years = [2008,2009,2010,2011,2012,2013]
prices = [160,167,171,166,159,161]
prices2 = [162,163,172,163,166,159]

np_arr = np.array(prices2)

# Crear el grafico
plt.plot(years,prices)
plt.plot(years,np_arr)

# Mostrar el grafico
plt.show()