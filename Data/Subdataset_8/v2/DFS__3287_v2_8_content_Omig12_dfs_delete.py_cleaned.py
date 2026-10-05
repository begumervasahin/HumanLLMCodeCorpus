import socket
import sys
from Packet import Packet
def usage():
    print("Usage:")
    print("\tFrom DFS: python {} <server>:<port>:<dfs file path>".format(sys.argv[0]))
    sys.exit(0)
def delete_from_dfs(metadata_server_address, file_path):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(metadata_server_address)
    packet = Packet()
    packet.BuildDelPacket(file_path)
    sock.sendall(packet.getEncodedPacket())
    received_data = sock.recv(4096)
    packet.DecodePacket(received_data)
    for node_ip, node_port, block_id in packet.getDataNodes():
        print("Deleting block {} from {}:{}".format(block_id, node_ip, node_port))
        node_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        node_sock.connect((node_ip, int(node_port)))
        packet.BuildDelDataBlockPacket(block_id)
        node_sock.sendall(packet.getEncodedPacket())
        response = node_sock.recv(4096)
        print("Response from {}: {}".format((node_ip, node_port), response))
        node_sock.close()
    print("Received response from metadata server:", received_data)
    sock.close()
if __name__ == "__main__":
    if len(sys.argv) != 2:
        usage()
    server_address, file_path = sys.argv[1].split(":")
    ip, port = server_address, int(file_path)
    delete_from_dfs((ip, port), file_path)