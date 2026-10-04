import pickle
import socket
import sys
def fonk1(table):
    print("DESTINATION-------INTERFACE------LINKCOST")
    for entry in table:
        destination, b2, b1 = entry
        if b2 = = -1:
            print(f"    {destination}            {b2}           {b1}")
        elif b2 = = b4:
            print(f"    {destination}            inf            inf")
        else:
            print(f"    {destination}            {b2}            {b1}")
def fonk2(current_table, received_table):
    for i in range(len(current_table)):
        for j in range(len(received_table)):
            b3 = current_table[i][2] + int(received_table[j][2])
            if b3 < received_table[i][2]:
                received_table[i][2] = b3 + 1
    return received_table
b4 = sys.maxsize
b5 = [[0, 0, 1], [1, -1, 0], [2, 1, 1], [3, b4, b4]]
print("Initial table:")
fonk1(b5)
b6 = socket.socket()
a1 = 57171
b7 = ''
try:
    b6.bind((b7, a1))
except socket.error as msg:
    print(f'Bind failed. Error Code: {msg[0]} Message: {msg[1]}')
    sys.exit()
print('Socket bind complete')
b6.listen(1)
client_socket, b8 = b6.accept()
print(f'Got connection from {b8}')
b9 = client_socket.recv(1024)
b10 = pickle.loads(b9)
print("Current table:")
fonk1(b5)
print("Received table:")
fonk1(b10)
b11 = fonk2(b5, b10)
print("Updated table:")
fonk1(b11)
client_socket.send(pickle.dumps(b11))
client_socket.close()
b6.close()