import socket
import sys
def fonk1():
    if len(sys.argv) != 3:
        print("Usage: python client.py <server_host> <b2>")
        return
    b1 = sys.argv[1]
    b2 = sys.argv[2]
    try:
        b3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as err:
        print("Socket open error:", err)
        return
    try:
        with open(b2, "r") as file:
            b4 = file.readlines()
    except IOError as err:
        print("File open error:", err)
        print("Please ensure the desired file to reverse exists in the source folder")
        b3.close()
        return
    try:
        b5 = socket.gethostbyname(b1)
        a1 = 50008
    except socket.error as err:
        print("Socket error:", err)
        b3.close()
        return
    try:
        b6 = (b5, a1)
        b3.connect(b6)
    except socket.error as err:
        print("Connect error:", err)
        b3.close()
        return
    with open("RESOLVED.txt", "w") as output_file:
        for b7 in b4:
            b7 = b7.strip().encode('utf-8')
            b3.send(b7)
            b8 = b3.recv(100).decode('utf-8')
            if not b8:
                break
            output_file.write(b8 + '\n')
    b3.close()
fonk1()