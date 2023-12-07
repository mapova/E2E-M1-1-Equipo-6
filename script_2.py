import requests
import pymongo
import time

#time.sleep(10)

# Conexión a MongoDB
client = pymongo.MongoClient("mongodb://admin:admin@mongo:27017/")
db = client['valenbici']
collection = db['sample_table']

# API URL para obtener datos de muestra
api_url = 'https://valencia.opendatasoft.com/api/explore/v2.1/catalog/datasets/valenbisi-disponibilitat-valenbisi-dsiponibilidad/records?limit=20'

# Intervalo de actualización (5 minutos = 300 segundos)
intervalo_actualizacion = 300

try:
    while True:
        # Realizar solicitud HTTP a la API
        response = requests.get(api_url)

        # Verificar si la solicitud fue exitosa (código 200)
        if response.status_code == 200:
            # Obtener datos JSON de la respuesta
            data = response.json()

        # Insertar cada documento en MongoDB
            for entry in data['results']:
                collection.insert_one(entry)

            # Imprimir mensaje en la consola
            print("Datos insertados correctamente. Próxima actualización en 5 minutos.")

        else:
            print(f"Error al obtener datos: {response.status_code}")

        # Esperar 5 minutos antes de la próxima actualización
        time.sleep(intervalo_actualizacion)

except KeyboardInterrupt:
    print("\nProceso interrumpido por el usuario.")
except Exception as e:
    print(f"Error: {e}")
finally:
    # Cerrar la conexión a MongoDB al finalizar el script
    client.close()
