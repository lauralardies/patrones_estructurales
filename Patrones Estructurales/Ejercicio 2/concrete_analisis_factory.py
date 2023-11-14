from abstract_factory import AbstractFactory
from abstract_analisis import AbstractAnalisis
from abstract_grafica import AbstractGrafica
from analisis import Analisis

class ConcreteAnalisisFactory(AbstractFactory):

    def crear_analisis_estadistico(self) -> AbstractAnalisis:
        return Analisis()

    def crear_graficas(self) -> AbstractGrafica:
        return None # No se implementa en este caso