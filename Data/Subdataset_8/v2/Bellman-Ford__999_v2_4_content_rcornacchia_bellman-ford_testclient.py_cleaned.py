import socket
local_ip = socket.gethostbyname(socket.gethostname())
udp_port = 5005
message = "Hello, World!"
print("UDP target IP:", local_ip)
print("UDP target port:", udp_port)
print("Message:", message)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(bytes(message, 'utf-8'), (local_ip, udp_port))