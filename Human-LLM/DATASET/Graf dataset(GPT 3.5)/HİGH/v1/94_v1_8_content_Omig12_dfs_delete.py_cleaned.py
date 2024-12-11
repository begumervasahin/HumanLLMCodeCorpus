import socket
import sys
from Packet import Packet
def fonk1():
    print("Usage:")
    print("\tFrom DFS: python {} <server>:<b9>:<dfs b7 path>".format(sys.argv[0]))
    sys.exit(0)
def fonk2(address, fname):
    b1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    b1.connect(address)
    b2 = Packet()
    b2.BuildDelPacket(fname)
    b1.sendall(b2.getEncodedPacket())
    b3 = b1.recv(4096)
    b2.DecodePacket(b3)
    for i, j, k in b2.getDataNodes():
        print(i, j, k)
        b4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        b4.connect((i, int(j)))
        b2.BuildDelDataBlockPacket(k)
        b4.sendall(b2.getEncodedPacket())
        b5 = b4.recv(4096)
        print(k, b5)
        b4.close()
    print(b3)
    b1.close()
if b6 = = "__main__":
    if len(sys.argv) != 2:
        fonk1()
    b7 = sys.argv[1].split(":")
    b8 = b7[0]
    b9 = int(b7[1])
    b10 = b7[2]
    fonk2((b8, b9), b10)