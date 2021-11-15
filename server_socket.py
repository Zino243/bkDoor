import socket
import subprocess
import optparse
mi_socket = socket.socket()

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-k", "--host", dest = "host", help= "ip del host de servidor")
    parser.add_option("-p", "--port", dest = "port", help = "puerto de escucha del servidor")
    (options, arguments) = parser.parse_args()
    if not options.host:
        parser.error("[-] Por favor indica un host, usa --help para mas informacion")
    elif not options.port:
        parser.error("[-] Por favor indica un puerto, usa --help para mas informacion")
    return options
def start_server(host, port):
    print("[+] iniciando servidor")
    port = (int(port))
    mi_socket.bind( (host,port) )
    mi_socket.listen(5)

options = get_arguments()
start_server(options.host,options.port)


while True:
    conexion, addr = mi_socket.accept()
    print("[+] nueva conexion establecida")
    print(addr)
    call = subprocess.call("ipconfig")
    conexion.send(call)
    conexion.close()