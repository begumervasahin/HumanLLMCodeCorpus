from ast import literal_eval
import pickle
import socket
import sys
import thread
import time
a1 = 5
b1 = sys.argv[1]
a2 = 1
b2 = open(b1, 'r')
b3 = pickle.loads(b2.read())
b2.close()
b4 = dict(b3)
print 'node routing table'
print b4
b5 = time.time()
def fonk1():
    global b1, b3, a2, b4
    while 1:
        b2 = open(b1, 'r')
        b6 = pickle.loads(b2.read())
        b2.close()
        if b6 != b3:
            b3 = dict(b6)
            print 'node routing table :', b3
            for route in b4:
                if route in b6:
                    b4[route] = b6[route]
            print 'b14'
            print 'current routing table: ', b4, "; pick time: ", time.time() - b5
            a2 = 1
        time.sleep(a1)
def fonk2():
    global b3
def fonk3():
    global b1, a2
    b7 = open('connections', 'r')
    b8 = literal_eval(b7.read())
    print b8
    time.sleep(a1)
    try:
        while 1:
            if a2:
                for route_node in b8[b1]:
                    b9 = socket.socket()
                    a3 = 12345
                    b9.connect((route_node, a3))
                    b9.settimeout(None)
                    b10 = pickle.dumps(b4)
                    b9.send(b10)
                    b9.close()
                a2 = 0
    except Exception, e:
        print str(e)
def fonk4():
    global b1, a2, b5
    b7 = open('connections', 'r')
    b11 = literal_eval(b7.read())
    print b11
    try:
        b12 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        a3 = 12345
        print a3
        b12.bind(('', a3))
        b12.listen(12)
        while 1:
            connection, b13 = b12.accept()
            print 'connection from', b13
            b10 = connection.recv(1024)
            b14 = pickle.loads(b10)
            b15 = b11[b1][b13[0]]
            if b15 in b4:
                b16 = b4[b15]
                for neighbour in b14:
                    if neighbour not in b4:
                        b4[neighbour] = b14[neighbour] + b16
                        a2 = 1
                    else:
                        if b14[neighbour] + b16 < b4[neighbour]:
                            b4[neighbour] = b14[neighbour] + b16
                            a2 = 1
                if a2:
                    print '\n \n'
                    print 'updated routing costs: ', b15, ': ', b4
                    print " Elapsed time in ms: ", time.time() - b5
            connection.close()
    except Exception, e:
        print str(e)
if b17 = = '__main__':
    global b5, b1
    b5 = time.time()
    print b1
    thread.start_new_thread(server_thread, ())
    thread.start_new_thread(client_thread, ())
    thread.start_new_thread(monitor, ())
    input()