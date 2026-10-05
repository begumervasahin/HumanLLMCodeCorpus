import socket
local_ip = socket.gethostbyname(socket.gethostname())
udp_port = 5005
message = "Hello, World!"
print(f"UDP target IP: {local_ip}")
print(f"UDP target port: {udp_port}")
print(f"Message: {message}")
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
encoded_message = message.encode()
udp_socket.sendto(encoded_message, (local_ip, udp_port))