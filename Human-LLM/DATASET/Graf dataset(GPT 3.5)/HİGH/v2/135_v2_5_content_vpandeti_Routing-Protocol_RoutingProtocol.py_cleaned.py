from ast import literal_eval
import pickle
import socket
import sys
import threading
import time
a1 = 5
b1 = sys.argv[1]
a2 = 1
with open(b1, 'rb') as file:
    b2 = pickle.load(file)
b3 = dict(b2)
print('Node routing table:')
print(b3)
b4 = time.time()
def fonk1():
    global b1, b2, a2, b3
    while True:
        with open(b1, 'rb') as file:
            b5 = pickle.load(file)
        if b5 != b2:
            b2 = dict(b5)
            print('Node routing table:', b2)
            for route in b3:
                if route in b5:
                    b3[route] = b5[route]
            print('Current routing table:', b3)
            print('Pick time:', time.time() - b4)
            a2 = 1
        time.sleep(a1)
def fonk2():
    global b1, a2
    b6 = open('connections', 'r')
    b7 = literal_eval(b6.read())
    print(b7)
    time.sleep(a1)
    try:
        while True:
            if a2:
                for route_node in b7[b1]:
                    b8 = socket.socket()
                    a3 = 12345
                    b8.connect((route_node, a3))
                    b8.settimeout(None)
                    b9 = pickle.dumps(b3)
                    b8.send(b9)
                    b8.close()
                a2 = 0
    except Exception as e:
        print(str(e))
def fonk3():
    global b1, a2, b4
    b6 = open('connections', 'r')
    b10 = literal_eval(b6.read())
    print(b10)
    try:
        b11 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        a3 = 12345
        print(a3)
        b11.bind(('', a3))
        b11.listen(12)
        while True:
            connection, b12 = b11.accept()
            print('Connection from', b12)
            b9 = connection.recv(1024)
            b13 = pickle.loads(b9)
            b14 = b10[b1][b12[0]]
            if b14 in b3:
                b15 = b3[b14]
                for neighbour in b13:
                    if neighbour not in b3:
                        b3[neighbour] = b13[neighbour] + b15
                        a2 = 1
                    else:
                        if b13[neighbour] + b15 < b3[neighbour]:
                            b3[neighbour] = b13[neighbour] + b15
                            a2 = 1
                if a2:
                    print('\n')
                    print('Updated routing costs:', b14, ':', b3)
                    print('Elapsed time in ms:', time.time() - b4)
            connection.close()
    except Exception as e:
        print(str(e))
if b16 = = '__main__':
    global b4, b1
    b4 = time.time()
    print(b1)
    threading.Thread(b17 = server_thread).start()
    threading.Thread(b17 = client_thread).start()
    threading.Thread(b17 = monitor).start()
    input()
