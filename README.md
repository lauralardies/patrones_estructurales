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

El SAMUR-Protección Civil, tras su proceso de digitalización, se enfrenta al reto de administrar una cantidad masiva de documentos digitales relacionados con sus activaciones y operaciones. Esta documentación no solo consiste en informes y registros, sino que también incluye imágenes, vídeos, audios y otros tipos de archivos multimedia. La necesidad de garantizar un acceso rápido pero seguro a esta información es esencial, especialmente cuando se trata de datos sensibles o confidenciales.

- Documentos: Estos son los archivos básicos en el sistema. Cada documento tiene un nombre, un tipo (texto, imagen, video, etc.) y un tamaño. El contenido de estos documentos puede ser accedido y modificado, pero para algunos documentos sensibles, es necesario llevar un registro de quién y cuándo se accede o modifica.
- Enlaces (Links): Son referencias a otros documentos o carpetas en el sistema. No poseen contenido propio, pero ofrecen una forma rápida de acceder a la información referenciada. Su tamaño es simbólico, no correspondiente al tamaño real del archivo o carpeta al que apuntan.
- Carpetas: Contenedores que albergan varios documentos, enlaces y otras carpetas. Su tamaño es la suma de los tamaños de todos los elementos contenidos. Se pueden expandir añadiendo más elementos en cualquier momento.
- Proxy de Acceso: Para garantizar la seguridad y la trazabilidad en el acceso a los documentos, se implementará un proxy que actuará como intermediario. Este proxy registrará cada acceso o modificación a los documentos, especialmente aquellos que sean sensibles o confidenciales, y solo permitirá el acceso a usuarios autorizados.

**Objetivos:**
1. Utilizar el patrón de diseño Composite para modelar la estructura de documentos del sistema.
2. Implementar el patrón Proxy para controlar y registrar el acceso a documentos específicos.
3. Desarrollar en Python las clases y la lógica necesaria para representar y gestionar los documentos, enlaces y carpetas, garantizando la seguridad y trazabilidad mediante el uso del proxy.
4. Implementar funciones que faciliten la navegación, creación, modificación y eliminación de elementos en el sistema.

**Instrucciones:**
- Diseñar un diagrama de clases que refleje la estructura propuesta, identificando las relaciones, interfaces y métodos esenciales.
- Implementar las clases en Python, asegurando buenas prácticas y la utilización adecuada de los patrones de diseño Composite y Proxy.
- Crear funciones que permitan navegar por la estructura, añadir documentos, modificar contenidos, eliminar elementos y acceder a través del Proxy.
- Desarrollar pruebas para validar la correcta implementación y comportamiento del sistema, especialmente en lo que respecta a la seguridad y registro de acceso a los documentos.

## Archivos

Todos los archivos están guardados en una carpeta llamada `Patrones Estructurales`, que a su vez contiene:
- Archivo `requirements.txt` que incluye todas las librerías necesarias para poder ejecutar el código que no vienen incluidas con Python. Es decir, en este archivo incluimos las bibliotecas que tenemos que instalar por separado empleando el comando `pip`.
- Carpeta `img` donde guardamos las fotos empleadas en este documento `README-md`.
- Carpeta `Ejercicio 1`:
  - Carpeta `data`. Aquí se genera un archivo `pizza_cliente.csv` donde se van almacenando las pizzas que pide el cliente.
  - Carpeta `uml`. Aquí se guarda una imagen PNG que representa un diagrama de clases del patrón Composite que hemos desarrollado.

<img alt="uml" src="https://github.com/lauralardies/patrones_estructurales/blob/main/Patrones Estructurales/Ejercicio 1/uml/uml.png">
    
  - Archivo `config.py` que contiene una función encargada de limpiar la terminal del usuario.
  - Archivo `tests.py`, donde se desarrollan pruebas para validar la correcta implementación y comportamiento del sistema.
  - Archivos que conforman un patrón Builder. Estos archivos son: `builder.py`, `director.py`, `pizza_builder.py`, `pizza.py`.
  - Archivos que conforman un patrón Composite. Estos archivos son: `basico_menu.py`, `bebida_menucomponente.py`, `combo_pareja.py`, `menu_componente.py`, `pizza_menucomponente.py`, `postre_menucomponente.py`.
  - Archivo `main.py`, código cliente que junta ambos patrones y es lo que ve el usuario.
  - Archivo `run.py`, el lanzador.
- Carpeta `Ejercicio 2`:
  - Carpeta `accesos`. Aquí se genera un archivo `registro_accesos.log` donde se van almacenando los registros de los usuarios que acceden a archivos clasificados como sensibles. 
  - Carpeta `uml`. Aquí se guardan dos imágenes PNG que representan los diagramas de clases de los patrones Composite y Proxy que hemos desarrollado.
    
