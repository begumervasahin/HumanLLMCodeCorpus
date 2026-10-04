import os
import json
from socket import *
import random
def get_random_prime():
    PRIMES = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
        53, 59, 61, 67, 71, 73, 79, 83, 89, 97
    ]
    return random.choice(PRIMES)
def main():
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server_socket.bind(('', 2222))
    server_socket.listen(2)
    private_key = random.randint(1, 35535)
    prime = get_random_prime()
    base = random.randint(1, 35535)
    params = {'p': prime, 'base': base}
    print(f"Parameters chosen: prime={prime}, base={base}, private_key={private_key}")
    connection, address = server_socket.accept()
    print(f"Connection established with {address}")
    while True:
        message = connection.recv(1024).decode('utf-8')
        if "NEGOTIATION" in message:
            connection.send(json.dumps(params).encode('utf-8'))
            print("Sent base and prime number to the client.")
            break
    A = pow(base, private_key, prime)
    message = connection.recv(1024).decode('utf-8')
    client_data = json.loads(message)
    B = client_data['B']
    shared_secret = pow(B, private_key, prime)
    print("Computed shared secret.")
    connection.send(json.dumps({'A': A}).encode('utf-8'))
    print(f"Sent public value A to the client: {A}")
    print(f"The shared secret is: {shared_secret}")
    connection.close()
    server_socket.close()
    print("Connection closed.")
if __name__ == "__main__":
    main()