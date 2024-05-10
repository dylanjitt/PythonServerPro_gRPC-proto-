#!/bin/bash

# Nombre del archivo JSON
JSON_FILE="request_seq.json"

# Iterar sobre cada objeto en el archivo JSON
for item in $(jq -c '.[]' "$JSON_FILE"); do
    # Crear un archivo temporal para almacenar el objeto actual
    TEMP_FILE=$(mktemp)

    # Escribir el objeto actual en el archivo temporal
    echo "$item" > "$TEMP_FILE"

    # Ejecutar el comando grpcurl con el objeto actual como entrada
    grpcurl -d @ -plaintext localhost:2026 Viaje_rpc.Start < "$TEMP_FILE"

    # Eliminar el archivo temporal
    rm "$TEMP_FILE"
done