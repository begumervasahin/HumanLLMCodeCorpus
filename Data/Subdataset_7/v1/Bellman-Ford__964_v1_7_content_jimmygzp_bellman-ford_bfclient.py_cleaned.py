import sys
import socket
import select
import pickle
from time import time, sleep
import datetime
import copy
a1 = 1
b1 = a1
a2 = 4096
b2 = {}
b3 = {}
b4 = {}
b5 = {}
b6 = (0, 0)
b7 = time()
b8 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
b8.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
b8.setblocking(0)
b9 = socket.gethostbyname(socket.gethostname())
if b9[:3] == '127':
    b9 = '127.0.0.1'
b10 = float("inf")
def fonk1(b22):
    b8.sendto('DOWN', b22)
def fonk2(b22, weight):
    b2[b22] = float(weight)
    b3[b22] = time()
    b4[b22] = 1
    b5[b6][b22] = [b22, float(weight)]
    b5[b22] = {}
    b5[b22][b22] = [b22, 0]
def fonk3(b22, vector):
    b5[b22] = vector
    b5[b6][b22] = [b22, b5[b22][b6][1]]
    b2[b22] = float(b5[b22][b6][1])
def fonk4():
    global b7
    if a1:
        print(b5[b6])
        print(b4)
    for b18, vector in b5.items():
        if b18 is not b6:
            if b1:
                print(b18)
                print(b4[b18])
            if b4[b18] == 1:
                if b1:
                    print("broadcast: sending to b22 " + str(b18))
                b11 = copy.deepcopy(b5[b6])
                for b12, b13 in b5[b6].items():
                    if b13[0] == b18 and b12 != b18:
                        b11[b12][1] = b10
                if a1:
                    print("poisoned message to b18 %s : %s" % (b18, b11))
                    print("actual b5[b6] " + str(b5[b6]))
                b8.sendto(pickle.dumps(b11), b18)
    b7 = time()
def fonk5():
    print(str(datetime.datetime.now()) + ", Current Distance Vector is:")
    for b12, b13 in b5[b6].items():
        if b12 is not b6:
            if a1:
                print("b12 = " + str(b12))
                print("b13 = " + str(b13))
            print("b14 = %s:%d, Cost = %.1f, Link = (%s:%d)" % (b12[0], b12[1], float(b13[1]), b13[0][0], b13[0][1]))
def fonk6():
    a3 = 0
    for b12, b15 in b5[b6].items():
        b13 = b15[0]
        try:
            b5[b6][b12][1] = b5[b6][b13][1] + b5[b13][b12][1]
        except:
            b5[b6][b12][1] = b10
    b13 = ("UNREACHABLE", 0)
    for b12, b15 in b5[b6].items():
        if b12 is not b6:
            if a1:
                print("----updating distance to b12 : " + str(b12))
                print("----old b15 = " + str(b15))
            try:
                if a1:
                    print("^^^^^^^^^^^^^^ TRYING INITIAL CLEANUP")
                    print("b12 = " + str(b12))
                    print("b15[0] = " + str(b12))
                    print("b5[b6][b12]" + str(b5[b6][b12]))
                    print("b5[b15[0]] = " + str(b5[b15[0]]))
                    print("b5[b15[0]][b6][1] = " + str(b5[b15[0]][b6][1]))
                    print("b5[b15[0]][b12][1] = " +  str(b5[b15[0]][b12][1]))
                if b5[b15[0]][b6][1] + b5[b15[0]][b12][1] > b5[b6][b12][1]:
                    b5[b6][b12] = [b12, b5[b15[0]][b6][1] + b5[b15[0]][b12][1]]
            except:
                pass
        b16 = b5[b6][b12][1]
        b17 = b10
        for b18, links in b5.items():
            if b4[b18] and b18 != b6:
                if a1:
                    print("-b18 is not b6, b18 = " + str(b18))
                    print("-b6: " + str(b6))
                try:
                    b19 = b5[b18][b12][1]
                except:
                    b19 = b10
                if a1:
                    print("-b5[b6] = " + str(b5[b6]))
                    print("-b5[b6][b18] = " + str(b5[b6][b18]))
                    print("-b5[b6][b18][1] = " + str(b5[b6][b18][1]))
                    print("-b5[b18][b12][1] = " + str(b19))
                    print("-b16 = " + str(b16))
                if b18 != b12:
                    b20 = b5[b6][b18][1]
                else:
                    b20 = b2[b18]
                if b20 + b19 < b17:
                    if a1:
                        print("-route discovered, b5[%s][%s] + b5[%s][%s] = %s" % (b6, b18, b18, b12, b5[b6][b18][1] + b19))
                    b17 = b20 + b19
                    b13 = b18
        if b16 != b17:
            if a1:
                print("====New route superior; CHANGE RECORDED")
                print("====b16 = " + str(b16))
                print("====b17 = " +str(b17))
                print("====b21 = " + str(b12))
                print("====via b13" + str(b13))
            a3 = 1
            b5[b6][b12] = [b13, b17]
        if a1:
            print("====================================================")
    return a3
def fonk7(client_input):
    b22 = client_input
    if b22[0] == 'localhost' or b22[0][:3] == '127':
        b22 = (b9, client_input[1])
    b4[b22] = 0
    b2[b22] = b5[b6][b22][1]
    b5[b6][b22][1] = b10
    try:
        b5[b22][b6][1] = b10
    except:
        if a1:
            print("don't have the DV for " + str(b22) + " yet.")
    if b1:
        print(b5[b6])
    for b12, b13 in b5[b6].items():
        if a1:
            print("****killing intermediary... b12 = " +