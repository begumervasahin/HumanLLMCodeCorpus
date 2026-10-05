import sys
import socket
import select
from collections import namedtuple
import thread
import time
b1 = time.time()
b2 = socket.gethostbyname(socket.gethostname())
b3 = int(sys.argv[1])
b4 = int(sys.argv[2])
b5 = {}
b6 = {}
b7 = {}
b8 = {}
b9 = {}
b10 = {}
b11 = {}
b12 = {}
b13 = {}
a1 = 3
b14 = (len(sys.argv[3:]))/3
b15 = time.time()
b16 = (b2, b3)
b17 = True
if(len(sys.argv[3:])%3 != 0):
    print "incorrect usage, b7 should be listed:ip address, port, b43"
    exit()
while(a1/3 <= b14):
    b18 = sys.argv[a1]
    b19 = int(sys.argv[a1 + 1])
    b20 = int(sys.argv[a1 + 2])
    b21 = (b18, b19)
    b5[b21] = int(b20)
    b8[b21] = int(b20)
    b6[b21] = b21
    b10[b21] = b21
    b7[b21] = b15
    a1 += 3
b9 = b8
def fonk1():
    for b21 in b7:
        b22 = None
        if b8.has_key(b21):
            b22 = "ROUTE_UPDATE" + " " + b2 + " " + str(b3) + " " + str(b8[b21]) + " "
        for v in b5:
            if b22 is None:
                b22 = "ROUTE_UPDATE "
            b22 += str(v[0]) + " " + str(v[1]) + " " + str(b5[v]) + " "
        if b22 is not None:
            b22 += "EOT"
            b26.sendto(b22, (b21[0], b21[1]))
            b1 = time.time()
def fonk2(b35):
    print "SENDING LINKDOWN"
    b22 = "LINKDOWN" + " " + b16[0] + " " + str(b16[1]) + " "
    b26.sendto(b22, (b35[0], b35[1]))
def fonk3(b35):
    print "SENDING LINKUP"
    b22 = "LINKUP" + " " + b16[0] + " " + str(b16[1]) + " "
    b26.sendto(b22, (b35[0], b35[1]))
def fonk4():
    b23 = time.strftime("%H:%M:%S", time.localtime(time.time()))
    print str(b23) + "\tDistance vector list is: "
    for b35 in b5:
        print "b24 = " + b35[0] + ":" + str(b35[1]) + "\tCost=" + str(b5[b35]) +"\t\tLink:"+ str(b6[b35])
def fonk5(broken_node, target_node):
    print "LINK DESTROYED"
    b22 = "LINK_DESTROYED" + " " + b16[0] + " " + str(b16[1]) + " " + broken_node[0] + " " + str(broken_node[1]) + " "
    b26.sendto(b22, (target_node[0], target_node[1]))
def fonk6(self, delay):
    b1 = time.time()
    while b17:
        b23 = time.time()
        b25 = []
        for b21 in b7:
            if(b23 - b7[b21] > b4 * 2):
                print "REMOVING DEACTIVATED NEIGHBOR"
                b13[b21] = b8[b21]
                b25.append(b21)
        for inactive_node in b25:
            if inactive_node in b7:
                b5[inactive_node] == float("inf")
                del b7[inactive_node]
            for key in b6:
                if b6[key] == inactive_node:
                    if key in b7:
                        b5[key] = b8[key]
                    else:
                        b5[inactive_node] = float("inf")
                        b5[key] = float("inf")
                        b6[key] = "no link exists"
            fonk1()
        if (b23 - b1 > b4):
            b1 = time.time()
            fonk1()
        time.sleep(1)
