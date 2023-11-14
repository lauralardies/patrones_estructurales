from abc import ABC, abstractmethod

class AbstractGrafica(ABC):
    
    @abstractmethod
    def mostrar_histograma(self, data, columna):
        pass

    def mostrar_diagrama_barras(self, data, columna):
        pass