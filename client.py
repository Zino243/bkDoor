import socket

mi_socket = socket.socket()
mi_socket.connect( ('95.63.226.100', 5555) )

i = True
def disconnect():
    print("se ha cerrado el programa")
    mi_socket.close()
    return i

#escribe lo que el servidor le mande al conectarse a tamaño de 1024bits o menor
#respuesta = mi_socket.recv(1024)
#print(str(respuesta))

while i:
    rec = input("abrir servidor? (s/n): ")
    print(rec)
    if rec == "s":
        rec = bytes(rec, 'utf-8')
        mi_socket.send(rec)
        print("solicitud enviada")
        i = False
        disconnect()
    elif rec == "n":
        i = False
        disconnect()
    else: print("no ha introducido correctamente")
