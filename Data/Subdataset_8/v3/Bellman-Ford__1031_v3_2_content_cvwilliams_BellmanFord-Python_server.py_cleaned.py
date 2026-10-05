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
def receive_table_from_client(socket):
    table = socket.recv(1024)
    return pickle.loads(table)
def update_table(table1, table0):
    for i in range(len(table1)):
        for j in range(len(table0)):
            num = table1[i][2] + int(table0[j][2])
            if num < table0[i][2]:
                table0[i][2] = num + 1
    return table0
def main():
    table1 = [[0, 0, 1], [1, -1, 0], [2, 1, 1], [3, MAXINT, MAXINT]]
    print("Initial table: ")
    print_table(table1)
    s = socket.socket()
    port = 57171
    host = ''
    try:
        s.bind((host, port))
    except socket.error as msg:
        print(f'Bind failed. Error Code: {msg[0]}. Message: {msg[1]}')
        sys.exit()
    print('Socket bind complete')
    s.listen(1)
    client, addr = s.accept()
    print('Got connection from', addr)
    table0 = receive_table_from_client(client)
    print("Current table: ")
    print_table(table1)
    print("Received table: ")
    print_table(table0)
    updated_table = update_table(table1, table0)
    print("Updated table: ")
    print_table(updated_table)
    client.send(pickle.dumps(updated_table))
    s.close()
if __name__ == "__main__":
    main()