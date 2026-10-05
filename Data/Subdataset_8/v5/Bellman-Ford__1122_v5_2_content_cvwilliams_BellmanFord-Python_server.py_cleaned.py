import pickle
import socket
import sys
MAXINT = sys.maxsize
def print_table(table):
    print("DESTINATION-------INTERFACE------LINKCOST")
    for entry in table:
        dest, interface, cost = entry
        if interface == -1:
            print(f"    {dest}            {interface}           {cost}")
        elif interface == MAXINT:
            print(f"    {dest}            inf            inf")
        else:
            print(f"    {dest}            {interface}            {cost}")
def receive_table(socket_conn):
    table_data = socket_conn.recv(1024)
    return pickle.loads(table_data)
def update_table(local_table, received_table):
    for i in range(len(local_table)):
        for j in range(len(received_table)):
            num = local_table[i][2] + int(received_table[j][2])
            if num < received_table[i][2]:
                received_table[i][2] = num + 1
def main():
    local_table = [[0, 0, 1], [1, -1, 0], [2, 1, 1], [3, MAXINT, MAXINT]]
    print("Initial table: ")
    print_table(local_table)
    server_socket = socket.socket()
    port = 57171
    host = ''
    try:
        server_socket.bind((host, port))
    except socket.error as msg:
        print(f'Bind failed. Error Code: {msg[0]}. Message: {msg[1]}')
        sys.exit()
    print('Socket bind complete')
    server_socket.listen(1)
    client_socket, addr = server_socket.accept()
    print('Got connection from', addr)
    received_table = receive_table(client_socket)
    print("Current table: ")
    print_table(local_table)
    print("Received table: ")
    print_table(received_table)
    update_table(local_table, received_table)
    print("Updated table: ")
    print_table(received_table)
    client_socket.send(pickle.dumps(received_table))
    server_socket.close()
if __name__ == "__main__":
    main()