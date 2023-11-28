from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
import csv
import datetime


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
    def list_element(self) -> str:
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

    def tam(self) -> str:
        return self._tam
    
    def list_element(self) -> str:
        return self._nombre
    
    def access(self):
        if self._sensible:
            print("El documento es sensible, se va a registrar su acceso. Facilite los siguientes datos:")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            dni = input("DNI: ")
            datos = [nombre, apellido, dni, self._nombre, datetime.datetime.now()]
            with open("Patrones Estructurales/Ejercicio 2/accesos/registro_accesos.csv", "a", newline="") as archivo:
                writer = csv.writer(archivo)
                writer.writerow(datos)
        return self._contenido

class Enlace(Component):
    def __init__(self, ruta, tam) -> None:
        self._ruta = ruta
        self._tam = tam # Tamaño simbólico

    def tam(self) -> str:
        return self._tam
    
    def list_element(self) -> str:
        return self._nombre
    
    def access(self):
        return self._ruta


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
        return [x.list_element() for x in self._children]