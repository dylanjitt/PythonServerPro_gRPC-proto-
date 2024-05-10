import json
import Taxi_pb2 as pb

# Nombre del archivo JSON
archivo_json = "sample_request_data.json"

# Leer el archivo JSON
with open(archivo_json, "r") as archivo:
    data = json.load(archivo)

# Iterar sobre cada entrada en el JSON
for idx in data["taxi_id"]:
    # Crear una instancia de mensaje Taxi
    mensaje_taxi = pb.Taxi()

    # Asignar valores a los campos del mensaje Taxi
    mensaje_taxi.taxi_id = data["taxi_id"][idx]
    mensaje_taxi.conductor_id = data["conductor_id"][idx]
    mensaje_taxi.pasajero_id.extend(data["pasajero_id"][idx].split(", "))
    mensaje_taxi.costo_estimado = data["costo_estimado"][idx]

    # Serializar el mensaje
    mensaje_serializado = mensaje_taxi.SerializeToString()

    # Mostrar la salida binaria (opcional)
    print(mensaje_taxi)
    print("Salida binaria del mensaje:")
    print(mensaje_serializado)

    # Guardar la salida binaria en un archivo .bin
    with open("taxi.bin", "ab") as archivo_binario:
        archivo_binario.write(mensaje_serializado)

print("Serialización completa. Los mensajes se han guardado en taxi.bin.")
