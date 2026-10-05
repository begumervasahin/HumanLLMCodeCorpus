from ast import literal_eval
import pickle
import socket
import sys
import threading
import time
a1 = 5
b1 = sys.argv[1]
a2 = 1
def fonk1(file_path):
    with open(file_path, 'rb') as file:
        return pickle.load(file)
def fonk2(b3, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(b3, file)
def fonk3():
    global b1, a2
    b2 = fonk1(b1)
    b3 = dict(b2)
    while True:
        b4 = fonk1(b1)
        if b4 != b2:
            b2 = dict(b4)
            for route in b3:
                if route in b4:
                    b3[route] = b4[route]
            print('Current routing table:', b3)
            print('Pick time:', time.time() - b13)
            a2 = 1
        time.sleep(a1)
def fonk4(b3, routing_paths):
    global b1, a2
    while True:
        if a2:
            for route_node in routing_paths[b1]:
                b5 = socket.socket()
                a3 = 12345
                b5.connect((route_node, a3))
                b5.settimeout(None)
                b6 = pickle.dumps(b3)
                b5.send(b6)
                b5.close()
            a2 = 0
        time.sleep(a1)
def fonk5(node_connections):
    global b1, b13
    b7 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    a3 = 12345
    b7.bind(('', a3))
    b7.listen(12)
    while True:
        connection, b8 = b7.accept()
        print('Connection from', b8)
        b6 = connection.recv(1024)
        b9 = pickle.loads(b6)
        b10 = node_connections[b1][b8[0]]
        if b10 in b3:
            b11 = b3[b10]
            for neighbour in b9:
                if neighbour not in b3:
                    b3[neighbour] = b9[neighbour] + b11
                    a2 = 1
                elif b9[neighbour] + b11 < b3[neighbour]:
                    b3[neighbour] = b9[neighbour] + b11
                    a2 = 1
            if a2:
                print('\n')
                print('Updated routing costs:', b10, ':', b3)
                print('Elapsed time in ms:', time.time() - b13)
        connection.close()
if b12 = = '__main__':
    global b13, b1
    b13 = time.time()
    print(b1)
    threading.Thread(b14 = monitor_routing_table).start()
    threading.Thread(b14 = update_neighboring_nodes, args=(b3, literal_eval(open('connections', 'r').read()))).start()
    threading.Thread(b14 = handle_incoming_connections, args=(literal_eval(open('connections', 'r').read()),)).start()
    input()
