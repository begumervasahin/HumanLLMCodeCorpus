import socket
import sys
if len(sys.argv) < 2:
    print("Usage: python udp_server.py <b1>")
    sys.exit(1)
b1 = int(sys.argv[1])
b2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
b3 = ("160.39.231.6", b1)
b2.bind(b3)
print(f"UDP server is running on port {b1}")
while True:
    data, b4 = b2.recvfrom(1024)
    b5 = data.decode('utf-8')
    print(f"Received b5 from {b4}: {b5}")