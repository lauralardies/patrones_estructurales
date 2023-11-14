from director import Director
from pizza_builder import PizzaBuilder
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
        # Primero pedimos crear la pizza
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