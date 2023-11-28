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


class Documento(Component):
    def __init__(self, nombre, tipo, tam) -> None:
        self._nombre = nombre
        self._tipo = tipo
        self._tam = tam

    def tam(self) -> str:
        return self._tam


class Enlace(Component):
    def __init__(self, contenido, tam) -> None:
        self._contenido = contenido
        self._tam = tam # Tamaño simbólico

    def tam(self) -> str:
        return self._tam


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