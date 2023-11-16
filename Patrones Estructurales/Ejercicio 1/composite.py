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


class Pizza(MenuComponente):
    def __init__(self, nombre: str, precio: float) -> None:
        self._nombre = nombre
        self._precio = precio

    def operacion(self) -> str:
        return f"{self._nombre}: {self._precio}."
    
    def precio(self) -> float:
        return self._precio


class Bebida(MenuComponente):
    def __init__(self, nombre: str, precio: float) -> None:
        self._nombre = nombre
        self._precio = precio
    
    def operacion(self) -> str:
        return f"{self._nombre}: {self._precio}."
    
    def precio(self) -> float:
        return self._precio


class Postre(MenuComponente):
    def __init__(self, nombre: str, precio: float) -> None:
        self._nombre = nombre
        self._precio = precio
    
    def operacion(self) -> str:
        return f"{self._nombre}: {self._precio}."
    
    def precio(self) -> float:
        return self._precio


class ComboPareja(MenuComponente):
    def __init__(self) -> None:
        self._nombre = "Combo pareja"
        self._hijos: List[MenuComponente] = []

    def agregar(self, componente: MenuComponente) -> None:
        self._hijos.append(componente)
        componente.padre = self

    def eliminar(self, componente: MenuComponente) -> None:
        self._hijos.remove(componente)
        componente.padre = None

    def operacion(self) -> str:
        res = [hijo.operacion() for hijo in self._hijos]
        return f"{self._nombre}: {', '.join(res)}"

    def precio(self) -> float:
        return sum(hijo.precio() for hijo in self._hijos)