<img alt="uml1" src="https://github.com/lauralardies/patrones_estructurales/blob/main/Patrones Estructurales/Ejercicio 2/uml/composite_uml.png">

<img alt="uml2" src="https://github.com/lauralardies/patrones_estructurales/blob/main/Patrones Estructurales/Ejercicio 2/uml/proxy_uml.png">


  - Archivo `config.py` que contiene una función encargada de limpiar la terminal del usuario.
  - Archivo `log.py` es donde se define un decorador personalizado que toma como parámetro la ruta del archivo `registro_accesos.log`. Si se pone el decorador sobre una función, el decorador almacena la información que devuelve dicha función en el archivo `registro_accesos.log`.
  - Archivo `tests.py`, donde se desarrollan pruebas para validar la correcta implementación y comportamiento del sistema.
  - Archivos que conforman un patrón Composite. Estos archivos son: `carpeta.py`, `component.py`, `documento.py`, `enlace.py`.
  - Archivos que conforman un patrón Proxy. Estos archivos son: `proxy.py`, `real_subject.py`, `subject.py`.
  - Archivo `main.py`, código cliente que junta ambos patrones y es lo que ve el usuario.
  - Archivo `run.py`, el lanzador.

Además, fuera de esta carpeta `Patrones Estructurales` encontramos una carpeta llamada `entorno` que incluye un entorno para este proyecto. 

## Ejecutar programa

Ejecutar los dos ejercicios de esta entrega es muy sencillo. 
- Para ejecutar el ejercicio 1, accede a la carpeta `Ejercicio 1` y ejecuta el archivo `run.py` que como ya hemos dicho, es el lanzador de este ejercicio. En consola se mostrará un menú desde el cual el usuario podrá ir pidiendo pizzas y/o menús.

<img alt="uml" src="https://github.com/lauralardies/patrones_estructurales/blob/main/Patrones Estructurales/img/menu_ej1.png">

- Para ejecutar el ejercicio 2, accede esta vez a la carpeta `Ejercicio 2` y ejecuta el archivo `run.py` de dicha carpeta, el lanzador del ejercicio 2. En consola se mostrará un menú desde el cual el usuario podrá crear, acceder, modificar y eliminar carpetas, documentos y/o enlaces.

<img alt="uml" src="https://github.com/lauralardies/patrones_estructurales/blob/main/Patrones Estructurales/img/menu_ej2.png">

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

#### Archivo `carpeta.py`
```
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
        if self._parent is not None:
            self._parent._tam += int(component.tam())
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        self._tam -= int(component.tam())
        if self._parent is not None:
            self._parent._tam -= int(component.tam())
        component.parent = None

    def get_name(self) -> str:
        return f"Carpeta {self._nombre}"

    def tam(self) -> str:
        return self._tam
    
    def access(self) -> None:
        return [x.get_name() for x in self._children]
```

#### Archivo `component.py`
```
from __future__ import annotations
from abc import ABC, abstractmethod


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
```

#### Archivo `config.py`
```
import os
import platform


def limpiar_pantalla():
    os.system('cls') if platform.system() == "Windows" else os.system('clear')
```

#### Archivo `documento.py`
```
from component import Component
from config import limpiar_pantalla
from real_subject import RealSubject
from proxy import Proxy


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
```

#### Archivo `enlace.py`
```
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
```

#### Archivo `log.py`
```
import datetime


def log(fichero_log):
    def decorador_log(func):
        def decorador_funcion(*args, **kwargs):
            with open(fichero_log, 'a') as opened_file:
                output = func(*args, **kwargs)
                output.append(str(datetime.datetime.now()))
                opened_file.write(f"{output}\n")
        return decorador_funcion
    return decorador_log
```

