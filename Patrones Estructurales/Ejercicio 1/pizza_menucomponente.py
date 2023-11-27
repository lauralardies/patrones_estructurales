from menu_componente import MenuComponente

class Pizza(MenuComponente):
    def __init__(self, nombre: str, precio: float) -> None:
        self._nombre = nombre
        self._precio = precio

    def operacion(self) -> str:
        return f"{self._nombre}: {self._precio}."
    
    def precio(self) -> float:
        return self._precio