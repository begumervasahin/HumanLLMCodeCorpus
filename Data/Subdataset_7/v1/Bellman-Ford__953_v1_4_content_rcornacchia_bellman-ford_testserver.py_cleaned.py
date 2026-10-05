import socket
import sys
if len(sys.argv) < 2:
    print("Usage: python udp_server.py <b1>")
    sys.exit(1)
b1 = int(sys.argv[1])
b2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
b2.bind(("160.39.231.6", b1))
print(f"UDP server is running on {b1}")
while True:
    data, b3 = b2.recvfrom(1024)
    print(f"Received message from {b3}: {data.decode('utf-8')}")