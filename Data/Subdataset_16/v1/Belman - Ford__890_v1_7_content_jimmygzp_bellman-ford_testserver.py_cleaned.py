import socket
import sys
import pickle
def fonk1():
    if len(sys.argv) != 2:
        print("Usage: python script.py <b1>")
        sys.exit(1)
    b1 = int(sys.argv[1])
    b2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    b2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    b2.bind(("", b1))
    print(f"Listening on b1 {b1}")
    data, b3 = b2.recvfrom(4096)
    b4 = pickle.loads(data)
    print(f"Sender: {b3}")
    print(f"Recovered entry: {b4}")
if b5 = = "__main__":
    fonk1()