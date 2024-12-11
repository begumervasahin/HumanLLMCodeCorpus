import pickle
import socket
import sys
b1 = sys.maxsize
def fonk1(b4):
    print("DESTINATION-------INTERFACE------LINKCOST")
    for entry in b4:
        dest, b3, b2 = entry
        if b3 = = -1:
            print(f"    {dest}            {b3}           {b2}")
        elif b3 = = b1:
            print(f"    {dest}            inf            inf")
        else:
            print(f"    {dest}            {b3}            {b2}")
def fonk2(socket):
    b4 = socket.recv(1024)
    return pickle.loads(b4)
def fonk3(b6, b10):
    for i in range(len(b6)):
        for j in range(len(b10)):
            b5 = b6[i][2] + int(b10[j][2])
            if b5 < b10[i][2]:
                b10[i][2] = b5 + 1
    return b10
def fonk4():
    b6 = [[0, 0, 1], [1, -1, 0], [2, 1, 1], [3, b1, b1]]
    print("Initial b4: ")
    fonk1(b6)
    b7 = socket.socket()
    a1 = 57171
    b8 = ''
    try:
        b7.bind((b8, a1))
    except socket.error as msg:
        print(f'Bind failed. Error Code: {msg[0]}. Message: {msg[1]}')
        sys.exit()
    print('Socket bind complete')
    b7.listen(1)
    client, b9 = b7.accept()
    print('Got connection from', b9)
    b10 = fonk2(client)
    print("Current b4: ")
    fonk1(b6)
    print("Received b4: ")
    fonk1(b10)
    b11 = fonk3(b6, b10)
    print("Updated b4: ")
    fonk1(b11)
    client.send(pickle.dumps(b11))
    b7.close()
if b12 = = "__main__":
    fonk4()