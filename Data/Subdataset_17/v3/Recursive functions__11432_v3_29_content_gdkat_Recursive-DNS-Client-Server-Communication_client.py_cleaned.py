import socket as mysoc
import sys
rs_host = sys.argv[1]
file_name = sys.argv[2]
def client():
    try:
        client_socket = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
    except mysoc.error as err:
        print(f"Socket creation error: {err}")
        return
    try:
        with open(file_name, "r") as file_reader:
            hostnames = file_reader.readlines()
    except IOError as err:
        print(f"File open error: {err}")
        print("Please ensure the file exists in the source folder.")
        return
    try:
        server_address = mysoc.gethostbyname(rs_host)
        port = 50008
        server_binding = (server_address, port)
        client_socket.connect(server_binding)
    except mysoc.error as err:
        print(f"Connection error: {err}")
        return
    try:
        with open("RESOLVED.txt", "w") as file_writer:
            for hostname in hostnames:
                client_socket.send(hostname.strip().encode('utf-8'))
                data_from_server = client_socket.recv(100).decode('utf-8')
                if not data_from_server:
                    break
                file_writer.write(data_from_server + '\n')
    finally:
        client_socket.close()
if __name__ == "__main__":
    client()