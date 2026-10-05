import socket
import sys
if len(sys.argv) < 2:
    print("Usage: python udp_server.py <b1>")
    sys.exit(1)
b1 = int(sys.argv[1])
b2 = "160.39.231.6"
b3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
b3.bind((b2, b1))
print(f"UDP server is listening on {b2}:{b1}")
while True:
    data, b4 = b3.recvfrom(1024)
    print("Received message:", data)