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
        destination, b4, b3 = entry
        if b4 = = -1:
            print(f"    {destination}            {b4}           {b3}")
        elif b4 = = b1:
            print(f"    {destination}            inf            inf")
        else:
            print(f"    {destination}            {b4}            {b3}")
def fonk2():
    print("Initial Routing Table:")
    fonk1(b2)
    with socket.socket() as s:
        b5 = "afsconnect2.njit.edu"
        a1 = 57171
        print("Client: Connecting to the server...")
        s.connect((b5, a1))
        print("Client: Sending initial table...")
        s.send(pickle.dumps(b2))
        print("Client: Waiting for update...")
        b6 = s.recv(1024)
        b6 = pickle.loads(b6)
        print("Client: Received updated table.")
        fonk1(b6)
        print('Client: Connection closed')
if b7 = = '__main__':
    fonk2()