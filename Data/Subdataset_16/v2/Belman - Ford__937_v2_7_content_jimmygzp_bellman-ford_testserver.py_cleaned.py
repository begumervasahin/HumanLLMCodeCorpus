import socket
import sys
import pickle
def fonk1():
    if len(sys.argv) != 2:
        print("Usage: python script.py <b1>")
        sys.exit(1)
    b1 = int(sys.argv[1])
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as recvsock:
        recvsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        recvsock.bind(("", b1))
        print(f"Listening on b1 {b1}")
        data, b2 = recvsock.recvfrom(4096)
    b3 = pickle.loads(data)
    print(f"Sender: {b2}")
    print(f"Recovered entry: {b3}")
if b4 = = "__main__":
    fonk1()