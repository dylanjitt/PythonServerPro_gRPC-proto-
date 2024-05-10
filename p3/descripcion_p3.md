# **Parte 3**
## **Respuesta del Servidor e Implementación de Funcionalidades Adicionales**

### Introducción

En esta sección, se analizarán los mensajes de respuesta del servidor y se implementarán funcionalidades adicionales para el manejo eficiente de solicitudes y validación de datos en un sistema de servicios de transporte usando gRPC. 

### 1\. Implementación de la Clase y Funciones del Servidor

Se dispone del archivo `server.py`, el cual requiere ser completado y configurado para que el servidor funcione sin errores. Este archivo implementa las funcionalidades del servidor en el sistema de servicios de transporte utilizando gRPC.

#### Desarrollo

-   **Definición de Función de Identificación**: 
La respuesta al mensaje inicial de solicitud consiste en enviar un ID unico como respuesta. Esto puede ser implementado por ejemplo via el método `uuid4` para generar un identificador único (`ride_id`) para cada viaje. Implementar esta funcionalidad e integrarlo a server.py. Este identificador rastrea y gestiona los viajes de forma única a lo largo de la solicitud del cliente.
    
-   **Completar la Clase `Viaje`**:
    
    -   Extender `rpc.Viaje_rpcServicer` en la clase `Viaje`. Esta extensión integra las funcionalidades del servicio de viajes con la infraestructura gRPC.
    -   Completar el método `Start` dentro de esta clase, que se encargará de:
        -   Asignar el `ride_id` a cada solicitud de viaje, utilizando el identificador generado por la función `uuid4`.
        -  Inicialmente asumir que el costo nominal de cada viaje es de $mod (C_{UPB},100)$ . Donde $C_{UPB}$ es su codigo de estudiante. Calcular el costo del viaje basado en el tipo de viaje especificado en el mensaje del cliente:
            -   **Tipo POOL**: Dividir el costo estimado del viaje entre el número de pasajeros indicados en la solicitud.
            -   **Tipo PREMIUM**: Incrementar el costo estimado en un 25%, reflejando un servicio de mayor calidad.

-   **Configuración del Servidor**:
    
    -   Ajustar el servidor según las especificaciones  del archivo `config.py`. Este archivo contiene parámetros que afectan la operación del servidor, como puertos y configuraciones de protocolo.
    -   Habilitar `grpc_reflection.v1alpha` en el servidor. La reflexión es una característica de grpc que permite a los clientes descubrir los servicios activos en un servidor gRPC, así como los métodos y tipos de mensajes asociados. Esto facilita la interoperabilidad y el mantenimiento del sistema.

### 2\. Ejecución y Monitoreo del Servidor

#### Inicio del Servidor

-   **Configuración**: Establecer el puerto en el que el servidor estará activo. 
-   **Activación**: Ejecutar el script `server.py` desde una terminal, a este punto, el servidor se inicia sin errores y quede en espera de solicitudes. 

#### Monitoreo de Servicios Disponibles

-   **Uso de grpcurl para Listar Servicios**:
    - **Preparación**: Abrir una nueva terminal.
    - **Ejecución**: Utilizar `grpcurl` con la opción `-list` para enumerar todos los servicios activos disponibles en el servidor. Este comando proporciona una visión general rápida de los servicios que el servidor está capacitado para manejar, puede realizar este paso agregando la opcion `-plaintext`, para evitar la necesidad de configurar TLS/SSL, lo cual simplifica las pruebas en entornos de desarrollo.
    - Documentar los pasos realizados y reportar la lista de los servicios activos. 
    

#### Detalle de los Mensajes

-   **Uso de grpcurl para Describir Estructuras de Mensajes**:
    -  Es posible obtener una descripción de las estructuras de los mensajes específicos utilizados por el servicio.
    - Para esto puede emplear `grpcurl` con la opción `-describe` para obtener información detallada sobre las estructuras de los mensajes. 


### 3\. Interacciones con el Servidor Utilizando grpcurl

#### Envío de Solicitudes al Servidor

-   **Especificar los Datos de Solicitud**:
    -   **Archivo de Datos**: Utilizar un archivo JSON, como `request.json`, que contenga los datos estructurados para la solicitud. Asegurarse de que el archivo esté correctamente formateado y accesible. Modificar este archivo si es necesario, anotando los cambios realizados. Documentar todos los pasos.
    -   **Comando de grpcurl**: Ejecutar `grpcurl` con la opción `-d @` para enviar los datos desde el archivo especificado a un servicio en el servidor. 

