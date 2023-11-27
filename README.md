# Patrones Estructurales

Mi dirección de GitHub para este repositorio es la siguiente: [GitHub](https://github.com/lauralardies/patrones_estructurales)
https://github.com/lauralardies/patrones_estructurales


## Enunciados

En este repositorio trabajamos sobre dos ejercicios diferentes:

### Ejercicio 1

Tras el éxito inicial de su plataforma digital de creación y gestión de pizzas gourmet personalizadas, la cadena "Delizioso" desea llevar su propuesta al siguiente nivel. Ahora, aparte de permitir la personalización individual de pizzas, quiere ofrecer a sus clientes la posibilidad de combinar sus creaciones en menús personalizados, que podrían incluir entradas, bebidas, pizzas y postres. Estos menús pueden ser creados tanto por el cliente como por el equipo culinario de "Delizioso", con opciones preestablecidas que representan la esencia de la marca.

**Objetivos:**
1. Desarrollo de Menús Personalizados:
   - Introducir la noción de un "menú", que puede contener varios elementos: entradas, bebidas, pizzas (que ya han sido definidas previamente con su sistema de creación de pizzas) y postres.
   - Un "menú" puede ser simple (contener elementos básicos) o compuesto (incluir otros menús más pequeños, como un "Combo Pareja" que incluye dos menús individuales).
   - Cada "menú" tendrá un código único y un precio, que se determina como la suma de los precios de sus elementos, con un descuento según la promoción aplicada.
2. Patrones de Diseño:
   - Implementar el patrón Composite para modelar la relación entre los elementos y menús, facilitando la creación, modificación y cálculo de precios de menús compuestos.
   - Continuar utilizando el patrón Builder para la creación detallada de las pizzas.
3. Interacción con CSV:
   - Ampliar el sistema de almacenamiento en CSV para incluir los menús personalizados, de forma que se pueda registrar y recuperar la información de menús individuales y compuestos.
   - Permitir que, a partir de un menú almacenado, se pueda reconstruir toda la estructura del menú con sus elementos individuales y precios.
4. Restricciones:
   - Las librerías estándar de Python para la interacción con archivos CSV están permitidas.
   - Se espera un diseño modular y orientado a objetos, con una clara separación de responsabilidades.
   - La implementación del cálculo del precio de un "menú" debe hacerse en tiempo de ejecución y ser eficiente.

**Entrega:**
- Un diagrama UML detallando las clases, relaciones y métodos.
- Código Python correspondiente a la implementación.
- Un breve informe que justifique las decisiones de diseño tomadas y explique cómo se han aplicado los patrones de diseño.
- Un conjunto de pruebas unitarias que demuestren la correcta funcionalidad del sistema.
 
### Ejercicio 2

## Archivos

## Código

### Ejercicio 1

#### Archivo `basico_menu.py`
```
from menu_componente import MenuComponente
from pizza_menucomponente import Pizza
from bebida_menucomponente import Bebida
from postre_menucomponente import Postre
from typing import List
import csv

class Basico(MenuComponente):
    def __init__(self, pizza="Pizza", bebida="Refresco", postre="Postre") -> None:
        self._nombre = "Básico"
        self._hijos: List[MenuComponente] = [Pizza(pizza, 7.00), Bebida(bebida, 1.50), Postre(postre, 2.25)]

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
```

####  Archivo `bebida_menucomponente.py`
```
from menu_componente import MenuComponente

class Bebida(MenuComponente):
    def __init__(self, nombre: str, precio: float) -> None:
        self._nombre = nombre
        self._precio = precio
    
    def operacion(self) -> str:
        return f"{self._nombre}: {self._precio}."
    
    def precio(self) -> float:
        return self._precio
```

#### Archivo `builder.py`
```
from __future__ import annotations
from abc import ABC, abstractmethod


class Builder(ABC):

    @property
    @abstractmethod
    def pizza(self) -> None:
        pass

    @abstractmethod
    def masa(self) -> None:
        pass

    @abstractmethod
    def salsa(self) -> None:
        pass

    @abstractmethod
    def ingredientes(self) -> None:
        pass

    @abstractmethod
    def coccion(self) -> None:
        pass

    @abstractmethod
    def presentacion(self) -> None:
        pass

    @abstractmethod
    def maridajes(self) -> None:
        pass

    @abstractmethod
    def extras(self) -> None:
        pass
```

#### Archivo `combo_pareja.py`
```
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
```

#### Archivo `config.py`
```
import os
import platform

def limpiar_pantalla():
    os.system('cls') if platform.system() == "Windows" else os.system('clear')
```

#### Archivo `director.py`
```
from builder import Builder


class Director:

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def construir_completo(self) -> None:
        self.builder.masa()
        self.builder.salsa()
        self.builder.ingredientes()
        self.builder.coccion()
        self.builder.presentacion()
        self.builder.maridajes()
        self.builder.extras()
```

#### Archivo `main.py`
```
from director import Director
from pizza_builder import PizzaBuilder
from combo_pareja import ComboPareja
from basico_menu import Basico
from config import limpiar_pantalla


# Cliente
def main():
    '''
    Desde esta función, el cliente podrá acceder a los servicios de la pizzeria desde la terminal
    '''
    director = Director()
    builder = PizzaBuilder()
    director.builder = builder

    while True:
        limpiar_pantalla()
        # Primero decidimos si queremos crear una pizza o coger un menú predefinido
        print("Selecciona una opción:\n[1] Menú predefinido.\n[2] Crear pizza personalizada.\n[3] Salir.")
        opcion = input('>> ')
        limpiar_pantalla()
        if opcion == '1': # Si elegimos menú predefinido, mostramos los menús disponibles
            print("Selecciona un menú:")
            print(f"Opción 1 - {ComboPareja().operacion()}")
            print(f"Precio total: {ComboPareja().precio()}\n")
            print(f"Opción 2 - {Basico().operacion()}")
            print(f"Precio total: {Basico().precio()}\n")
            seleccion = input('>> ')
            limpiar_pantalla()
            if seleccion == '1':
                while True:
                    while True:
                        print("¡Elige tu primera pizza!\n- Pizza Carbonara\n- Pizza Barbacoa\n- Pizza 4 Quesos\n- Pizza Margarita\n- Pizza Hawaiana\n- Pizza Vegetariana\n- Pizza 4 Estaciones\n- Pizza Napolitana\n- Pizza Romana\n- Pizza Prosciutto\n- Pizza Capricciosa\n- Pizza Diavola\n- Pizza Frutti di Mare\n- Pizza Calzone")
                        pizza1 = input('>> ')
                        limpiar_pantalla()
                        print("¡Elige tu segunda pizza!\n- Pizza Carbonara\n- Pizza Barbacoa\n- Pizza 4 Quesos\n- Pizza Margarita\n- Pizza Hawaiana\n- Pizza Vegetariana\n- Pizza 4 Estaciones\n- Pizza Napolitana\n- Pizza Romana\n- Pizza Prosciutto\n- Pizza Capricciosa\n- Pizza Diavola\n- Pizza Frutti di Mare\n- Pizza Calzone")
                        pizza2 = input('>> ')
                        limpiar_pantalla()
                        pizzas = ["Pizza Carbonara", "Pizza Barbacoa", "Pizza 4 Quesos", "Pizza Margarita", "Pizza Hawaiana", "Pizza Vegetariana", "Pizza 4 Estaciones", "Pizza Napolitana", "Pizza Romana", "Pizza Prosciutto", "Pizza Capricciosa", "Pizza Diavola", "Pizza Frutti di Mare", "Pizza Calzone"]
                        if pizza1 not in pizzas or pizza2 not in pizzas:
                            print("Opción no válida. Inténtalo de nuevo.\nDebes seleccionar una pizza de la lista")
                            input('Presiona cualquier tecla para continuar...')
                            limpiar_pantalla()
                        else:
                            break
                    while True:
                        print("¡Elige tu bebida!\n- Coca Cola\n- Fanta\n- Sprite\n- Agua\n- Cerveza\n- Cerveza sin gluten")
                        bebida = input('>> ')
                        limpiar_pantalla()
                        bebidas = ["Coca Cola", "Fanta", "Sprite", "Agua", "Cerveza", "Cerveza sin gluten"]
                        if bebida not in bebidas:
                            print("Opción no válida. Inténtalo de nuevo.\nDebes seleccionar una bebida de la lista")
                            input('Presiona cualquier tecla para continuar...')
                            limpiar_pantalla()
                        else:
                            break
                    while True:
                        print("¡Elige tu postre!\n- Tiramisú\n- Brownie\n- Helado\n- Tarta de queso\n- Tarta de manzana\n- Tarta de chocolate")
                        postre = input('>> ')
                        limpiar_pantalla()
                        postres = ["Tiramisú", "Brownie", "Helado", "Tarta de queso", "Tarta de manzana", "Tarta de chocolate"]
                        if postre not in postres:
                            print("Opción no válida. Inténtalo de nuevo.\nDebes seleccionar un postre de la lista")
                            input('Presiona cualquier tecla para continuar...')
                            limpiar_pantalla()
                        else:
                            break
                    print("Tu menú: ")
                    print(ComboPareja(pizza1, pizza2, bebida, postre).operacion())
                    print(f"Precio total: {ComboPareja(pizza1, pizza2, bebida, postre).precio()}")
                    print("¿Te gusta tu menú? [Y]/N")
                    respuesta = input('>> ')
                    limpiar_pantalla()
                    if respuesta.capitalize() == 'N':
                        print('Empecemos de nuevo')
                        input('Presiona cualquier tecla para continuar...')
                    else:
                        ComboPareja(pizza1, pizza2, bebida, postre).agregar_csv()
                        print('¡Gracias por tu compra!')
                        input('Presiona cualquier tecla para continuar...')
                        break

            elif seleccion == '2':
                while True:
                    while True:
                        print("¡Elige tu pizza!\n- Pizza Carbonara\n- Pizza Barbacoa\n- Pizza 4 Quesos\n- Pizza Margarita\n- Pizza Hawaiana\n- Pizza Vegetariana\n- Pizza 4 Estaciones\n- Pizza Napolitana\n- Pizza Romana\n- Pizza Prosciutto\n- Pizza Capricciosa\n- Pizza Diavola\n- Pizza Frutti di Mare\n- Pizza Calzone")
                        pizza = input('>> ')
                        limpiar_pantalla()
                        pizzas = ["Pizza Carbonara", "Pizza Barbacoa", "Pizza 4 Quesos", "Pizza Margarita", "Pizza Hawaiana", "Pizza Vegetariana", "Pizza 4 Estaciones", "Pizza Napolitana", "Pizza Romana", "Pizza Prosciutto", "Pizza Capricciosa", "Pizza Diavola", "Pizza Frutti di Mare", "Pizza Calzone"]
                        if pizza not in pizzas:
                            print("Opción no válida. Inténtalo de nuevo.\nDebes seleccionar una pizza de la lista")
                            input('Presiona cualquier tecla para continuar...')
                            limpiar_pantalla()
                        else:
                            break
                    while True:
                        print("¡Elige tu bebida!\n- Coca Cola\n- Fanta\n- Sprite\n- Agua\n- Cerveza\n- Cerveza sin gluten")
                        bebida = input('>> ')
                        limpiar_pantalla()
                        bebidas = ["Coca Cola", "Fanta", "Sprite", "Agua", "Cerveza", "Cerveza sin gluten"]
                        if bebida not in bebidas:
                            print("Opción no válida. Inténtalo de nuevo.\nDebes seleccionar una bebida de la lista")
                            input('Presiona cualquier tecla para continuar...')
                            limpiar_pantalla()
                        else:
                            break
                    while True:
                        print("¡Elige tu postre!\n- Tiramisú\n- Brownie\n- Helado\n- Tarta de queso\n- Tarta de manzana\n- Tarta de chocolate")
                        postre = input('>> ')
                        limpiar_pantalla()
                        postres = ["Tiramisú", "Brownie", "Helado", "Tarta de queso", "Tarta de manzana", "Tarta de chocolate"]
                        if postre not in postres:
                            print("Opción no válida. Inténtalo de nuevo.\nDebes seleccionar un postre de la lista")
                            input('Presiona cualquier tecla para continuar...')
                            limpiar_pantalla()
                        else:
                            break
                    print("Tu menú: ")
                    print(Basico(pizza, bebida, postre).operacion())
                    print(f"Precio total: {Basico(pizza, bebida, postre).precio()}")
                    print("¿Te gusta tu menú? [Y]/N")
                    respuesta = input('>> ')
                    limpiar_pantalla()
                    if respuesta.capitalize() == 'N':
                        print('Empecemos de nuevo')
                        input('Presiona cualquier tecla para continuar...')
                    else:
                        Basico(pizza, bebida, postre).agregar_csv()
                        print('¡Gracias por tu compra!')
                        input('Presiona cualquier tecla para continuar...')
                        break

            else:
                print('Opción no válida. Inténtalo de nuevo.\nDebes seleccionar 1 o 2')
                input('Presiona cualquier tecla para continuar...')

        elif opcion == '2': # Si elegimos crear pizza personalizada
            while True:
                print("Crea tu pizza: ")
                director.construir_completo()
                builder.pizza.guardar_csv()

                # Luego mostramos la pizza creada
                limpiar_pantalla()
                print("Tu pizza: ")
                builder.pizza.visualizacion_csv()

                # Finalmente preguntamos si le gusta la pizza
                print("¿Te gusta tu pizza? [Y]/N")
                respuesta = input('>> ')
                limpiar_pantalla()
                if respuesta.capitalize() == 'N': # Si no le gusta, volvemos a empezar
                    builder.pizza.borrar_pizza()
                    print('Empecemos de nuevo')
                    input('Presiona cualquier tecla para continuar...')
                else: # Si le gusta, guardamos la pizza y terminamos
                    print('¡Gracias por tu compra!')
                    input('Presiona cualquier tecla para continuar...')
                    break
        
        elif opcion == '3': # Si elegimos salir, terminamos
            print('¡Gracias por tu visita!')
            input('Presiona cualquier tecla para salir...')
            break

        else:
            print('Opción no válida. Inténtalo de nuevo.\nDebes seleccionar 1, 2 o 3')
            input('Presiona cualquier tecla para continuar...')
```

#### Archivo `menu_componente.py`
```
from __future__ import annotations
from abc import ABC, abstractmethod

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

    def agregar_csv(self) -> None:
        pass
```

#### Archivo `pizza_builder.py`
```
from builder import Builder
from pizza import Pizza

class PizzaBuilder(Builder):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._pizza = Pizza()

    @property
    def pizza(self) -> Pizza:
        pizza = self._pizza
        self.reset()
        return pizza

    def masa(self) -> None:
        '''
        El cliente selecciona el tipo de masa que quiere para su pizza
        '''
        while True:
            print("Seleccione el tipo de masa: \n- Masa tradicional\n- Masa integral\n- Masa sin gluten\n")
            opcion = input(">> ")
            if opcion in ["Masa tradicional", "Masa integral", "Masa sin gluten"]: 
                self._pizza.agregar(opcion)
                break
            else:
                print("Opción no valida\n")

    def salsa(self) -> None:
        '''
        El cliente selecciona el tipo de salsa que quiere para su pizza
        '''
        while True:
            print("Seleccione el tipo de salsa: \n- Salsa de tomate\n- Salsa barbacoa\n- Salsa carbonara\n")
            opcion = input(">> ")
            if opcion in ["Salsa de tomate", "Salsa barbacoa", "Salsa carbonara"]:
                self._pizza.agregar(opcion)
                break
            else:
                print("Opción no valida\n")

    def ingredientes(self) -> None:
        '''
        El cliente selecciona los ingredientes que quiere para su pizza, aunque también le damos una recomendación
        '''
        # Primero hacemos una recomendación basada en las opciones seleccionadas hasta ahora.
        if self._pizza.partes[0] == "Masa tradicional" and self._pizza.partes[1] == "Salsa de tomate":
            print("Le recomendamos agregar jamón y queso")
        elif self._pizza.partes[0] == "Masa integral" and self._pizza.partes[1] == "Salsa barbacoa":
            print("Le recomendamos agregar bacon y cebolla")
        elif self._pizza.partes[0] == "Masa sin gluten" and self._pizza.partes[1] == "Salsa carbonara":
            print("Le recomendamos agregar piña y carne picada")
        else:
            print("No hay recomendaciones de ingredientes")
        # Luego le pedimos que seleccione los ingredientes.
        while True:
            print("Seleccione los ingredientes separados por comas: \n- Jamon\n- Queso\n- Bacon\n- Cebolla\n- Pimiento\n- Piña\n- Carne picada\n- Pollo\n- Atun\n- Tomate\n- Aceitunas\n- Maiz\n- Champiñones\n- Anchoas\n- Salami\n- Pimiento picante\n- Rucula\n- Salsa barbacoa\n- Salsa carbonara\n")
            opciones = input(">> ").split(", ")
            no_validas = []
            for opcion in opciones:
                if opcion not in ["Jamon", "Queso", "Bacon", "Cebolla", "Pimiento", "Piña", "Carne picada", "Pollo", "Atun", "Tomate", "Aceitunas", "Maiz", "Champiñones", "Anchoas", "Salami", "Pimiento picante", "Rucula", "Salsa barbacoa", "Salsa carbonara"]:
                    no_validas.append(opcion)
                else:
                    pass
            if len(no_validas) == 0:
                self._pizza.agregar(opciones)
                break
            else:
                print("Hay alguna opción no válida, vuelva a intentarlo\n")

    def coccion(self) -> None:
        '''
        El cliente selecciona el tipo de cocción que quiere para su pizza
        '''
        while True:
            print("Seleccione el tipo de cocción: \n- Horno de leña\n- Horno electrico\n- Horno de gas\n")
            opcion = input(">> ")
            if opcion in ["Horno de leña", "Horno electrico", "Horno de gas"]:
                self._pizza.agregar(opcion)
                break
            else:
                print("Opción no valida\n")

    def presentacion(self) -> None:
        '''
        El cliente selecciona el tipo de presentación que quiere para su pizza
        '''
        while True:
            print("Seleccione el tipo de presentación: \n- Pizza entera\n- Pizza por raciones\n")
            opcion = input(">> ")
            if opcion in ["Pizza entera", "Pizza por raciones"]:
                self._pizza.agregar(opcion)
                break
            else:
                print("Opción no valida\n")

    def maridajes(self) -> None:
        '''
        El cliente selecciona el tipo de maridaje que quiere para su pizza, aunque también le damos una recomendación
        '''
        # Primero hacemos una recomendación basada en las opciones seleccionadas hasta ahora.
        if self._pizza.partes[0] == "Masa tradicional" and self._pizza.partes[1] == "Salsa de tomate" and self._pizza.partes[2] == ["Jamon", "Queso"]:
            print("Maridaje recomendado: Vino tinto")
        elif self._pizza.partes[0] == "Masa integral" and self._pizza.partes[1] == "Salsa barbacoa" and self._pizza.partes[2] == ["Bacon", "Cebolla"]:
            print("Maridaje recomendado: Vino blanco") 
        elif self._pizza.partes[0] == "Masa sin gluten" and self._pizza.partes[1] == "Salsa carbonara" and self._pizza.partes[2] == ["Piña", "Carne picada"]: 
            print("Maridaje recomendado: Cerveza sin gluten")
        else:
            print("No hay maridaje recomendado")
        # Luego le pedimos que seleccione los maridajes.
        while True:
            print("Seleccione un maridajes para acompañar: \n- Vino tinto\n- Vino blanco\n- Cerveza\n- Cerveza sin gluten\n- Refresco\n- Agua\n- None\n")
            opcion = input(">> ")
            if opcion in ["Vino tinto", "Vino blanco", "Cerveza", "Cerveza sin gluten", "Refresco", "Agua", "None"]:
                self._pizza.agregar(opcion)
                break
            else:
                print("Opción no válida\n")

    def extras(self) -> None:
        '''
        El cliente selecciona si quier agregar algún ingrediente extra a la pizza
        '''
        while True:
            print("Seleccione los extras separados por comas: \n- Queso extra\n- Jamon extra\n- Bacon extra\n- Cebolla extra\n- Pimiento extra\n- Piña extra\n- Carne picada extra\n- Pollo extra\n- Atun extra\n- Tomate extra\n- Aceitunas extra\n- Maiz extra\n- Champiñones extra\n- Anchoas extra\n- Salami extra\n- Pimiento picante extra\n- Rucula extra\n- Salsa barbacoa extra\n- Salsa carbonara extra\n- None\n")
            opciones = input(">> ").split(", ")
            no_validas = []
            for opcion in opciones:
                if opcion not in ["Queso extra", "Jamon extra", "Bacon extra", "Cebolla extra", "Pimiento extra", "Piña extra", "Carne picada extra", "Pollo extra", "Atun extra", "Tomate extra", "Aceitunas extra", "Maiz extra", "Champiñones extra", "Anchoas extra", "Salami extra", "Pimiento picante extra", "Rucula extra", "Salsa barbacoa extra", "Salsa carbonara extra", "None"]:
                    no_validas.append(opcion)
                else:
                    pass
            if len(no_validas) == 0:
                self._pizza.agregar(opciones)
                break
            else:
                print("Hay alguna opción no válida, vuelva a intentarlo\n")
```

#### Archivo `pizza_menucomponente.py`
```
from menu_componente import MenuComponente

class Pizza(MenuComponente):
    def __init__(self, nombre: str, precio: float) -> None:
        self._nombre = nombre
        self._precio = precio

    def operacion(self) -> str:
        return f"{self._nombre}: {self._precio}."
    
    def precio(self) -> float:
        return self._precio
```

#### Archivo `pizza.py`
```
from typing import Any
import csv


class Pizza():

    def __init__(self) -> None:
        self.partes = []

    def agregar(self, parte: Any) -> None:
        '''
        Agregamos las elecciones del cliente a la pizza
        '''
        self.partes.append(parte)
    
    def guardar_csv(self):
        '''
        Guardamos la pizza generada por el cliente en un archivo csv
        '''
        with open("Patrones Estructurales/Ejercicio 1/data/pizza_cliente.csv", "a", newline="") as archivo:
            writer = csv.writer(archivo)
            writer.writerow(self.partes)
    
    def ultima_fila(self):
        '''
        Con este método obtenemos la última fila del archivo csv
        '''
        with open("Patrones Estructurales/Ejercicio 1/data/pizza_cliente.csv", "r") as archivo:
            reader = csv.reader(archivo)
            for row in reader:
                last_row = row
            return last_row

    def visualizacion_csv(self) -> None:
        '''
        Leemos el archivo csv y mostramos la pizza creada por el cliente
        '''
        for element in self.ultima_fila():
            if '[' in element and ']' in element:
                element = element.replace('[', '')
                element = element.replace(']', '')
                element = element.replace("'", '')
            else:
                pass
            print(f"- {element}")

    def borrar_pizza(self):
        '''
        En caso de que el cliente no quiera la pizza que creó, borramos la última fila del archivo csv
        '''
        f = open('Patrones Estructurales/Ejercicio 1/data/pizza_cliente.csv', "r+")
        lines = f.readlines()
        lines.pop()
        f = open('Patrones Estructurales/Ejercicio 1/data/pizza_cliente.csv', "w+")
        f.writelines(lines)
```

#### Archivo `postre_menucomponente.py`
```
from menu_componente import MenuComponente

class Postre(MenuComponente):
    def __init__(self, nombre: str, precio: float) -> None:
        self._nombre = nombre
        self._precio = precio
    
    def operacion(self) -> str:
        return f"{self._nombre}: {self._precio}."
    
    def precio(self) -> float:
        return self._precio
```

#### Archivo `run.py`
```
from main import main


if __name__ == "__main__":
    '''
    Lanzador del programa
    '''
    main()
```

#### Archivo `tests.py`
```
import unittest
import os
import csv
from pizza_menucomponente import Pizza
from bebida_menucomponente import Bebida
from postre_menucomponente import Postre
from combo_pareja import ComboPareja
from basico_menu import Basico

class TestMenuComponente(unittest.TestCase):

    def setUp(self):
        self.pizza = Pizza("Pizza de Pepperoni", 8.00)
        self.bebida = Bebida("Refresco de Cola", 2.00)
        self.postre = Postre("Tarta de Chocolate", 3.50)
        self.combo_pareja = ComboPareja("Pizza Margarita", "Pizza Hawaiana", "Agua", "Helado")
        self.basico = Basico("Pizza Vegetariana", "Refresco de Limón", "Brownie")

    def tearDown(self):
        if os.path.exists("Patrones Estructurales/Ejercicio 1/data/pizza_cliente.csv"):
            os.remove("Patrones Estructurales/Ejercicio 1/data/pizza_cliente.csv")

    def test_precio_pizza(self):
        self.assertEqual(self.pizza.precio(), 8.00)

    def test_operacion_pizza(self):
        self.assertEqual(self.pizza.operacion(), "Pizza de Pepperoni: 8.0.")

    def test_precio_bebida(self):
        self.assertEqual(self.bebida.precio(), 2.00)

    def test_operacion_bebida(self):
        self.assertEqual(self.bebida.operacion(), "Refresco de Cola: 2.0.")

    def test_precio_postre(self):
        self.assertEqual(self.postre.precio(), 3.50)

    def test_operacion_postre(self):
        self.assertEqual(self.postre.operacion(), "Tarta de Chocolate: 3.5.")

    def test_precio_combo_pareja(self):
        self.assertEqual(self.combo_pareja.precio(), 17.75)

    def test_operacion_combo_pareja(self):
        expected_output = "Menú Combo pareja:\n Pizza Margarita: 7.0., Pizza Hawaiana: 7.0., Agua: 1.5., Helado: 2.25."
        self.assertEqual(self.combo_pareja.operacion(), expected_output)

    def test_precio_basico(self):
        self.assertEqual(self.basico.precio(), 10.75)

    def test_operacion_basico(self):
        expected_output = "Menú Básico:\n Pizza Vegetariana: 7.0., Refresco de Limón: 1.5., Brownie: 2.25."
        self.assertEqual(self.basico.operacion(), expected_output)

    def test_agregar_csv(self):
        self.combo_pareja.agregar_csv()
        with open("Patrones Estructurales/Ejercicio 1/data/pizza_cliente.csv", newline="") as archivo:
            row = archivo.readlines()[-1]
            expected_row = "Pizza Margarita,Pizza Hawaiana,Agua,Helado\r\n"
            self.assertEqual(row, expected_row)

if __name__ == '__main__':
    unittest.main()
```

### Ejercicio 2

