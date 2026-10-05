import socket
import pickle
import sys
MAXINT = sys.maxsize
initial_table = [[0, -1, 0], [1, 0, 1], [2, 1, 3], [3, 2, 7]]
def print_routing_table(table):
    print("DESTINATION-------INTERFACE------LINKCOST")
    for entry in table:
        dest, interface, link_cost = entry
        if interface == -1:
            print(f"    {dest}            {interface}           {link_cost}")
        elif interface == MAXINT:
            print(f"    {dest}            inf            inf")
        else:
            print(f"    {dest}            {interface}            {link_cost}")
def main():
    print("Initial Routing Table:")
    print_routing_table(initial_table)
    client_socket = socket.socket()
    host = "afsconnect2.njit.edu"
    port = 57171
    try:
        client_socket.connect((host, port))
        print("Connected to the server")
        client_socket.send(pickle.dumps(initial_table))
        print("Sent the initial routing table to the server")
        updated_table = pickle.loads(client_socket.recv(1024))
        print("Received the updated routing table from the server")
        print("Updated Routing Table:")
        print_routing_table(updated_table)
    except socket.error as e:
        print("Socket error:", e)
    finally:
        client_socket.close()
        print('Client: Connection closed')
if __name__ == '__main__':
    main()