#### Archivo `main.py`
```
from component import Component
from config import limpiar_pantalla
from carpeta import Carpeta
from documento import Documento
from enlace import Enlace


def client_code(component: Component) -> None:
    while True:
        limpiar_pantalla()
        # Mostramos el contenido de la carpeta
        print(f"Contenido {component.get_name()}: ")
        print(f"Tamaño: {component.tam()} bytes")
        contenido = component.access()
        for c in contenido:
            print(f"- {c}")
        print("\n\n¿Qué desea hacer?")
        print("1. Crear carpeta")
        print("2. Crear documento")
        print("3. Crear enlace")
        print("4. Acceder elemento")
        print("5. Eliminar elemento")
        print("6. Salir")
        opcion = input("Introduzca el número de la opción que desee: ")
        limpiar_pantalla()

        if opcion == "1":
            nombre = input("Introduzca el nombre de la carpeta: ")
            component.add(Carpeta(nombre, component))
            limpiar_pantalla()
            print("Carpeta creada correctamente.")
            input("Pulse enter para continuar.")

        elif opcion == "2":
            nombre = input("Introduzca el nombre del documento: ")
            while True:
                limpiar_pantalla()
                print("- Tipos de documentos -\n- Texto\n- Imagen\n- Video\n- Audio\n- Otro\n")
                tipo = input("Introduzca el tipo del documento: ")
                if tipo not in ["Texto", "Imagen", "Video", "Audio", "Otro"]:
                    limpiar_pantalla()
                    print("Tipo de documento no válido. Inténtelo de nuevo.")
                    input("Pulse enter para continuar.")
                else:
                    limpiar_pantalla()
                    break
            contenido = input("Introduzca el contenido del documento: ")
            limpiar_pantalla()
            while True:
                try:
                    limpiar_pantalla()
                    tam = float(input("Introduzca el tamaño del documento (en bytes): "))
                    break
                except ValueError:
                    limpiar_pantalla()
                    print("Tamaño no válido. Inténtelo de nuevo. Asegúrese de introducir solo números. En caso de haber decimal, introduczca un punto en vez de una coma.")
                    input("Pulse enter para continuar.")
                    continue
            limpiar_pantalla()
            print("¿Es un documento sensible? Y/[N]")
            seleccion = input(">> ")
            limpiar_pantalla()
            if seleccion.capitalize() == "Y":
                component.add(Documento(nombre, contenido, tipo, tam, True))
                print("El documento es sensible, se registraran los datos de todo aquel que acceda a él.")
            else:
                component.add(Documento(nombre, contenido, tipo, tam))
                print("El documento no es sensible, no se registrarán los datos de todo aquel que acceda a él.")
            print("Documento creado correctamente.")
            input("Pulse enter para continuar.")

        elif opcion == "3":
            while True:
                ruta = input("Introduzca la ruta del enlace: ")
                if "/" not in ruta:
                    limpiar_pantalla()
                    print("Ruta no válida. Inténtelo de nuevo. Debe incluir al menos un '/'.")
                    input("Pulse enter para continuar.")
                    limpiar_pantalla()
                else:
                    break
            component.add(Enlace(ruta))
            limpiar_pantalla()
            print("Enlace creado correctamente.")
            input("Pulse enter para continuar.")

        elif opcion == "4":
            while True:
                # Mostramos el contenido de la carpeta
                print(f"Contenido {component.get_name()}: ")
                print(f"Tamaño: {component.tam()} bytes")
                contenido = component.access()
                for c in contenido:
                    print(f"- {c}")
                elemento = input("\n\nIntroduzca el nombre del elemento que desea acceder: ")
                if elemento not in component.access():
                    limpiar_pantalla()
                    print("Este elemento no existe en la carpeta. Inténtelo de nuevo. Asegúrese de incluir Archivo, Carpeta o Enlace en el nombre.")
                    input("Pulse enter para continuar.")
                    limpiar_pantalla()
                else:
                    if 'Archivo' in elemento:
                        tipo = 'Archivo'
                    elif 'Carpeta' in elemento:
                        tipo = 'Carpeta'
                    elif 'Enlace' in elemento:
                        tipo = 'Enlace'
                    break
            for child in component._children:
                if child.get_name() == elemento:
                    elemento = child
                    break

            if tipo == 'Carpeta':
                component = elemento

            elif tipo == 'Archivo':
                contenido = elemento.access()
                while True:
                    limpiar_pantalla()
                    print(f"Contenido {elemento.get_name()}:\n")
                    print(contenido)
                    print("\n¿Qué desea hacer?")
                    print("1. Agregar contenido")
                    print("2. Eliminar contenido")
                    print("3. Ver tamaño")
                    print("4. Salir")
                    opcion = input("Introduzca el número de la opción que desee: ")
                    limpiar_pantalla()

                    if opcion == '1':
                        texto = input("Introduzca el contenido que desea agregar: ")
                        elemento.add(texto)
                        contenido = elemento._contenido
                        limpiar_pantalla()
                        print("Contenido agregado correctamente.")
                        input("Pulse enter para continuar.")

                    elif opcion == '2':
                        texto = input("Introduzca el contenido que desea eliminar: ")
                        elemento.remove(texto)
                        contenido = elemento._contenido
                        limpiar_pantalla()
                        print("Contenido eliminado correctamente.")
                        input("Pulse enter para continuar.")

                    elif opcion == '3':
                        print(f"El tamaño del archivo es de {elemento.tam()} bytes.")
                        input("Pulse enter para continuar.")

                    elif opcion == '4':
                        input("Pulse enter para continuar.")
                        break

                    else:
                        print("Opción no válida. Inténtelo de nuevo.")
                        input("Pulse enter para continuar.")
            
            elif tipo == 'Enlace':
                limpiar_pantalla()
                print("Contenido:\n")
                print(elemento.access())
                input("\nPulse enter para continuar.")


        elif opcion == "5":
            while True:
                # Mostramos el contenido de la carpeta
                print(f"Contenido {component.get_name()}: ")
                print(f"Tamaño: {component.tam()} bytes")
                contenido = component.access()
                for c in contenido:
                    print(f"- {c}")
                elemento = input("\n\nIntroduzca el nombre del elemento que desea eliminar: ")
                if elemento not in component.access():
                    limpiar_pantalla()
                    print("Este elemento no existe en la carpeta. Inténtelo de nuevo. Asegúrese de incluir Archivo, Carpeta o Enlace en el nombre.")
                    input("Pulse enter para continuar.")
                    limpiar_pantalla()
                else:
                    break
            for child in component._children:
                if child.get_name() == elemento:
                    elemento = child
                    break
            component.remove(elemento)
            limpiar_pantalla()
            print("Elemento eliminado correctamente.")
            input("Pulse enter para continuar.")

        elif opcion == "6":
            if component._parent == None:
                print("Saliendo...")
                input("Pulse enter para continuar.")
                break
            else:
                component = component._parent

        else:
            print("Opción no válida. Inténtelo de nuevo.")
            input("Pulse enter para continuar.")
```

