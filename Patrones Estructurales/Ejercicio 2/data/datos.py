import pandas as pd

url = 'https://datos.madrid.es/egob/catalogo/212504-0-emergencias-activaciones.csv'

# Cargamos el fichero CSV en un dataframe leyendo desde la url
data = pd.read_csv(url, sep=';', encoding='ISO-8859-1')

# Mostramos las 5 primeras filas
print('Dataframe original, de tamaño {}:'.format(data.shape)) # Comprobamos el tamaño del dataset --> (15, 30)
print(data.head()) # De esta forma podemos ver la estructura de los datos

# ----------------------------------------------------------
# Limpieza de datos
# ----------------------------------------------------------

print(data.isnull().sum()) # Comprobamos el número de valores nulos por columna

# Eliminamos las filas que tienen valores nulos
columnas_basura = ['PRECIO', 'DIAS-EXCLUIDOS', 'HORA', 'DESCRIPCION', 'AUDIENCIA', 'Unnamed: 29']
data_limpio = data.drop(columns=columnas_basura)

print('\nDataframe limpio, de tamaño {}:'.format(data_limpio.shape))
print(data_limpio.head())

# No aplicamos dropna() para eliminar filas con valores nulos porque de lo contrario,
# el dataframe se queda prácticamente vacío

# ----------------------------------------------------------
# Transformación de datos
# ----------------------------------------------------------

print(data_limpio.dtypes) # Comprobamos los tipos de datos de cada columna
# FECHA: object --> datetime64[ns]

# Convertimos las columnas FECHA y FECHA-FIN a tipo datetime
data_limpio['FECHA'] = pd.to_datetime(data_limpio['FECHA'], errors='coerce')
data_limpio['FECHA-FIN'] = pd.to_datetime(data_limpio['FECHA-FIN'], errors='coerce')

print(data_limpio.dtypes) # Comprobamos los tipos de datos de cada columna

# Guardamos el dataframe limpio en un fichero CSV dentro de la carpeta data
data_limpio.to_csv('Patrones Creacionales/Ejercicio 1/data/data_limpio.csv', sep=';', encoding='ISO-8859-1')