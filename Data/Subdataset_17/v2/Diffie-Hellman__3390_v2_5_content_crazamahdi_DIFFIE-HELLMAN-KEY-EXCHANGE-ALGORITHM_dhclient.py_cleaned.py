import random
import socket
def generate_private_component(q):
    return random.randint(1, q - 1)
def calculate_public_component(a, private_component, q):
    return pow(a, private_component, q)
def main():
    host = 'localhost'
    port = int(input("Enter port: "))
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        q = int(s.recv(1024).decode())
        print("Prime:", q)
        s.send(b"Send primitive root")
        a = int(s.recv(1024).decode())
        print("Primitive root:", a)
        private_component = generate_private_component(q)
        print("Private component:", private_component)
        public_component = calculate_public_component(a, private_component, q)
        print("Public component:", public_component)
        s.send(str(public_component).encode())
        server_public_component = int(s.recv(1024).decode())
        print("Server public component:", server_public_component)
        shared_secret_key = pow(server_public_component, private_component, q)
        print("Secret key is", shared_secret_key)
if __name__ == "__main__":
    main()