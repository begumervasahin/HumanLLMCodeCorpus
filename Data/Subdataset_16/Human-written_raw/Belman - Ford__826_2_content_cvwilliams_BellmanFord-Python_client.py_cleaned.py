import socket
import pickle
import sys
b1 = sys.maxsize
b2 = [[0,-1,0],[1,0,1],[2,1,3],[3,2,7]]
def fonk1(table):
    print("DESTINATION-------INTERFACE------LINKCOST")
    for i in table:
        if i[1] == -1:
            print("    ",i[0],"            ",i[1],"           ",i[2])
        elif i[1]==b1:
            print("    ",i[0],"            inf            inf")
        else:
            print("    ",i[0],"            ",i[1],"            ",i[2])
fonk1(b2)
b3 = socket.socket()
b4 = "afsconnect2.njit.edu"
a1 = 57171
b3.connect((b4, a1))
b3.send(pickle.dumps(b2))
b5 = b3.recv(1024)
b5 = pickle.loads(b5)
fonk1(b5)
b3.close
print ('Client: Connection closed')