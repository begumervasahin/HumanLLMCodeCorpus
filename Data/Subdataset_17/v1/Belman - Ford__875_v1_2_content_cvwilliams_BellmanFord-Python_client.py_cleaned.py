import socket
import pickle
import sys
MAXINT = sys.maxsize
table0 = [
    [0, -1, 0],
    [1, 0, 1],
    [2, 1, 3],
    [3, 2, 7]
]
def printTable(table):
    print("DESTINATION-------INTERFACE------LINKCOST")
    for i in table:
        if i[1] == -1:
            print(f"    {i[0]}            {i[1]}           {i[2]}")
        elif i[1] == MAXINT:
            print(f"    {i[0]}            inf            inf")
        else:
            print(f"    {i[0]}            {i[1]}            {i[2]}")
def main():
    printTable(table0)
    s = socket.socket()
    host = "afsconnect2.njit.edu"
    port = 57171
    print("Client: Connecting to the server...")
    s.connect((host, port))
    print("Client: Sending initial table...")
    s.send(pickle.dumps(table0))
    print("Client: Waiting for update...")
    tab_update = s.recv(1024)
    tab_update = pickle.loads(tab_update)
    print("Client: Received updated table.")
    printTable(tab_update)
    s.close()
    print('Client: Connection closed')
if __name__ == '__main__':
    main()