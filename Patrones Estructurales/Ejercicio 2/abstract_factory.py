from __future__ import annotations
from abc import ABC, abstractmethod
from abstract_analisis import AbstractAnalisis
from abstract_grafica import AbstractGrafica

class AbstractFactory(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def crear_analisis_estadistico(self) -> AbstractAnalisis:
        pass

    @abstractmethod
    def crear_graficas(self) -> AbstractGrafica:
        pass