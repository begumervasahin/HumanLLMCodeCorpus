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
        with open(b2, "r") as file:
            b4 = socket.gethostbyname(b1)
            a1 = 50008
            b5 = (b4, a1)
            b3.connect(b5)
            with open("RESOLVED.txt", "w") as output_file:
                for hostname in file:
                    b3.send(hostname.strip().encode('utf-8'))
                    b6 = b3.recv(100).decode('utf-8')
                    if b6:
                        output_file.write(b6 + '\n')
                    else:
                        break
    except IOError as err:
        print("File open error:", err)
        print("Please ensure the desired file to reverse exists in the source folder")
        return
    except socket.error as err:
        print("Connect error:", err)
        return
    finally:
        b3.close()
if b7 = = "__main__":
    fonk1()