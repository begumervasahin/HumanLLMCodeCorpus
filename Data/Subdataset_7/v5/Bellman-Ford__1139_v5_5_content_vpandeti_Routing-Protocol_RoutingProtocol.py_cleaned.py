from ast import literal_eval
import pickle
import socket
import sys
import threading
import time
a1 = 5
b1 = sys.argv[1]
b2 = True
with open(b1, 'rb') as file:
    b3 = pickle.load(file)
b4 = dict(b3)
print('Node routing table:')
print(b4)
b5 = time.time()
def fonk1():
    global b1, b3, b2, b4, b5
    while True:
        with open(b1, 'rb') as file:
            b6 = pickle.load(file)
        if b6 != b3:
            b3 = dict(b6)
            print('Updated node routing table:', b3)
            for route in b4:
                if route in b6:
                    b4[route] = b6[route]
            print('Current routing table:', b4)
            print('Time elapsed since start:', time.time() - b5)
            b2 = True
        time.sleep(a1)
def fonk2():
    global b1, b2, b4
    with open('connections', 'r') as json_file:
        b7 = literal_eval(json_file.read())
    print(b7)
    time.sleep(a1)
    try:
        while True:
            if b2:
                for route_node in b7[b1]:
                    b8 = socket.socket()
                    a2 = 12345
                    b8.connect((route_node, a2))
                    b8.settimeout(None)
                    b9 = pickle.dumps(b4)
                    b8.send(b9)
                    b8.close()
                b2 = False
    except Exception as e:
        print(str(e))
def fonk3():
    global b1, b2, b5, b4
    with open('connections', 'r') as json_file:
        b10 = literal_eval(json_file.read())
    print(b10)
    try:
        b11 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        a2 = 12345
        print(a2)
        b11.bind(('', a2))
        b11.listen(12)
        while True:
            connection, b12 = b11.accept()
            print('Connection from', b12)
            b9 = connection.recv(1024)
            b13 = pickle.loads(b9)
            b14 = b10[b1][b12[0]]
            if b14 in b4:
                b15 = b4[b14]
                for neighbour in b13:
                    if neighbour not in b4:
                        b4[neighbour] = b13[neighbour] + b15
                        b2 = True
                    elif b13[neighbour] + b15 < b4[neighbour]:
                        b4[neighbour] = b13[neighbour] + b15
                        b2 = True
                if b2:
                    print('\n')
                    print('Updated routing costs from', b14, ':', b4)
                    print('Time elapsed since start (ms):', time.time() - b5)
            connection.close()
    except Exception as e:
        print(str(e))
if b16 = = '__main__':
    print('Routing node:', b1)
    threading.Thread(b17 = receive_routing_table).start()
    threading.Thread(b17 = send_routing_table).start()
    threading.Thread(b17 = monitor_routing_table).start()
    input()
