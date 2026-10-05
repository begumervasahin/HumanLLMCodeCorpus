import socket
local_ip = socket.gethostbyname(socket.gethostname())
udp_port = 5005
message = "Hello, World!"
print("UDP target IP:", local_ip)
print("UDP target port:", udp_port)
print("Message:", message)
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.sendto(message.encode(), (local_ip, udp_port))