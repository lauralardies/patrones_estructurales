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