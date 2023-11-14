from main import client_code
from concrete_analisis_factory import ConcreteAnalisisFactory
from concrete_graficas_factory import ConcreteGraficasFactory


if __name__ == "__main__":    
    
    print('Analizamos las activaciones por día.')

    # Sólo calculamos la media de las activaciones por día y sólo dibujamos el histograma
    client_code(ConcreteAnalisisFactory(), media = True)
    client_code(ConcreteGraficasFactory(), histograma = True)

    print("Las gráficas se han guardado en la carpeta graficas.")