from abstract_factory import AbstractFactory
from abstract_analisis import AbstractAnalisis
from abstract_grafica import AbstractGrafica
from grafica import Grafica

class ConcreteGraficasFactory(AbstractFactory):

    def crear_analisis_estadistico(self) -> AbstractAnalisis:
        return None # No se implementa en este caso

    def crear_graficas(self) -> AbstractGrafica:
        return Grafica()