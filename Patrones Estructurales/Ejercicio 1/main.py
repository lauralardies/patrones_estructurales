from director import Director
from pizza_builder import PizzaBuilder
from composite import *
from config import limpiar_pantalla

# ¿Por qué empleamos el patrón Builder para este ejercicio?
# En el escenario descrito, el patrón Builder sería adecuado para la implementación 
# del sistema de construcción de pizzas personalizadas. Dado que hay múltiples componentes 
# y pasos involucrados en la creación de una pizza personalizada, el patrón Builder 
# puede facilitar la construcción paso a paso de objetos complejos, como una pizza 
# con todas sus características específicas.
# Aquí hay algunas razones por las cuales sería útil emplear el patrón Builder en 
# este ejercicio:
# 1. Construcción paso a paso: El patrón Builder permite a los clientes construir su pizza 
#    paso a paso, seleccionando cada componente a lo largo del camino.
# 2. Validación de selecciones: El Builder puede asegurar que cada elección sea validada y 
#    compatible con las selecciones previas del cliente, evitando combinaciones inválidas.
# 3. Flexibilidad y expansión: El patrón Builder facilita la incorporación de nuevas 
#    características o componentes en la construcción de la pizza sin modificar el código 
#    existente, lo que garantiza la flexibilidad del sistema.
# 4. Estructura clara y modular: El uso del patrón Builder puede proporcionar una 
#    estructura clara y modular para la construcción de pizzas personalizadas, lo que 
#    facilita el mantenimiento y la comprensión del código a largo plazo.
# 5. Recomendaciones dinámicas: El sistema de recomendaciones basado en las elecciones 
#    previas del cliente puede integrarse fácilmente con el patrón Builder para sugerir 
#    ingredientes, técnicas de cocción y maridajes adecuados.
# 6. Separación de preocupaciones: El patrón Builder permite separar la lógica de construcción 
#    de pizza del código de la interfaz de usuario, lo que mejora la claridad y la 
#    mantenibilidad del código.
# En resumen, el patrón Builder sería útil en este escenario para facilitar la creación de 
# pizzas personalizadas, asegurando la validación de selecciones, la flexibilidad y la 
# modularidad del sistema, así como la implementación de recomendaciones dinámicas basadas 
# en las elecciones de los clientes.

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
                        print('¡Gracias por tu compra!')
                        input('Presiona cualquier tecla para continuar...')
                        break

            else:
                print('Opción no válida. Inténtalo de nuevo.\nDebes seleccionar 1 o 2')
                input('Presiona cualquier tecla para continuar...')

        elif opcion == '2': # Si elegimos crear pizza personalizada
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