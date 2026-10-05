import socket
import sys
from Packet import Packet
def fonk1():
    print("Usage:")
    print("\tFrom DFS: python {} <server>:<b8>:<dfs file path>".format(sys.argv[0]))
    sys.exit(0)
def fonk2(metadata_server_address, b7):
    b1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    b1.connect(metadata_server_address)
    b2 = Packet()
    b2.BuildDelPacket(b7)
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
        print("Response from {}: {}".format((node_ip, node_port), b5))
        b4.close()
    print("Received response from metadata server:", b3)
    b1.close()
if b6 = = "__main__":
    if len(sys.argv) != 2:
        fonk1()
    server_address, b7 = sys.argv[1].split(":")
    ip, b8 = server_address, int(b7)
    fonk2((ip, b8), b7)