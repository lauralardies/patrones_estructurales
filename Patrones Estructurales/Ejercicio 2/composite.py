from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
from config import limpiar_pantalla


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
    def get_name(self) -> str:
        pass

    @abstractmethod
    def tam(self) -> str:
        pass

    @abstractmethod
    def access(self):
        pass


class Documento(Component):
    def __init__(self, nombre, contenido, tipo, tam, sensible=False) -> None:
        self._nombre = nombre
        self._contenido = contenido
        self._tipo = tipo
        self._tam = tam
        self._sensible = sensible 
    
    def add(self):
        print("Este es el contenido de su documento: \n\n" + self._contenido)
        input("Pulse cualquier tecla para continuar...")
        limpiar_pantalla()
        print("Introduzca el texto que desea añadir al documento, se añadirá al final del mismo: ")
        texto = input(">> ")
        self._contenido += texto
        limpiar_pantalla()
        print("Se ha añadido el texto correctamente.\n\nEste es el contenido de su documento actualizado: \n\n" + self._contenido)
        input("Pulse cualquier tecla para continuar...")
       
    def remove(self):
        print("Este es el contenido de su documento: \n\n" + self._contenido)
        input("Pulse cualquier tecla para continuar...")
        limpiar_pantalla()
        print("Introduzca el texto que desea eliminar del documento: ")
        texto = input(">> ")
        self._contenido = self._contenido.replace(texto, "")
        limpiar_pantalla()
        print("Se ha eliminado el texto correctamente.\n\nEste es el contenido de su documento actualizado: \n\n" + self._contenido)
        input("Pulse cualquier tecla para continuar...")

    def get_name(self) -> str:
        return self._nombre
    
    def tam(self) -> str:
        return self._tam
    
    def access(self):
        return self._contenido

class Enlace(Component):
    def __init__(self, ruta) -> None:
        self._nombre = ruta.split("/")[-1] # Nombre del enlace = nombre del archivo al que apunta
        self._ruta = ruta
        self._tam = 2 # Tamaño simbólico

    def get_name(self) -> str:
        return self._nombre
    
    def tam(self) -> str:
        return self._tam
    
    def access(self):
        return self._ruta


class Carpeta(Component):
    def __init__(self, nombre) -> None:
        self._nombre = nombre
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
        return self._nombre

    def tam(self) -> str:
        return self._tam
    
    def access(self) -> None:
        return [x.get_name() for x in self._children]