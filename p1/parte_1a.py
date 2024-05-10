# Documentar y agregar comentarios al codigo

# Importar las bibliotecas necesarias para enviar el client stub
# Completar
import Taxi_pb2 as pb

# Completar las elipsis (...)
solicitud_1 = pb.Taxi(
    taxi_id=777,
    conductor_id='Sist_dist',
    pasajero_id=['62732','50348','12345'],  # ['Codigo_UPB', 'Codigo_UPB+10', 'Codigo_UPB+20']
    costo_estimado =  20.0
)

# Imprimir el mensaje de solicitud:
print("Formato de solicitud:\n",solicitud_1)

#serialize y parse