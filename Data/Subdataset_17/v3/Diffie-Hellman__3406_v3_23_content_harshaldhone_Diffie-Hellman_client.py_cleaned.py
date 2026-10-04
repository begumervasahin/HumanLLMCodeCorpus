import socket
def powmod(base, exponent, modulus):
    result = 1
    while exponent > 0:
        result = (result * base) % modulus
        exponent -= 1
    return result % modulus
def establish_connection():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = input("Please enter the host name of the server: ")
    port = 1024
    client_socket.connect((host, port))
    print("Connected to the server\n")
    return client_socket
def get_private_key():
    return int(input("Enter client private key: "))
def main():
    client_socket = establish_connection()
    private_key = get_private_key()
    base = 17
    modulus = 23
    client_message = str(powmod(base, private_key, modulus))
    server_message = client_socket.recv(1024).decode()
    print("Server:", server_message)
    client_socket.send(client_message.encode())
    print("Message has been sent\n")
    server_message_int = int(server_message)
    shared_secret = powmod(server_message_int, private_key, modulus)
    print("Shared secret key:", shared_secret)
if __name__ == "__main__":
    main()