thread.start_new_thread( run, ("thread1", 2, ) )
b26 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
b27 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
b27.bind((b2, b3))
b28 = [b27, sys.stdin]
b29 = [sys.stdin]
time.sleep(1)
while b17:
    try:
        inputready,outputready,b30 = select.select(b28,[],[])
        for b31 in inputready:
            if b31 = = sys.stdin:
                b32 = sys.stdin.readline()
                b32 = b32.split()
                if b32[0] == "LINKDOWN" and len(b32) > 2:
                    b33 = b32[1]
                    b34 = int(b32[2])
                    b35 = (b33, b34)
                    if b35 in b7:
                        b5[b35] = float("inf")
                        b12[b35] = b5[b35]
                    else:
                        print "Node is not a b21, can't Linkdown"
                    for b35 in b12:
                        if b35 in b7:
                            del b7[b35]
                            fonk2(b35)
                            fonk1()
                elif b32[0] == "LINKUP" and len(b32) > 2:
                    b35 = (b33, b34)
                    if b35 not in b7:
                        b7[b35] = time.time()
                        if b35 in b5:
                            b5[b35] = int(b8[b35])
                            fonk3(b35)
                elif b32[0] == "CLOSE":
                    print "Node shutting down"
                    b17 = False
                elif b32[0] == "SHOW_RT":
                    fonk4()
                else:
                    print b32[0] + "Command not recognized"
            else:
                b36 = b31.recv(1024)
                b36 = b36.split()
                if b36[0] == "ROUTE_UPDATE":
                    b37 = b36[1]
                    b38 = int(b36[2])
                    if b36[3] is float("inf"):
                        b39 = b36[3]
                    else:
                        b39 = int(b36[3])
                    b40 = (b37, b38)
                    if(b40 not in b13):
                        if(b7.has_key(b40)):
                            b7[b40] = time.time()
                            if b8.has_key(b40):
                                if(b8[b40] > b39):
                                    b8[b40] = b39
                                    b5[b40] = b39
                            else:
                                print "don't have b21 in b21 distance for some reason"
                        else:
                            b7[b40] = time.time()
                            b8[b40] = b39
                            b5[b40] = b39
                            b6[b40] = b40
                            b10 = b40
                        b41 = False
                        a2 = 4
                        b42 = {}
                        while(b41 is False):
                            if b36[a2+2] == str("inf"):
                                b43 = float("inf")
                            else:
                                b43 = int(b36[a2+2])
                            b42[b36[a2], int(b36[a2+1])] = b43
                            a2 += 3
                            if(b36[a2] == "EOT"):
                                b41 = True
                        for b35 in b42:
                            if b35 in b6:
                                if b40 = = b6[b35] and b35 in b5:
                                    if b42[b35] > b5[b35]:
                                        if b35 in b8:
                                            b44 = b8[b35]
                            if str(b35[0]) != str(b2) or str(b35[1]) != str(b3):
                                if b5.has_key(b35):
                                    if (b8[b40] == float('inf')):
                                        b45 = b8[b40]
                                    else:
                                        b45 = int(b8[b40])
                                    if (b42[b35] == float('inf')):
                                        if b40 = = b6[b35]:
                                            if b35 in b8:
                                                b44 = b8[b35]
                                        b46 = b42[b35]
                                    else:
                                        b46 = int(b42[b35])
                                    if (b5[b35] == float('inf')):
                                        b44 = b5[b35]
                                    else:
                                        b44 = int(b5[b35])
                                    if b45 + b46 < b44:
                                        b5[b35] = b45 + b46
                                        b6[b35] = (b37, b38)
                                else:
                                    b5[b35] = int(b42[b35]) + int(b36[3])
                                    b6[b35] = (b37, b38)
                                    b10[b35] = (b37, b38)
                elif b36[0] == "LINKUP":
                    print "LINKUP"
                    b40 = (b36[1], int(b36[2]))
                    if(b5[b40] == float("inf")):
                        if(b13[b40] is not None):
                            b5[b40] = int(b13[b40])
                            del b13[b40]
                            b7[b40] = time.time()
                            fonk1()
                            print "LINK RESTORED"
                elif b36[0] == "LINKDOWN":
                    b40 = (b36[1], int(b36[2]))
                    b13[b40] = int(b5[b40])
                    b5[b40] = float("inf");
                    del b7[b40]
                    for v in b5:
                        fonk5(b40, v)
                    fonk1()
                    print "LINK DEACTIVATED"
                elif b36[0] == "LINK_DESTROYED":
                    print b36
                    b40 = (b36[1], int(b36[2]))
                    b47 = (b36[3], int(b36[4]))
                    b11[b40] = b47
                    b11[b47] = b40
                    if b47 in b6:
                        if b47 in b5:
                            if b6[b47] == b40:
                                if b47 in b9:
                                    b5[b47] = b9[b47]
                                else:
                                    b5[b47] = float("inf")
                elif b36[0] is not None:
                    print "Unrecognized message received: "
                    print b36
                else:
                    b31.close()
                    b28.remove(b31)
    except socket.error, e:
        if e.errno != errno.EAGAIN:
            raise e
        print "blocking with", len(buf), "remaining"
        select.select([], [b28], [])
        print "unblocked"