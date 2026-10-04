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
def print_table(table):
    print("DESTINATION-------INTERFACE------LINKCOST")
    for entry in table:
        destination, interface, link_cost = entry
        if interface == -1:
            print(f"    {destination}            {interface}           {link_cost}")
        elif interface == MAXINT:
            print(f"    {destination}            inf            inf")
        else:
            print(f"    {destination}            {interface}            {link_cost}")
def main():
    print("Initial Routing Table:")
    print_table(table0)
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
    print_table(tab_update)
    s.close()
    print('Client: Connection closed')
if __name__ == '__main__':
    main()