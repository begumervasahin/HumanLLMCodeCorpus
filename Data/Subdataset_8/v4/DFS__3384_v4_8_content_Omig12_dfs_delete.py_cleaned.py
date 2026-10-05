import socket
import sys
from Packet import Packet
def usage():
    print("Usage:\n\tFrom DFS: python {} <server>:<port>:<dfs file path>\n\t".format(sys.argv[0]))
    sys.exit(0)
def del_from_dfs(address, fname):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(address)
    packet = Packet()
    packet.BuildDelPacket(fname)
    sock.sendall(packet.getEncodedPacket())
    received = sock.recv(4096)
    packet.DecodePacket(received)
    for node_ip, node_port, block_id in packet.getDataNodes():
        print("Deleting block {} from {}:{}".format(block_id, node_ip, node_port))
        node_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        node_sock.connect((node_ip, int(node_port)))
        packet.BuildDelDataBlockPacket(block_id)
        node_sock.sendall(packet.getEncodedPacket())
        s = node_sock.recv(4096)
        print(block_id, s)
        node_sock.close()
    print(received)
    sock.close()
if __name__ == "__main__":
    if len(sys.argv) != 2:
        usage()
    file_info = sys.argv[1].split(":")
    ip = file_info[0]
    port = int(file_info[1])
    file_path = file_info[2]
    del_from_dfs((ip, port), file_path)