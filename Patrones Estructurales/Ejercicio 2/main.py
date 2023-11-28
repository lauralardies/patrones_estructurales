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
                    tam = float(input("Introduzca el tamaño del documento: "))
                    break
                except ValueError:
                    limpiar_pantalla()
                    print("Tamaño no válido. Inténtelo de nuevo. Asegúrese de introducir solo números. En caso de haber decimal, introduczca un punto en vez de una coma.")
                    input("Pulse enter para continuar.")
                    continue
            limpiar_pantalla()
            component.add(Documento(nombre, contenido, tipo, tam))
            limpiar_pantalla()
            print("Documento creado correctamente.")
            input("Pulse enter para continuar.")
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