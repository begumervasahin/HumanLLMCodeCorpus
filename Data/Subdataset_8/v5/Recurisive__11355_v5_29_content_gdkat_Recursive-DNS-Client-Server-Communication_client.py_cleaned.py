import socket
import sys
def client():
    if len(sys.argv) != 3:
        print("Usage: python client.py <server_host> <file_name>")
        return
    rs_host = sys.argv[1]
    file_name = sys.argv[2]
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as err:
        print("Socket open error:", err)
        return
    try:
        with open(file_name, "r") as file:
            hostnames = file.readlines()
    except IOError as err:
        print("File open error:", err)
        print("Please ensure the desired file to reverse exists in the source folder")
        client_socket.close()
        return
    try:
        server_ip = socket.gethostbyname(rs_host)
        port = 50008
    except socket.error as err:
        print("Socket error:", err)
        client_socket.close()
        return
    try:
        server_address = (server_ip, port)
        client_socket.connect(server_address)
    except socket.error as err:
        print("Connect error:", err)
        client_socket.close()
        return
    with open("RESOLVED.txt", "w") as output_file:
        for hostname in hostnames:
            hostname = hostname.strip().encode('utf-8')
            client_socket.send(hostname)
            data_from_server = client_socket.recv(100).decode('utf-8')
            if not data_from_server:
                break
            output_file.write(data_from_server + '\n')
    client_socket.close()
client()