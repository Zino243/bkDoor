import socket
import subprocess

mi_socket = socket.socket()
mi_socket.connect( ('localhost', 8000) )


respuesta = mi_socket.recv(1024)
print(str(respuesta.decode()))
mi_socket.close()
