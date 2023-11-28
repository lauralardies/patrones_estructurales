from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
from config import limpiar_pantalla
from proxy import *


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
        self._access = False
    
    def add(self, texto):
        if self._sensible & (not self._access): # Si es sensible y no has registrado tu acceso, no puedes modificarlo
            print("No puede modificar el documento si no ha registrado su acceso previamente.")
            input("Pulse cualquier tecla para continuar...")
        else:
            self._contenido += texto

    def remove(self, texto):
        if self._sensible & (not self._access): # Si es sensible y no has registrado tu acceso, no puedes modificarlo
            print("No puede modificar el documento si no ha registrado su acceso previamente.")
            input("Pulse cualquier tecla para continuar...")
        else:
            self._contenido = self._contenido.replace(texto, "")

    def get_name(self) -> str:
        return f"Archivo {self._nombre}"
    
    def tam(self) -> str:
        return self._tam
 
    def access(self):
        if self._sensible:
            while True:
                limpiar_pantalla()
                print("El documento es sensible, se va a registrar su acceso. Facilite los siguientes datos:")
                nombre = input("Nombre: ")
                apellido = input("Apellido: ")
                dni = input("DNI: ")
                if nombre.isalpha() and apellido.isalpha() and dni.isalnum() and len(dni) == 9:
                    break
                else:
                    limpiar_pantalla()
                    print("Los datos introducidos no son válidos, inténtelo de nuevo.")
                    print("Asegúrese de no introducir espacios y de que el DNI tenga 8 dígitos y 1 letra.")

            real_subject = RealSubject(nombre, apellido, dni)
            self._access = Proxy(real_subject).request()

            if not self._access:
                return "No tiene acceso a este documento"
            
        return self._contenido


class Enlace(Component):
    def __init__(self, ruta) -> None:
        self._nombre = ruta.split("/")[-1] # Nombre del enlace = nombre del archivo al que apunta
        self._ruta = ruta
        self._tam = 2 # Tamaño simbólico

    def get_name(self) -> str:
        return f"Enlace {self._nombre}"
    
    def tam(self) -> str:
        return self._tam
    
    def access(self):
        return self._ruta


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