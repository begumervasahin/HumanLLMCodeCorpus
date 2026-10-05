import socket
local_ip_address = socket.gethostbyname(socket.gethostname())
udp_port = 5005
message = "Hello, World!"
print("UDP target IP:", local_ip_address)
print("UDP target port:", udp_port)
print("Message:", message)
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.sendto(bytes(message, 'utf-8'), (local_ip_address, udp_port))