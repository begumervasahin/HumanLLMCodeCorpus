import random
import math
import socket
def generate_prime_numbers(limit):
    primes = []
    for num in range(100, limit):
        if is_prime(num):
            primes.append(num)
    return primes
def is_prime(num):
    if num < 2:
        return False
    for div in range(2, int(math.sqrt(num)) + 1):
        if num % div == 0:
            return False
    return True
def compute_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def find_primitive_roots(modulus):
    roots = []
    required_set = set(num for num in range(1, modulus) if compute_gcd(num, modulus) == 1)
    for g in range(1, modulus):
        actual_set = set(pow(g, power) % modulus for power in range(1, modulus))
        if required_set == actual_set:
            roots.append(g)
    return roots
def generate_private_component(modulus):
    return random.randint(0, modulus - 1)
def generate_public_component(modulus, primitive_root, private_component):
    return pow(primitive_root, private_component, modulus)
def main():
    host = 'localhost'
    port = int(input("Enter port: "))
    prime_limit = 500
    primes_list = generate_prime_numbers(prime_limit)
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
    private_key = generate_private_component(q)
    print("Private key component (x1) is:", private_key)
    public_key = generate_public_component(q, alpha, private_key)
    print("Public key component (y1) is:", public_key)
    client_socket.send(str(public_key).encode())
    client_public_key = int(client_socket.recv(1024).decode())
    print("Client's public key component (yc) is:", client_public_key)
    secret_key = pow(client_public_key, private_key, q)
    print("Secret key (k) is:", secret_key)
    client_socket.close()
    server_socket.close()
if __name__ == "__main__":
    main()