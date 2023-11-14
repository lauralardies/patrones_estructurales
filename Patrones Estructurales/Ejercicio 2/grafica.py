from abstract_grafica import AbstractGrafica    
import matplotlib.pyplot as plt

class Grafica(AbstractGrafica):

    def mostrar_histograma(self, data, columna):
        val = data[columna]
        if data[columna].dtypes == 'datetime64[ns]' or data[columna].dtypes == 'M8[ns]':
            val = data.groupby(data[columna].dt.date).size()
        val.plot(kind='hist')
        plt.savefig('Patrones Creacionales/Ejercicio 1/graficas/histograma.png')

    def mostrar_diagrama_barras(self, data, columna):
        val = data[columna]
        if data[columna].dtypes == 'datetime64[ns]' or data[columna].dtypes == 'M8[ns]':
            val = data.groupby(data[columna].dt.date).size()
        val.plot(kind='bar')
        plt.savefig('Patrones Creacionales/Ejercicio 1/graficas/diagramabarras.png')