import socket
def powmod(base, exponent, modulus):
    result = 1
    while exponent > 0:
        result = (result * base) % modulus
        exponent -= 1
    return result
def initialize_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 1024
    server_socket.bind((host, port))
    print(f"Server will start on host: {host}\n")
    print("Server has successfully bound to host and port")
    print("Server is waiting for a connection...\n")
    server_socket.listen(1)
    return server_socket
def handle_client_connection(conn):
    private_key = int(input("Enter server private key: "))
    base = 17
    modulus = 23
    server_message = str(powmod(base, private_key, modulus))
    conn.send(server_message.encode())
    print("Message has been sent\n")
    client_message = conn.recv(1024).decode()
    print(f"Client: {client_message}")
    client_message_int = int(client_message)
    shared_secret = powmod(client_message_int, private_key, modulus)
    print(f"Shared secret key: {shared_secret}")
def start_server():
    server_socket = initialize_server()
    conn, addr = server_socket.accept()
    print(f"{addr} is connected to the server and is now online...\n")
    handle_client_connection(conn)
if __name__ == "__main__":
    start_server()