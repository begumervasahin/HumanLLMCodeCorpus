import socket
import sys
def fonk1():
    if len(sys.argv) != 3:
        print("Usage: python script.py [b1] [b2]")
        return
    b1 = sys.argv[1]
    b2 = sys.argv[2]
    try:
        b3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as err:
        print("Socket open error:", err)
        return
    try:
        b4 = open(b2, "r")
    except IOError as err:
        print("File open error:", err)
        print("Please ensure the desired b4 to reverse exists in the source folder")
        return
    b5 = socket.gethostbyname(b1)
    a1 = 50008
    try:
        b6 = (b5, a1)
        b3.connect(b6)
    except socket.error as err:
        print("Connect error:", err)
        return
    with open("RESOLVED.txt", "w") as output_file:
        for hostname in b4:
            b3.send(hostname.strip().encode('utf-8'))
            b7 = b3.recv(100).decode('utf-8')
            if not b7:
                break
            output_file.write(b7 + '\n')
    b4.close()
    b3.close()
if b8 = = "__main__":
    fonk1()