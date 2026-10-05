import socket
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
udp_socket.bind(("localhost", 8179))
destination_address = ('localhost', 8181)
udp_socket.sendto(b"Hello", destination_address)
response_data, _ = udp_socket.recvfrom(4096)
print(response_data.decode())
udp_socket.close()