from os import environ
## LLenar los datos faltantes
## puerto_server = 2024 + mod(codigo_upb,10) 
puerto_server = 2026
port = int(environ.get('PORT', puerto_server))
host = environ.get('HOST', 'localhost')
