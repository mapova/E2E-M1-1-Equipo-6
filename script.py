import requests
import pymongo

# Conexión a MongoDB
client = pymongo.MongoClient("mongodb://admin:admin@localhost:27017/")
db = client['valenbici']
collection = db['sample_table']

# API URL para obtener datos de muestra
api_url = 'https://valencia.opendatasoft.com/api/explore/v2.1/catalog/datasets/valenbisi-disponibilitat-valenbisi-dsiponibilidad/records?limit=20'

try:
    # Realizar solicitud HTTP a la API
    response = requests.get(api_url)

    # Verificar si la solicitud fue exitosa (código 200)
    if response.status_code == 200:
        # Obtener datos JSON de la respuesta
        data = response.json()

        # Actualizar la colección en MongoDB
        collection.insert_many(data['results'])

        print("Datos insertados correctamente.")

    else:
        print(f"Error al obtener datos: {response.status_code}")

except Exception as e:
    print(f"Error: {e}")

