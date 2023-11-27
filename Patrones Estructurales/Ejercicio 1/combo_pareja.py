from menu_componente import MenuComponente
from pizza_menucomponente import Pizza
from bebida_menucomponente import Bebida
from postre_menucomponente import Postre
from typing import List
import csv

class ComboPareja(MenuComponente):
    def __init__(self, pizza1="Pizza 1", pizza2="Pizza 2", bebida="Refresco", postre="Postre") -> None:
        self._nombre = "Combo pareja"
        self._hijos: List[MenuComponente] = [Pizza(pizza1, 7.00), Pizza(pizza2, 7.00), Bebida(bebida, 1.50), Postre(postre, 2.25)]

    def operacion(self) -> str:
        res = [hijo.operacion() for hijo in self._hijos]
        return f"Menú {self._nombre}:\n {', '.join(res)}"

    def precio(self) -> float:
        return sum(hijo.precio() for hijo in self._hijos)
    
    def agregar_csv(self) -> None:
        nombres = [self._hijos[i]._nombre for i in range(len(self._hijos))]
        with open("Patrones Estructurales/Ejercicio 1/data/pizza_cliente.csv", "a", newline="") as archivo:
            writer = csv.writer(archivo)
            writer.writerow(nombres)