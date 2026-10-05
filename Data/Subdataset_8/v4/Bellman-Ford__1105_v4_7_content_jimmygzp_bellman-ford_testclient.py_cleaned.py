import socket
send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
send_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
send_socket.bind(("", 8179))
destination_address = ('localhost', 8181)
send_socket.sendto(b"Hello", destination_address)
response_data, _ = send_socket.recvfrom(4096)
print(response_data.decode())
send_socket.close()