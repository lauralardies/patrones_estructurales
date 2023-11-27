from __future__ import annotations
from abc import ABC, abstractmethod

class MenuComponente(ABC):
    """
    The base Component class declares common operations for both simple and
    complex objects of a composition.
    """

    @property
    def padre(self) -> MenuComponente:
        return self._padre

    @padre.setter
    def padre(self, padre: MenuComponente):
        self._padre = padre

    def agregar(self, componente: MenuComponente) -> None:
        pass

    def eliminar(self, componente: MenuComponente) -> None:
        pass

    @abstractmethod
    def operacion(self) -> str:
        pass

    @abstractmethod
    def precio(self) -> float:
        pass

    def agregar_csv(self) -> None:
        pass