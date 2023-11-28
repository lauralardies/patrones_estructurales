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
                    tam = float(input("Introduzca el tamaño del documento: "))
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
            else:
                limpiar_pantalla()
                print("Contenido:\n")
                print(elemento.access())
                input("\nPulse enter para continuar.")

        elif opcion == "5":
            while True:
                # Mostramos el contenido de la carpeta
                print(f"Contenido {component.get_name()}: ")
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