import socket
import sys
from Packet import Packet
def usage():
    print("Usage:")
    print("\tFrom DFS: python {} <server>:<port>:<dfs file path>".format(sys.argv[0]))
    sys.exit(0)
def del_from_dfs(address, fname):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(address)
    p = Packet()
    p.BuildDelPacket(fname)
    sock.sendall(p.getEncodedPacket())
    received = sock.recv(4096)
    p.DecodePacket(received)
    for i, j, k in p.getDataNodes():
        print(i, j, k)
        sockete = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sockete.connect((i, int(j)))
        p.BuildDelDataBlockPacket(k)
        sockete.sendall(p.getEncodedPacket())
        s = sockete.recv(4096)
        print(k, s)
        sockete.close()
    print(received)
    sock.close()
if __name__ == "__main__":
    if len(sys.argv) != 2:
        usage()
    file = sys.argv[1].split(":")
    ip = file[0]
    port = int(file[1])
    file_path = file[2]
    del_from_dfs((ip, port), file_path)