import socket
import sys
from Packet import Packet
def usage():
    print("Usage:")
    print("\tFrom DFS: python {} <server>:<port>:<dfs file path>".format(sys.argv[0]))
    sys.exit(0)
def delete_from_dfs(metadata_server_address, file_path):
    metadata_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    metadata_socket.connect(metadata_server_address)
    delete_packet = Packet()
    delete_packet.BuildDelPacket(file_path)
    metadata_socket.sendall(delete_packet.getEncodedPacket())
    response = metadata_socket.recv(4096)
    delete_packet.DecodePacket(response)
    for node_ip, node_port, block_id in delete_packet.getDataNodes():
        print("Deleting block {} from {}:{}".format(block_id, node_ip, node_port))
        node_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        node_socket.connect((node_ip, int(node_port)))
        delete_packet.BuildDelDataBlockPacket(block_id)
        node_socket.sendall(delete_packet.getEncodedPacket())
        node_response = node_socket.recv(4096)
        print("Received response from {}: {}".format((node_ip, node_port), node_response))
        node_socket.close()
    print("Received response from metadata server:", response)
    metadata_socket.close()
if __name__ == "__main__":
    if len(sys.argv) != 2:
        usage()
    server_address, file_path = sys.argv[1].split(":")
    ip = server_address
    port = int(file_path)
    delete_from_dfs((ip, port), file_path)