#### Documentación de la Respuesta del Servidor

-  Reportar la respuesta del servidor, especialmente al `id` que identifica de manera única cada transacción o viaje gestionado por el servidor. Este `id` es crítico para el seguimiento y la auditoría de las operaciones y si existe otra respuesta adicional. Deberia existir dos respuestas del servidor. 
-  Documentar la estructura y el contenido de la respuesta del servidor para asegurar que cumple con las expectativas y los requisitos del sistema.

#### Creación y Prueba de un Archivo JSON Personalizado

-   **Desarrollo del Archivo JSON**: Crear un archivo JSON adicional, por ejemplo, `custom_request.json`, que contenga datos personalizados del usuario para probar la flexibilidad y robustez del servidor.
-   **Prueba**: Enviar este nuevo archivo de solicitud al servidor usando el mismo método `grpcurl` para observar y documentar cómo el servidor maneja variaciones en los datos de entrada. 


### 4\. Envío de Solicitudes Múltiples

#### Configuración Inicial

-  Utilizar el archivo `request_seq.json`, este archivo contiene varias estructuras de datos JSON que representen distintas solicitudes a ser enviadas al servidor.

#### Proceso de Envío de Solicitudes

-  Utilizar `grpcurl` para enviar cada una de las solicitudes contenidas en `request_seq.json` al servidor. Este proceso puede realizarse mediante un bucle en un script o manualmente para cada solicitud, dependiendo de la cantidad de datos y la necesidad de automatización.
        

#### Documentación de las Respuestas

-   **Observación y Registro**:
    - Capturar y registrar la respuesta para cada solicitud enviada, prestar atención a la respuesta a cada mensaje, ej. el `id` de la respuesta
    - Guardar las respuestas en un formato estructurado, como un archivo de texto o un documento de registro, incluyendo tanto la solicitud original como la respuesta del servidor y el `id` asociado.

#### Análisis y Verificación

-   Después de enviar todas las solicitudes y recopilar las respuestas, realizar un análisis para asegurarse de que todas las respuestas son coherentes con las expectativas y que todos los `id` son únicos y correctos.
-   Reportar en una tabla que resuma las solicitudes enviadas, las respuestas recibidas, y cualquier anomalía o error detectado durante el proceso. 


### 5\. Validación de Mensajes Entrantes y Pruebas con Datos No Válidos

#### Establecimiento de Funciones de Validación
-   Implementar una función de validación en el servidor que se ejecute al principio de cada método que procese solicitudes. Esta función debe asegurarse de que todos los campos necesarios, como `taxi_id` y `tipoViaje`, estén presentes y sean válidos antes de proceder con cualquier lógica adicional. 

#### Creación de Archivo de Validación

- Integrar las funciones de validacion en su proyecto.   Opcionalmente, es posible crear un archivo de script, por ejemplo, `validation.py`, que contenga todas las funciones de validación. Este archivo ayudará a mantener el código del servidor organizado.
-   Definir errores generales y específicos de validación dentro de este archivo. Estos errores deben ser claros y proporcionar suficiente información para que los desarrolladores puedan entender rápidamente qué validación falló.

#### Manejo de Errores de Validación

-   En caso de que una validación falle, registrar el error y responder al cliente con un mensaje de error apropiado. Utilizar los códigos de estado de gRPC, como `INVALID_ARGUMENT`, para indicar el tipo de error.
-   Levantar excepciones o retornar mensajes de error específicos que detallen qué campo no cumplió con los requisitos de validación. 

#### Pruebas de Validación

-   Probar la función de validación generando un archivo `invalid_request.json`, que debe contener varios (>5) escenarios de datos de entrada erróneos o mal formados. Este puede ser un archivo con todas las solicitudes o multiples archivos con una solicitud cada uno. 
-   Enviar las solicitudes del archivo `invalid_request.json` al servidor y observar cómo maneja estos casos. Registrar las respuestas y los errores generados por el servidor.

#### Documentación de Resultados

-   Documentar cada prueba realizada, incluyendo la solicitud enviada y la respuesta recibida del servidor. 
-   Evaluar la efectividad de las respuestas de error para determinar si proporcionan suficiente información para que un cliente corrija la solicitud.
