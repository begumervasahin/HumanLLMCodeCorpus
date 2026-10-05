import random
import math
import socket
def is_prime(num):
    if num < 2:
        return False
    for div in range(2, int(math.sqrt(num)) + 1):
        if num % div == 0:
            return False
    return True
def generate_primes(limit):
    primes = []
    for num in range(100, limit):
        if is_prime(num):
            primes.append(num)
    return primes
def find_primitive_roots(modulo):
    roots = []
    required_set = set(num for num in range(1, modulo) if math.gcd(num, modulo) == 1)
    for g in range(1, modulo):
        actual_set = set(pow(g, power) % modulo for power in range(1, modulo))
        if required_set == actual_set:
            roots.append(g)
    return roots
def generate_private_component(modulo):
    return random.randint(0, modulo - 1)
def generate_public_component(modulo, primitive_root, private_component):
    return pow(primitive_root, private_component, modulo)
def main():
    host = 'localhost'
    port = int(input("Enter port: "))
    primes_list = generate_primes(500)
    q = random.choice(primes_list)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Waiting for connection...")
    client_socket, client_addr = server_socket.accept()
    print("Connected to client:", client_addr)
    print("Prime number (q) is:", q)
    client_socket.send(str(q).encode())
    client_msg = client_socket.recv(1024).decode()
    print("Received message from client:", client_msg)
    primitive_roots_q = find_primitive_roots(q)
    alpha = random.choice(primitive_roots_q)
    print("Primitive root (alpha) is:", alpha)
    client_socket.send(str(alpha).encode())
    x1 = generate_private_component(q)
    print("Private key component (x1) is:", x1)
    y1 = generate_public_component(q, alpha, x1)
    print("Public key component (y1) is:", y1)
    client_socket.send(str(y1).encode())
    yc = int(client_socket.recv(1024).decode())
    print("Client's public key component (yc) is:", yc)
    k = pow(yc, x1, q)
    print("Secret key (k) is:", k)
    client_socket.close()
    server_socket.close()
if __name__ == "__main__":
    main()