import socket
import sys
if len(sys.argv) < 2:
    print("Usage: python udp_server.py <UDP_PORT>")
    sys.exit(1)
UDP_PORT = int(sys.argv[1])
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind(("160.39.231.6", UDP_PORT))
print(f"UDP server is running on {UDP_PORT}")
while True:
    data, addr = udp_socket.recvfrom(1024)
    print(f"Received message from {addr}: {data.decode('utf-8')}")