import socket
import subprocess
import optparse
mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

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
    mi_socket.connect( (host,port) )
    mi_socket.listen(5)

def ejecutar_comando(command):
    return subprocess.check_output( command, shell=True)

options = get_arguments()
start_server(options.host,options.port)


conexion, addr = mi_socket.accept()
print("[+] nueva conexion establecida")
print(addr)
while True:
    




    inp = input("comando -> ")
    call = subprocess.call(inp)
    send_call = call.to_bytes(2, 'little')
    conexion.send(send_call)
    
conexion.close()
