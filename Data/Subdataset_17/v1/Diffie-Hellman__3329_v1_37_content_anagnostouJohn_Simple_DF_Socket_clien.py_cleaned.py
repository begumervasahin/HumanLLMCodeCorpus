
import socket
import json
from diffiehellman.diffiehellman import DiffieHellman
IP_ADDRESS = '192.168.168.184'
PORT = 8201
TIMEOUT = 5
BUFFER_SIZE = 100
def connect_to_server(ip_address, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.settimeout(TIMEOUT)
    server.connect((ip_address, port))
    return server
def send_public_key(server, public_key):
    data = json.dumps({"bob": public_key}).encode("utf-8")
    server.send(data)
def receive_data(server):
    total_data = ""
    while True:
        try:
            message = server.recv(BUFFER_SIZE).decode("utf-8")
            if message:
                total_data += message
            else:
                break
        except socket.error as ex:
            print(ex)
            break
    return total_data
def main():
    server = connect_to_server(IP_ADDRESS, PORT)
    bob = DiffieHellman()
    bob.generate_public_key()
    send_public_key(server, bob.public_key)
    total_data = receive_data(server)
    received_data = json.loads(total_data)
    bob.generate_shared_secret(received_data["alice"], echo_return_key=True)
    print(bob.shared_key)
    server.close()
if __name__ == '__main__':
    main()