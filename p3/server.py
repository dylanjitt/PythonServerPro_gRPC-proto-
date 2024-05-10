from concurrent.futures import ThreadPoolExecutor
from grpc_reflection.v1alpha import reflection
import grpc
import log
import Taxi2_pb2 as pb
import Taxi2_pb2_grpc as rpc
import uuid

import validation

def gen_id():
    # el id_gen es un identificador unico
    # se encuentra en formato hex.
    # puede hacer uso de la biblioteca uuid
    id_servicio = str(uuid.uuid4().int)[:8] # Tomar los primeros 10 dígitos
    return id_servicio


def costoViaje(typeRide,nPasajeros):
    costoNominal=62732%100
    costoFinal=0
    if typeRide==pb.TipoViaje.REGULAR:
        costoFinal=costoNominal
    elif typeRide==pb.TipoViaje.POOL:
        costoFinal=costoNominal/nPasajeros
    elif typeRide==pb.TipoViaje.PREMIUM:
        costoFinal=(costoNominal*0.25)+costoNominal
    return int(costoFinal)

class Viaje(rpc.Viaje_rpcServicer):
    def Start(self, request, context):
        # log la solicitud actual
        if validation.validate_start_request(request)==True:
            log.info('viaje: ', request)

            #generar un nuevo id para el ride
            # obtener este id de la funcion generada anteriormente

            id_viaje = gen_id()
            # obtener el costo estimado del viaje 
            nPasajeros=len(request.pasajero_id)
            costo_viaje = costoViaje(request.tipoViaje,nPasajeros)

            # generar la respuesta en base a la estructura indicada 
            # en el .proto file.
            respuesta = pb.StartResponse(
                id=id_viaje,
                costo_cliente=costo_viaje
            )
            return respuesta


if  __name__ == '__main__':
    import config
    # crear una nueva instancia de un servidor gRPC
    # utilizar un ThreadPoolExecutor para manejar las solicitudes entrantes
    server = grpc.server(ThreadPoolExecutor())
    # registrar un servicio gRPC en un servidor gRPC
    rpc.add_Viaje_rpcServicer_to_server(Viaje(), server)
    names = (
        # adicionar el nombre del servicio
        pb.DESCRIPTOR.services_by_name['Viaje_rpc'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(names, server)
    addr = f'[::]:{config.port}'
    server.add_insecure_port(addr)
    server.start()

    log.info('El servidor esta listo en el puerto%s', addr)
    server.wait_for_termination()
