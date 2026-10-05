import threading
import time
import math
from socket import socket, AF_INET, SOCK_DGRAM
a1 = 3.0
class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
    def fonk2(self, path2):
        return self.b1 = = path2.b1 and self.b2 == path2.b2
class class2:
    def fonk3(self, b3, b4, b5):
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        self.b6 = {}
b7 = str()
b8 = int()
b9 = str()
b10 = {}
b11 = {}
b12 = threading.Lock()
def fonk4(dest_id, send_link_cost):
    b13 = str(b7)
    if send_link_cost:
        b13 += ' ' + str(b10[dest_id].b3)
    b13 += '\n'
    for b28, path in b11.items():
        if path.b2 = = dest_id:
            b13 += str(b28) + " " + str(math.inf) + '\n'
        else:
            b13 += str(b28) + " " + str(path.b1) + '\n'
    return bytes(b13, 'utf-8')
def fonk5(send_link_cost):
    b14 = socket(AF_INET, SOCK_DGRAM)
    b12.acquire()
    for b28, neighbour in b10.items():
        b14.sendto(fonk4(b28, send_link_cost), ('localhost', neighbour.b4))
    b12.release()
    b14.close()
def fonk6():
    b15 = '\t'
    for b28 in sorted(b11.keys()):
        b15 += '\t' + b28
    print(b15)
    b15 = b7 + '\t'
    for b28 in sorted(b11.keys()):
        b15 += '\t' + str("%.1f" % b11[b28].b1)
    print(b15)
    for b28 in sorted(b10.keys()):
        b15 = b28+'\t'+str(b10[b28].b3)
        for key2 in sorted(b10[b28].b6.keys()):
            b15 += '\t' + str("%.1f" % b10[b28].b6[key2].b1)
        print(b15)
    print('')
def fonk7():
    while True:
        time.sleep(1)
        for b28, neighbour in b10.items():
            b16 = socket(AF_INET, SOCK_DGRAM)
            try:
                b16.bind(('localhost', neighbour.b4))
                b16.close()
                if b10[b28].b3 != math.inf:
                    b12.acquire()
                    b11[b28].b1 = math.inf
                    neighbour.b3 = math.inf
                    neighbour.b5 = time.time()
                    for key2, item2 in b11.items():
                        if item2.b2 = = b28:
                            item2.b1 = math.inf
                    b12.release()
                    fonk5(False)
                    threading.Timer(a1, b17 = bellManFord).start()
            except:
                pass
def fonk8():
    b18 = socket(AF_INET, SOCK_DGRAM)
    b18.bind(('localhost', b8))
    while True:
        message, b19 = b18.recvfrom(2048)
        b20 = str(message)[2:len(str(message))-1].split('\\n')
        b21 = b20[0].split()
        b22 = b21[0]
        b10[b22].b5 = -1.0
        if len(b21) > 1:
            b10[b22].b3 = float(b21[1])
            b10[b22].b5 = -1
        b12.acquire()
        for i in range(1, len(b20)):
            if b20[i] == '':
                continue
            b23 = b20[i].split()
            b24 = class1(float(b23[1]),'direct')
            if b23[0] not in b10[b22].b6:
                fonk9(b23[0])
            if not b10[b22].b6[b23[0]].fonk2(b24):
                b10[b22].b6[b23[0]] = b24
        threading.Thread(b17 = bellManFord).start()
        b12.release()
def fonk9(name):
    global b10
    b25 = class1(math.inf, 'direct')
    b11[name] = b25
    for b28, neighbour in b10.items():
        neighbour.b6[name] = b25
def fonk10():
    global b11
    b26 = False
    b12.acquire()
    for b28, route in b11.items():
        b27 = []
        if b28 = = b7:
            continue
        if b28 in b10:
            if time.time() > b10[b28].b5 and time.time() < b10[b28].b5 + a1:
                b11[b28] = class1(math.inf, 'direct')
                continue
            else:
                b27.append(class1(b10[b28].b3, 'direct'))
        for id2, neighbour in b10.items():
            b25 = class1(b10[id2].b3 + neighbour.b6[b28].b1, id2)
            b27.append(b25)
        b27.append(b25)
        b29 = min(b27, key=lambda x: x.b1)
        if not b11[b28].fonk2(class1(b29.b1, b29.b2)):
            b11[b28] = class1(b29.b1, b29.b2)
            b26 = True
    b12.release()
    if b26:
        fonk5(False)
def fonk11():
    a2 = 0
    while True:
        print('\n****I AM ROUTER ' + b7 + '****\n')
        a2 = int(input('1: Display Costs.\n2: Display b1 vector table.\n3: Edit link costs\n4: Quit\nYour choice: '))
        if a2 = = 1:
            print('Destination\tNext Hop\tDistance')
            for b28, route in sorted(b11.items()):
                if b28 != b7:
                    print('     ' + b28 + '\t\t' + route.b2 + '\t\t' + str("%.1f" % route.b1))
        elif a2 = = 2:
            fonk6()
        elif a2 = = 3:
            b15 = 'Neighbours:'
            for b28 in sorted(b10.keys()):
                b15 += ' ' + b28
            print(b15)
            b30 = input('Enter which link to edit: ')
            b31 = float(input('Enter new b1 for ' + b30 + ': '))
            b10[b30].b3 = b31
            b32 = socket(AF_INET, SOCK_DGRAM)
            b12.acquire()
            b32.sendto(fonk4(b30, True), ('localhost', b10[b30].b4))
            b12.release()
            b32.close()
            threading.Thread(b17 = bellManFord).start()
        elif a2 = = 4:
            os._exit(-1)
if b33 = = '__main__':
    try:
        b7 = sys.argv[1]
        b8 = int(sys.argv[2])
        b9 =