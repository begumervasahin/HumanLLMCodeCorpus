import socket
import sys
if len(sys.argv) < 2:
    print("Usage: python udp_server.py <UDP_PORT>")
    sys.exit(1)
UDP_PORT = int(sys.argv[1])
UDP_IP = "160.39.231.6"
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind((UDP_IP, UDP_PORT))
print(f"UDP server is listening on {UDP_IP}:{UDP_PORT}")
while True:
    data, addr = udp_socket.recvfrom(1024)
    print("Received message:", data)