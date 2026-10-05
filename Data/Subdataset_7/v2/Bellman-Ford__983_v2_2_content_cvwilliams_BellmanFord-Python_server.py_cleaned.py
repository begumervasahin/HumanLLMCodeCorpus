import pickle
import socket
import sys
b1 = sys.maxsize
def fonk1(table):
    print("DESTINATION-------INTERFACE------LINKCOST")
    for entry in table:
        dest, b3, b2 = entry
        if b3 = = -1:
            print(f"    {dest}            {b3}           {b2}")
        elif b3 = = b1:
            print(f"    {dest}            inf            inf")
        else:
            print(f"    {dest}            {b3}            {b2}")
def fonk2():
    b4 = [[0, 0, 1], [1, -1, 0], [2, 1, 1], [3, b1, b1]]
    print("Initial table: ")
    fonk1(b4)
    b5 = socket.socket()
    a1 = 57171
    b6 = ''
    try:
        b5.bind((b6, a1))
    except socket.error as msg:
        print(f'Bind failed. Error Code: {msg[0]}. Message: {msg[1]}')
        sys.exit()
    print('Socket bind complete')
    b5.listen(1)
    client, b7 = b5.accept()
    print('Got connection from', b7)
    b8 = client.recv(1024)
    b8 = pickle.loads(b8)
    print("Current table: ")
    fonk1(b4)
    print("Received table: ")
    fonk1(b8)
    for i in range(len(b4)):
        for j in range(len(b8)):
            b9 = b4[i][2] + int(b8[j][2])
            if b9 < b8[i][2]:
                b8[i][2] = b9 + 1
    print("Updated table: ")
    fonk1(b8)
    client.send(pickle.dumps(b8))
    b5.close()
if b10 = = "__main__":
    fonk2()