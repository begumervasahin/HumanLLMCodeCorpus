import socket as mysoc
import pickle
import sys
rs_host = sys.argv[1]
file_name = sys.argv[2]
def client():
    try:
        ctors = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
    except mysoc.error as err:
        print(f"Socket creation error: {err}")
        return
    try:
        with open(file_name, "r") as fr:
            hostnames = fr.readlines()
    except IOError as err:
        print(f"File open error: {err}")
        print("Please ensure the desired file to reverse exists in the source folder.")
        return
    try:
        server_address = mysoc.gethostbyname(rs_host)
        port = 50008
        server_binding = (server_address, port)
        ctors.connect(server_binding)
    except mysoc.error as err:
        print(f"Connection error: {err}")
        return
    try:
        with open("RESOLVED.txt", "w") as fw:
            for hostname in hostnames:
                ctors.send(hostname.strip().encode('utf-8'))
                data_from_rs = ctors.recv(100).decode('utf-8')
                if not data_from_rs:
                    break
                fw.write(data_from_rs + '\n')
    finally:
        ctors.close()
if __name__ == "__main__":
    client()