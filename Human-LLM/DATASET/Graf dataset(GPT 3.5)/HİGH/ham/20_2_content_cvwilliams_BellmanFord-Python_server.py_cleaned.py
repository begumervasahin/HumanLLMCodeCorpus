import pickle
import socket
import sys
def fonk1(table):
    print("DESTINATION-------INTERFACE------LINKCOST")
    for i in table:
        if i[1] == -1:
            print("    ",i[0],"            ",i[1],"           ",i[2])
        elif i[1]==b1:
            print("    ",i[0],"            inf            inf")
        else:
            print("    ",i[0],"            ",i[1],"            ",i[2])
b1 = sys.maxsize
b2 = [[0,0,1],[1,-1,0],[2,1,1],[3,b1,b1]]
fonk1(b2)
b3 = socket.socket()
a1 = 57171
b4 = ''
try:
    b3.bind((b4,a1))
except (b3.error, msg):
    print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()
print('Socket bind complete')
b3.listen(1)
client, b5 = b3.accept()
print ('Got connection from', b5)
b6 = client.recv(1024)
b6 = pickle.loads(b6)
print("Current table: ")
fonk1(b2)
print("Received table: ")
fonk1(b6)
a2 = 0
b7 = len(b2)
b8 = len(b6)
for i in range(b7):
    for j in range(b8):
        a2 = b2[i][2] + int(b6[j][2])
        if a2<b6[i][2]:
            b6[i][2] = a2+1
print("Updated table: ")
fonk1(b6)
client.send(pickle.dumps(b6))
b3.close()