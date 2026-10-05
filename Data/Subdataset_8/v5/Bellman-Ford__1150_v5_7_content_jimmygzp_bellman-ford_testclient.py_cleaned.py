import socket
def create_udp_socket():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return udp_socket
def set_socket_options(udp_socket):
    udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
def bind_socket(udp_socket, host, port):
    udp_socket.bind((host, port))
def send_message(udp_socket, message, destination_address):
    udp_socket.sendto(message.encode(), destination_address)
def receive_response(udp_socket, buffer_size):
    response_data, _ = udp_socket.recvfrom(buffer_size)
    return response_data.decode()
def close_socket(udp_socket):
    udp_socket.close()
def main():
    send_socket = create_udp_socket()
    set_socket_options(send_socket)
    bind_socket(send_socket, "", 8179)
    destination_address = ('localhost', 8181)
    send_message(send_socket, "Hello", destination_address)
    response_data = receive_response(send_socket, 4096)
    print(response_data)
    close_socket(send_socket)
if __name__ == "__main__":
    main()