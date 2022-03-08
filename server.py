#cd C:\Users\Zino243\Documents\python\autoserver

import socket
import subprocess

mi_socket = socket.socket()
#host = '192.168.0.18'
#host = '95.63.226.100'
host = '0.0.0.0'
port = '5555'

def start_server(host, port):
    print("[+] iniciando servidor")
    port = (int(port))
    mi_socket.bind( (host,port) )
    mi_socket.listen(5)

start_server(host, port)

while True:
    #conexion me da todos los datos de la conexion
    #addr la ip y por que puerto se conecta el cliente
    conexion, addr = mi_socket.accept()
    # print("var conexion {}".format(conexion)) #simplemente para ver los datos que entran
    print("var addr {}".format(addr)) #simplemente para ver los datos que entran
    call = conexion.recv(1024) #recibir la informacion desde el cliente
    call = call.decode('utf-8') #decode en el mismo formato en el que encode del cliente
    #print(call)

    if call == "s":
        subprocess.call(["C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe", ". \"./init.ps1\";", "&hello"])
        #subprocess.call(["C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe", ". \"./SamplePowershell\";", "&hello"])

    #call = subprocess.call("echo hola mundo")
    #conexion.send(call)
