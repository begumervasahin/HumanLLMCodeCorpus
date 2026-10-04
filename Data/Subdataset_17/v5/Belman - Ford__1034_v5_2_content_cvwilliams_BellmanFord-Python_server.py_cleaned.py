import pickle
import socket
import sys
MAXINT = sys.maxsize
def print_table(table):
    print("DESTINATION-------INTERFACE------LINKCOST")
    for destination, interface, link_cost in table:
        if interface == -1:
            print(f"    {destination}            {interface}           {link_cost}")
        elif interface == MAXINT:
            print(f"    {destination}            inf            inf")
        else:
            print(f"    {destination}            {interface}            {link_cost}")
def update_table(current_table, received_table):
    for i, current_entry in enumerate(current_table):
        for j, received_entry in enumerate(received_table):
            new_cost = current_entry[2] + int(received_entry[2])
            if new_cost < received_table[i][2]:
                received_table[i][2] = new_cost + 1
    return received_table
def setup_server_socket(host, port):
    server_socket = socket.socket()
    try:
        server_socket.bind((host, port))
    except socket.error as msg:
        print(f'Bind failed. Error Code: {msg[0]} Message: {msg[1]}')
        sys.exit()
    print('Socket bind complete')
    server_socket.listen(1)
    return server_socket
def main():
    initial_table = [[0, 0, 1], [1, -1, 0], [2, 1, 1], [3, MAXINT, MAXINT]]
    print("Initial table:")
    print_table(initial_table)
    host = ''
    port = 57171
    server_socket = setup_server_socket(host, port)
    client_socket, client_address = server_socket.accept()
    print(f'Got connection from {client_address}')
    data = client_socket.recv(1024)
    received_table = pickle.loads(data)
    print("Current table:")
    print_table(initial_table)
    print("Received table:")
    print_table(received_table)
    updated_table = update_table(initial_table, received_table)
    print("Updated table:")
    print_table(updated_table)
    client_socket.send(pickle.dumps(updated_table))
    client_socket.close()
    server_socket.close()
if __name__ == "__main__":
    main()