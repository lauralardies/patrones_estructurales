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
    def __init__(self, pizza1="Pizza 1", pizza2="Pizza 2", bebida="Refresco", postre="Postre") -> None:
        self._nombre = "Combo pareja"
        self._hijos: List[MenuComponente] = [Pizza(pizza1, 7.00), Pizza(pizza2, 7.00), Bebida(bebida, 1.50), Postre(postre, 2.25)]

    def operacion(self) -> str:
        res = [hijo.operacion() for hijo in self._hijos]
        return f"Menú {self._nombre}:\n {', '.join(res)}"

    def precio(self) -> float:
        return sum(hijo.precio() for hijo in self._hijos)
    
class Basico(MenuComponente):
    def __init__(self, pizza="Pizza", bebida="Refresco", postre="Postre") -> None:
        self._nombre = "Básico"
        self._hijos: List[MenuComponente] = [Pizza(pizza, 7.00), Bebida(bebida, 1.50), Postre(postre, 2.25)]

    def operacion(self) -> str:
        res = [hijo.operacion() for hijo in self._hijos]
        return f"Menú {self._nombre}:\n {', '.join(res)}"

    def precio(self) -> float:
        return sum(hijo.precio() for hijo in self._hijos)