import socket
import json
from diffiehellman.diffiehellman import DiffieHellman
def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.settimeout(5)
    server_ip = '192.168.168.184'
    server_port = 8201
    try:
        server_socket.connect((server_ip, server_port))
    except socket.error as e:
        print("Error connecting to the server:", e)
        return
    bob = DiffieHellman()
    bob.generate_public_key()
    message = {"bob": bob.public_key}
    server_socket.send(json.dumps(message).encode("utf-8"))
    total_data = ""
    while True:
        try:
            received_data = server_socket.recv(100)
            if not received_data:
                break
            total_data += received_data.decode("utf-8")
        except socket.error as e:
            print("Error receiving message from the server:", e)
            break
    alice_public_key = json.loads(total_data)["alice"]
    bob.generate_shared_secret(alice_public_key, echo_return_key=True)
    print("Shared Secret Key:", bob.shared_key)
    server_socket.close()
if __name__ == "__main__":
    main()