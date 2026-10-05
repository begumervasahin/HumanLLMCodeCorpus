import sys
import socket
import json
import threading
import time
import os
import copy
b1 = sys.argv[1];
b2 = int(sys.argv[2]);
b3 = sys.argv[3];
b4 = {};
b5 = {};
b6 = []
b7 = {}
b8 = threading.Lock()
b9 = {}
b10 = {}
class class1:
     def fonk1(self, b1,b2,b3):
        self.b1 = b1;
        self.b2 = b2;
        b11 = {}
        b12 = []
        global b13
        b13 = {}
        self.b14 = b11
        self.b12 = b12
        b15 = open(b3, "r+");
        b16 = b15.read();
        b17 = (b16.split());
        b18 = b17[0];
        b19 = 1;
        b20 = len(b17);
        b4[b1]=[float(0),b2]
        while (b19!=b20):
            b4[b17[b19]]=[float(b17[b19+1]), int(b17[b19+2])]
            b19+=3;
        b21 = b4.items();
        b19 = 0;
        b20 = len(b4);
        while(b19 < b20 ):
            b11[b21[b19][0]]=b21[b19][1][0]
            if(b21[b19][0]!= b1):
                b12.append(b21[b19][0])
            b19+=1;
        b5[b1]=b11
        b13 = b5.copy()
def fonk2():
    b22 = "localhost"
    b23 = b2
    b24 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    b24.bind((b22,b23))
    b25 = {}
    b26 = {}
    print ("SERVER HERE!\nThe server is ready to receive")
    while 1:
        b27 = time.time();
        message, b28 = b24.recvfrom(2048)
        b29 = json.loads(message)
        for b31 in b29.keys():
            b30 = b31.encode('ascii','ignore')
        for b31,val in b29[b30].items():
            b31 = b31.encode('ascii','ignore')
            b26[b31]=val
        b25[b30]=b26.copy()
        b26 = {}
        b9[b1]=b13[b1].copy()
        b9.update(b25)
        for b32 in b42.b12:
            if b30 not in b10.keys():
                b10[b30]=b27;
            else:
                if b32 = =b30 and b10[b30] != float('INF'):
                    b10[b30]=b27
                elif (b32 = = b30 and b10[b30] == float('INF')):
                    b10[b30]=b27
                elif (b32 != b30 and b32 in b10.keys()):
                    if b27 - b10[b32] > 10:
                        b10[b32] = float('INF')
                        del b9[b1][b32]
                        del b9[b32]
                        del b7[b32]
        for b32 in b10.keys():
             if (b10[b32] == float('inf') and b32 in b9.keys() ):
                  del b9[b1][b32]
                  del b9[b32]
        threading.Thread(b33 = bellman_ford, args=(b9,)).start()
    b24.close()
def fonk3():
    while 1:
        b34 = []
        for b21 in b4.items():
            b34.append(b21[1][1]);
        b35 = "localhost"
        b36 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        b37 = json.dumps(b5)
        for items in b34:
            if int(items)!=b2:
                b36.sendto(b37.encode(),(b35, int(items)))
        time.sleep(5)
        b36.close()
def fonk4(b9):
    b38 = []
    for b32 in b9:
        for neighbour in b42.b12:
            if(b32 = = neighbour):
                b38.append(b32)
    b39 = []
    for b32 in b9:
        for neighbour in b9[b32]:
             if (neighbour in b10.keys()  and b10[neighbour]== float('inf')):
                pass
             else:
                b39.append(neighbour)
    b40 = set(b39)
    b6 = list(b40)
    for b32 in b9:
        for router in b6:
            if(router not in b9[b32].keys()):
                     b9[b32][router]=float('inf')
    for router in b6:
        for neighbour in b38:
            if (b9[b1][router] > b9[neighbour][router] + b9[b1][neighbour]):
                b41 = b9[neighbour][router] + b9[b1][neighbour]
                b9[b1][router]=b41
                if(router in b38 and b13[b1][router]<=b41):
                     b9[b1][router]=b13[b1][router]
                     b7[router]= 'direct'
                else:
                     b7[router] = neighbour
            elif (len(b7.keys()) != len(b6)):
                b7[router] = 'direct'
            elif(router in b38 and b13[b1][router] <= b9[b1][router]):
                     b9[b1][router]=b13[b1][router]
                     b7[router]= 'direct'
    b5[b1] = b9[b1]
    fonk5()
def fonk5():
        with b8:
            os.system("cls")
            print("\n I am Router " + b1 + '\n')
            for b32 in b5[b1].keys():
                  print(" Least cost path to router " + b32 + " : through " + b7[b32] + " with  cost " +  str("{0:.1f}".format(b5[b1][b32]) + "\n"))
b42 = class1(b1,b2,b3)
threading.Thread(b33 = Sender).start()
threading.Thread(b33 = Recv).start()