import socket
import json
from diffiehellman.diffiehellman import DiffieHellman
def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.settimeout(5)
    IP_address = '192.168.168.184'
    Port = 8201
    try:
        server.connect((IP_address, Port))
    except socket.error as ex:
        print("Error connecting to the server:", ex)
        return
    bob = DiffieHellman()
    bob.generate_public_key()
    bob_public_key = bob.public_key
    message = {"bob": bob_public_key}
    server.send(json.dumps(message).encode("utf-8"))
    total_data = ""
    while True:
        try:
            message = server.recv(100)
            if not message:
                break
            total_data += message.decode("utf-8")
        except socket.error as ex:
            print("Error receiving message from the server:", ex)
            break
    alice_public_key = json.loads(total_data)["alice"]
    bob.generate_shared_secret(alice_public_key, echo_return_key=True)
    print("Shared Secret Key:", bob.shared_key)
    server.close()
if __name__ == "__main__":
    main()