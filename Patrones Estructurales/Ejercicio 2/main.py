from abstract_factory import AbstractFactory
import pandas as pd

# ¿Por qué empleamos el patrón Abstract Factory para este ejercicio?
# El patrón Abstract Factory se puede utilizar en este escenario para proporcionar una 
# estructura flexible y escalable para la generación de análisis y representaciones de datos. 
# Dado que se requieren diferentes tipos de análisis y representaciones, el patrón Abstract 
# Factory puede ayudar a crear familias de objetos relacionados sin especificar sus clases 
# concretas.
# Al utilizar el patrón Abstract Factory en este caso, puedes modularizar el proceso de 
# generación de análisis y representaciones, lo que facilita la incorporación de nuevos 
# tipos de análisis o representaciones en el futuro sin alterar el código existente. Esto 
# mejora la mantenibilidad y la flexibilidad del programa en general.
# Además, dado que el programa necesita realizar múltiples tareas como la lectura de datos, 
# el modelado de datos y la generación de diferentes tipos de análisis y representaciones, 
# el uso del patrón Abstract Factory puede ayudar a mantener una estructura clara y organizada 
# en el código, lo que facilita su comprensión y mantenimiento a largo plazo.

def client_code(factory: AbstractFactory, media = False, mediana = False, moda = False, histograma = False, diagrama_barras = False) -> None:

    # Cargamos los datos del csv en la carpeta data
    data = pd.read_csv('Patrones Creacionales/Ejercicio 1/data/data_limpio.csv', sep=';', encoding='ISO-8859-1')

    # Volvemos a convertir las columnas FECHA y FECHA-FIN a tipo datetime
    data['FECHA'] = pd.to_datetime(data['FECHA'], errors='coerce')
    data['FECHA-FIN'] = pd.to_datetime(data['FECHA-FIN'], errors='coerce')

    # Porqué vuelvo a hacer transformación de datos?
    # Los archivos CSV, como formato de almacenamiento de datos, no incluyen información 
    # sobre el tipo de datos de cada columna. Cuando guardas un DataFrame en un archivo CSV, 
    # los datos se guardan sin la información de los tipos de datos, lo que significa que 
    # cuando vuelves a cargar el DataFrame, el programa debe inferir los tipos de datos en 
    # función de los datos almacenados en el CSV.

    columna = 'FECHA' # Columna que queremos analizar

    analisis_estadistico = factory.crear_analisis_estadistico()
    visualizacon_graficas = factory.crear_graficas()

    if visualizacon_graficas is None:
        if media:
            print(f"\nMedia: \n{analisis_estadistico.calcular_media(data, columna)}")
        elif mediana:
            print(f"\nMediana: \n{analisis_estadistico.calcular_mediana(data, columna)}")
        elif moda:
            print(f"\nModa: \n{analisis_estadistico.calcular_moda(data, columna)}")
        else:
            pass

    elif analisis_estadistico is None:
        if histograma:
            visualizacon_graficas.mostrar_histograma(data, columna)
        elif diagrama_barras:
            visualizacon_graficas.mostrar_diagrama_barras(data, columna)
        else:
            pass
    else:
        pass