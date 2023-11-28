from component import Component
from typing import List


class Carpeta(Component):
    def __init__(self, nombre, parent=None) -> None:
        self._nombre = nombre
        self._parent = parent
        self._children: List[Component] = []
        self._tam = 0

    def add(self, component: Component) -> None:
        self._children.append(component)
        self._tam += int(component.tam())
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        self._tam -= int(component.tam())
        component.parent = None

    def get_name(self) -> str:
        return f"Carpeta {self._nombre}"

    def tam(self) -> str:
        return self._tam
    
    def access(self) -> None:
        return [x.get_name() for x in self._children]