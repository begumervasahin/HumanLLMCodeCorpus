import pickle
import socket
import sys
b1 = sys.maxsize
def fonk1(table):
    print("DESTINATION-------INTERFACE------LINKCOST")
    for destination, b2, link_cost in table:
        if b2 = = -1:
            print(f"    {destination}            {b2}           {link_cost}")
        elif b2 = = b1:
            print(f"    {destination}            inf            inf")
        else:
            print(f"    {destination}            {b2}            {link_cost}")
def fonk2(current_table, b9):
    for i in range(len(current_table)):
        for j in range(len(b9)):
            b3 = current_table[i][2] + int(b9[j][2])
            if b3 < b9[i][2]:
                b9[i][2] = b3 + 1
    return b9
def fonk3(b6, a1):
    b4 = socket.socket()
    try:
        b4.bind((b6, a1))
    except socket.error as msg:
        print(f'Bind failed. Error Code: {msg[0]} Message: {msg[1]}')
        sys.exit()
    print('Socket bind complete')
    b4.listen(1)
    return b4
def fonk4():
    b5 = [[0, 0, 1], [1, -1, 0], [2, 1, 1], [3, b1, b1]]
    print("Initial table:")
    fonk1(b5)
    b6 = ''
    a1 = 57171
    b4 = fonk3(b6, a1)
    client_socket, b7 = b4.accept()
    print(f'Got connection from {b7}')
    b8 = client_socket.recv(1024)
    b9 = pickle.loads(b8)
    print("Current table:")
    fonk1(b5)
    print("Received table:")
    fonk1(b9)
    b10 = fonk2(b5, b9)
    print("Updated table:")
    fonk1(b10)
    client_socket.send(pickle.dumps(b10))
    client_socket.close()
    b4.close()
if b11 = = "__main__":
    fonk4()