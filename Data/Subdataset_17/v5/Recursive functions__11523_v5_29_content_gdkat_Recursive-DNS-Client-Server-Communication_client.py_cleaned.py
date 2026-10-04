import socket as mysoc
import sys
def client(rs_host, file_name):
    try:
        client_socket = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
    except mysoc.error as err:
        print(f'Socket open error: {err}')
        return
    try:
        with open(file_name, "r") as file:
            hostnames = file.readlines()
    except IOError as err:
        print(f'File open error: {err}')
        print("Please ensure the desired file to reverse exists in the source folder")
        return
    try:
        server_address = mysoc.gethostbyname(rs_host)
        server_port = 50008
        server_binding = (server_address, server_port)
        client_socket.connect(server_binding)
    except mysoc.error as err:
        print(f'Connection error: {err}')
        return
    try:
        with open("RESOLVED.txt", "w") as output_file:
            for hostname in hostnames:
                client_socket.send(hostname.strip().encode('utf-8'))
                response = client_socket.recv(100).decode('utf-8')
                if not response:
                    break
                output_file.write(response + '\n')
    except IOError as err:
        print(f'File write error: {err}')
    finally:
        client_socket.close()
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <RSHost> <FileName>")
    else:
        rs_host = sys.argv[1]
        file_name = sys.argv[2]
        client(rs_host, file_name)