#### Archivo `proxy.py`
```
from subject import Subject
from real_subject import RealSubject


class Proxy(Subject):
    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject

    def request(self):
        if self.check_access():
            self._real_subject.request()
            self.log_access()
            return True
        return False

    def check_access(self) -> bool:
        print("Proxy: Checking access prior to firing a real request.")
        return True

    def log_access(self) -> None:
        print("Proxy: Logging the time of request.", end="")
```

#### Archivo `real_subject.py`
```
from log import log
from subject import Subject


class RealSubject(Subject):
    def __init__(self, nombre, apellido, dni) -> None:
        self._nombre = nombre
        self._apellido = apellido
        self._dni = dni

    @log('Patrones Estructurales/Ejercicio 2/accesos/registro_accesos.log')
    def request(self) -> None:
        '''
        Si el usuario hace una petición, se mostrará su nombre, apellido y dni.
        '''
        return [self._nombre, self._apellido, self._dni] 
```

#### Archivo `run.py`
```
from main import client_code
from carpeta import Carpeta


if __name__ == '__main__':
    client_code(Carpeta('root')) # Inicializamos el programa con una carpeta raíz
```

#### Archivo `subject.py`
```
from abc import ABC, abstractmethod


class Subject(ABC):
    @abstractmethod
    def request(self) -> None:
        pass
```

#### Archivo `tests.py`
```
import unittest
from unittest.mock import patch
from real_subject import RealSubject
from proxy import Proxy
from documento import Documento
from enlace import Enlace
from carpeta import Carpeta


class TestTuModulo(unittest.TestCase):

    def setUp(self):
        # Crea instancias necesarias para las pruebas
        self.real_subject = RealSubject("Nombre", "Apellido", "12345678Y")
        self.proxy = Proxy(self.real_subject)

    def test_proxy_request_without_access(self):
        # Prueba para el método request de Proxy sin acceso
        with patch.object(self.proxy, 'check_access', return_value=False):
            with patch("builtins.print") as mock_print:
                output = self.proxy.request()
                mock_print.assert_not_called()
                self.assertEqual(output, False)

    def test_documento_add_without_access(self):
        # Prueba para el método add de Documento sin acceso
        documento = Documento("Test", "Contenido", "Texto", 10, sensible=True)
        with patch("builtins.print") as mock_print:
            with patch("builtins.input", side_effect=["Nombre", "Apellido", "12345678Y"]):
                documento.add("Nuevo contenido")
                mock_print.assert_called_with("No puede modificar el documento si no ha registrado su acceso previamente.")
                self.assertEqual(documento._contenido, "Contenido")

    def test_enlace_access(self):
        # Prueba para el método access de Enlace
        enlace = Enlace("/ruta/al/enlace")
        self.assertEqual(enlace.access(), "/ruta/al/enlace")

    def test_carpeta_add(self):
        # Prueba para el método add de Carpeta
        carpeta = Carpeta("Carpeta")
        documento = Documento("Documento", "Contenido", "Texto", 10)
        carpeta.add(documento)
        self.assertIn(documento, carpeta._children)

    def test_carpeta_remove(self):
        # Prueba para el método remove de Carpeta
        carpeta = Carpeta("Carpeta")
        documento = Documento("Documento", "Contenido", "Texto", 10)
        carpeta.add(documento)
        carpeta.remove(documento)
        self.assertNotIn(documento, carpeta._children)

    def test_carpeta_access(self):
        # Prueba para el método access de Carpeta
        carpeta = Carpeta("Carpeta")
        documento = Documento("Documento", "Contenido", "Texto", 10)
        carpeta.add(documento)
        self.assertEqual(carpeta.access(), ["Archivo Documento"])


if __name__ == '__main__':
    unittest.main()
```
