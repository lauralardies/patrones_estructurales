from composite import *

def client_code(component: Component) -> None:
    while True:
        limpiar_pantalla()
        # Mostramos el contenido de la carpeta
        print(f"Contenido {component.get_name()}: ")
        contenido = component.access()
        for c in contenido:
            print(f"- {c}")
        print("\n\n¿Qué desea hacer?")
        print("1. Crear carpeta")
        print("2. Crear documento")
        print("3. Crear enlace")
        print("5. Acceder")
        print("6. Salir")
        opcion = input("Introduzca el número de la opción que desee: ")
        limpiar_pantalla()
        if opcion == "1":
            nombre = input("Introduzca el nombre de la carpeta: ")
            component.add(Carpeta(nombre))
            limpiar_pantalla()
            print("Carpeta creada correctamente.")
            input("Pulse enter para continuar.")
        elif opcion == "2":
            pass
        elif opcion == "3":
            pass
        elif opcion == "4":
            pass
        elif opcion == "5":
            pass
        elif opcion == "6":
            print("Saliendo...")
            input("Pulse enter para continuar.")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")
            input("Pulse enter para continuar.")