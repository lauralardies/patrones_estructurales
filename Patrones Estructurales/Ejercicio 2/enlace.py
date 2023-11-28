from component import Component


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