from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Component(ABC):
    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
        self._parent = parent

    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass

    @abstractmethod
    def tam(self) -> str:
        pass

    @abstractmethod
    def access(self) -> None:
        pass


class Documento(Component):
    def __init__(self, nombre, tipo, tam) -> None:
        self._nombre = nombre
        self._tipo = tipo
        self._tam = tam

    def tam(self) -> str:
        return self._tam
    
    def access(self) -> str:
        return self._nombre


class Enlace(Component):
    def __init__(self, ruta, tam) -> None:
        self._ruta = ruta
        self._tam = tam # Tamaño simbólico

    def tam(self) -> str:
        return self._tam
    
    def access(self) -> str:
        return self._nombre


class Carpeta(Component):
    def __init__(self) -> None:
        self._children: List[Component] = []

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    def tam(self) -> str:
        return sum([x.tam() for x in self._children])
    
    def access(self) -> None:
        return [x.access() for x in self._children]