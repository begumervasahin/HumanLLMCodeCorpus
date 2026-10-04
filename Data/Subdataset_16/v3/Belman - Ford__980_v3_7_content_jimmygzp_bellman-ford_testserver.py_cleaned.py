import socket
import sys
import pickle
def fonk1(b2):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as recvsock:
        recvsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        recvsock.bind(("", b2))
        print(f"Listening on b2 {b2}")
        data, b1 = recvsock.recvfrom(4096)
    return data, b1
def fonk2():
    if len(sys.argv) != 2:
        print("Usage: python script.py <b2>")
        sys.exit(1)
    b2 = int(sys.argv[1])
    data, b1 = fonk1(b2)
    b3 = pickle.loads(data)
    print(f"Sender: {b1}")
    print(f"Recovered entry: {b3}")
if b4 = = "__main__":
    fonk2()