import socket
import pickle
import sys
b1 = sys.maxsize
b2 = [
    [0, -1, 0],
    [1, 0, 1],
    [2, 1, 3],
    [3, 2, 7]
]
def fonk1(table):
    print("DESTINATION-------INTERFACE------LINKCOST")
    for entry in table:
        dest, b4, b3 = entry
        if b4 = = -1:
            print(f"    {dest}            {b4}           {b3}")
        elif b4 = = b1:
            print(f"    {dest}            inf            inf")
        else:
            print(f"    {dest}            {b4}            {b3}")
def fonk2():
    print("Initial Routing Table:")
    fonk1(b2)
    b5 = socket.socket()
    b6 = "afsconnect2.njit.edu"
    a1 = 57171
    try:
        b5.connect((b6, a1))
        print("Connected to the server")
        b5.send(pickle.dumps(b2))
        print("Sent the initial routing table to the server")
        b7 = pickle.loads(b5.recv(1024))
        print("Received the updated routing table from the server")
        print("Updated Routing Table:")
        fonk1(b7)
    except socket.error as e:
        print("Socket error:", e)
    finally:
        b5.close()
        print('Client: Connection closed')
if b8 = = '__main__':
    fonk2()