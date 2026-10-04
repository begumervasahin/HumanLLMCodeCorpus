import socket
def create_socket():
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def connect_socket(sock, ip, port):
    sock.connect((ip, port))
    print(f'Connected to {ip} on port {port}')
def send_message(sock, message):
    sock.sendall(message.encode())
def receive_message(sock, buffer_size):
    data = sock.recv(buffer_size)
    return data.decode()
def main():
    TCP_IP = '52.43.121.77'
    TCP_PORT = 2329
    BUFFER_SIZE = 1024
    MESSAGE = "Hello, World!"
    sock = create_socket()
    connect_socket(sock, TCP_IP, TCP_PORT)
    send_message(sock, MESSAGE)
    data = receive_message(sock, BUFFER_SIZE)
    sock.close()
    print("Received data:", data)
if __name__ == "__main__":
    main()