import requests
import pymongo
import schedule
import time

# Conexión a MongoDB
client = pymongo.MongoClient("mongodb://admin:admin@localhost:27017/")
db = client['valenbici']
collection = db['sample_table']

# API URL para obtener datos de muestra
api_url = 'https://valencia.opendatasoft.com/api/explore/v2.1/catalog/datasets/valenbisi-disponibilitat-valenbisi-dsiponibilidad/records?limit=20'

def update_data():
    try:
        # Realizar solicitud HTTP a la API
        response = requests.get(api_url)

        # Verificar si la solicitud fue exitosa (código 200)
        if response.status_code == 200:
            # Obtener datos JSON de la respuesta
            data = response.json()

            # Insertar solo registros que no existen en la base de datos
            for record in data['records']:
                if collection.count_documents({'_id': record['_id']}) == 0:
                    collection.insert_one(record)
                    print(f"Nuevo registro insertado en {time.ctime()}")

        else:
            print(f"Error al obtener datos: {response.status_code}")

    except Exception as e:
        print(f"Error: {e}")

# Programar la ejecución cada 5 minutos
schedule.every(5).minutes.do(update_data)

# Ejecutar el programa en un bucle infinito
while True:
    schedule.run_pending()
    time.sleep(1)
