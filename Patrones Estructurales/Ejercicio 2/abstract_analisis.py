from abc import ABC, abstractmethod

class AbstractAnalisis(ABC):
    
    @abstractmethod
    def calcular_media(self, data, columna):
        pass
    
    def calcular_mediana(self, data, columna):
        pass

    def calcular_moda(self, data, columna):
        pass