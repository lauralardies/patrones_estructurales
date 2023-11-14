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
        with open("Patrones creacionales/Ejercicio 2/data/pizza_cliente.csv", "a", newline="") as archivo:
            writer = csv.writer(archivo)
            writer.writerow(self.partes)
    
    def ultima_fila(self):
        '''
        Con este método obtenemos la última fila del archivo csv
        '''
        with open("Patrones creacionales/Ejercicio 2/data/pizza_cliente.csv", "r") as archivo:
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
        f = open('Patrones creacionales/Ejercicio 2/data/pizza_cliente.csv', "r+")
        lines = f.readlines()
        lines.pop()
        f = open('Patrones creacionales/Ejercicio 2/data/pizza_cliente.csv', "w+")
        f.writelines(lines)