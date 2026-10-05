import socket
import sys
if len(sys.argv) < 2:
    print("Usage: python udp_server.py <UDP_PORT>")
    sys.exit(1)
UDP_PORT = int(sys.argv[1])
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ("160.39.231.6", UDP_PORT)
udp_socket.bind(server_address)
print(f"UDP server is running on port {UDP_PORT}")
while True:
    data, client_address = udp_socket.recvfrom(1024)
    message = data.decode('utf-8')
    print(f"Received message from {client_address}: {message}")