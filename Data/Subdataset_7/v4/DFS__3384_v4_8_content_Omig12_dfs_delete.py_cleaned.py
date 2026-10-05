import socket
import sys
from Packet import Packet
def fonk1():
    print("Usage:\n\tFrom DFS: python {} <server>:<b9>:<dfs file path>\n\t".format(sys.argv[0]))
    sys.exit(0)
def fonk2(address, fname):
    b1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    b1.connect(address)
    b2 = Packet()
    b2.BuildDelPacket(fname)
    b1.sendall(b2.getEncodedPacket())
    b3 = b1.recv(4096)
    b2.DecodePacket(b3)
    for node_ip, node_port, block_id in b2.getDataNodes():
        print("Deleting block {} from {}:{}".format(block_id, node_ip, node_port))
        b4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        b4.connect((node_ip, int(node_port)))
        b2.BuildDelDataBlockPacket(block_id)
        b4.sendall(b2.getEncodedPacket())
        b5 = b4.recv(4096)
        print(block_id, b5)
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