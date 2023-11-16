from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


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


class HojaMenu(MenuComponente):
    """
    The Leaf class represents the end objects of a composition. A leaf can't
    have any children.

    Usually, it's the Leaf objects that do the actual work, whereas Composite
    objects only delegate to their sub-components.
    """

    def __init__(self, nombre: str, precio: float) -> None:
        self._nombre = nombre
        self._precio = precio

    def operacion(self) -> str:
        return f"{self._nombre}: {self._precio}."
    
    def precio(self) -> float:
        return self._precio


class Composite(MenuComponente):
    """
    The Composite class represents the complex components that may have
    children. Usually, the Composite objects delegate the actual work to their
    children and then "sum-up" the result.
    """

    def __init__(self, nombre: str) -> None:
        self._nombre = nombre
        self._hijos: List[MenuComponente] = []

    """
    A composite object can add or remove other components (both simple or
    complex) to or from its child list.
    """

    def agregar(self, componente: MenuComponente) -> None:
        self._hijos.append(componente)
        componente.padre = self

    def eliminar(self, componente: MenuComponente) -> None:
        self._hijos.remove(componente)
        componente.padre = None

    def operacion(self) -> str:
        """
        The Composite executes its primary logic in a particular way. It
        traverses recursively through all its children, collecting and summing
        their results. Since the composite's children pass these calls to their
        children and so forth, the whole object tree is traversed as a result.
        """

        res = [hijo.operacion() for hijo in self._hijos]
        return f"{self._nombre}: {', '.join(res)}"

    def precio(self) -> float:
        return sum(hijo.precio() for hijo in self._hijos)