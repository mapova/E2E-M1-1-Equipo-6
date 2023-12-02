#Para llamar a la API primero importamos las bibliotecas requests y JSON para realizar solicitudes HTPP y analizar la respuesta json
# respectivamente. Luego, definimos la URL de la API y hacemos una solicitud GET utilizando la función requests.get(). 
# La respuesta se almacena en la variable response, y luego usamos la función json.loads() para analizar el contenido de la respuesta 
# en formato JSON. Finalmente, imprimimos el valor del chiste aleatorio utilizando la clave value del diccionario data.
# Para guardar el texto que hago del API pongo:

import requests 
import json
import pandas as pd
import pymongo

url= 'https://valencia.opendatasoft.com/api/explore/v2.1/catalog/datasets/valenbisi-disponibilitat-valenbisi-dsiponibilidad/records?limit=20'

response = requests.get(url)

if response.status_code == 200:  # Verificar si la solicitud fue exitosa (código 200)
    data = response.json()  # Obtener los datos en formato JSON
    # Trabajar con los datos obtenidos de la API
    print(data)
    results = data['results'] 
    # Establecer conexión con la base de datos MongoDB
    client = pymongo.MongoClient('mongodb://localhost:27017/')  # URL de conexión de tu base de datos
    db = client['nombre_de_tu_base_de_datos']  # Selecciona la base de datos
    collection = db['nombre_de_tu_coleccion']  # Selecciona la colección
    
    # Insertar los datos en la colección de MongoDB
    collection.insert_many(results)
    print("Datos insertados en MongoDB correctamente.")
else:
    print('Hubo un problema con la solicitud. Código de estado:', response.status_code)












'''
   # df = pd.DataFrame([result['address','number','open','available','free','total','ticket','update_at','geo_schape','geo_point_2d'] for result in results])  # Extraer los datos relevantes de lso registros y convertir los datos a DataFrame
    df = pd.DataFrame(data)
   '''


   #Configurar Pandas para mostrar todas las columnas y filas sin truncar
'''
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    # Mostrar todas las columnas del DataFrame
    print("Todas las columnas del DataFrame:")
    print(df)
    print("DataFrame creado con éxito:") #muestro el DataFrame
    print(df.head())  # Mostrar las primeras filas del DataFrame

else:
    print('Hubo un problema con la solicitud. Código de estado:', response.status_code)

'''



 