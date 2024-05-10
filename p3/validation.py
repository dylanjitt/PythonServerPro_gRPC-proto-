import Taxi2_pb2 as pb
import grpc
def validate_start_request(request):
    print(request.tipoViaje)
    pasa=True
    if not request.taxi_id:
        pasa=False
        raise ValueError(grpc.StatusCode.INVALID_ARGUMENT,": El campo 'taxi_id' es obligatorio.")
    if not request.conductor_id:
        pasa=False
        raise ValueError(grpc.StatusCode.INVALID_ARGUMENT,"El campo 'conductor_id' es obligatorio.")
    if not request.pasajero_id:
        pasa=False
        raise ValueError(grpc.StatusCode.INVALID_ARGUMENT,"El campo 'pasajero_id' es obligatorio.")
    if not request.tipoViaje:
        pasa=False
        raise ValueError(grpc.StatusCode.INVALID_ARGUMENT,"El campo 'tipoViaje' es obligatorio.")
    if not request.ubicacion.lat and not request.ubicacion.lng:
        pasa=False
        raise ValueError(grpc.StatusCode.INVALID_ARGUMENT,"El campo 'ubicacion' es obligatorio.")
    if not request.ubicacion.lat:
        pasa=False
        raise ValueError(grpc.StatusCode.INVALID_ARGUMENT,"El campo 'ubicacion.lat' es obligatorio.")
    if not request.ubicacion.lng:
        pasa=False
        raise ValueError(grpc.StatusCode.INVALID_ARGUMENT,"El campo 'ubicacion.lng' es obligatorio.")
    if not request.tiempo.seconds:
        pasa=False
        raise ValueError(grpc.StatusCode.INVALID_ARGUMENT,"El campo 'tiempo' es obligatorio.")
    return pasa


