import socket, pickle
def fonk1():
    b1 = raw_input("Enter 1 to login, 2 to sign up, 3 to exit: ")
    b26.send(b1.encode())
    b2 = raw_input("Enter b2: ")
    b26.send(b2.encode())
    b3 = raw_input("Enter b3: ")
    b26.send(b3.encode())
    print(b2, b3, b1)
    b4 = (b26.recv(1024)).decode()
    if b4 = = 'true':
        fonk2()
    elif b4 = = 'false':
        print 'Incorrect b3'
        fonk1()
    elif b4 = = 'exists':
        print 'Username already exists'
        fonk1()
    else:
        print'Program terminated'
def fonk2():
    b5 = raw_input('Type 1 to create a new file, and 2 to access existing file, 3 to exit ')
    b23.send(b5.encode())
    if b5 = = '1':
        b6 = raw_input('enter file name ')
        b23.send(b6.encode())
        b7 = raw_input('Write b8 into file: ')
        b23.send(b7.encode())
        b8 = b23.recv(2048)
        b9 = pickle.loads(b8)
        print b9
        fonk2()
    elif b5 = = '2':
        print 'Files in the server: '
        b10 = b23.recv(2048)
        b11 = pickle.loads(b10)
        print b11
        b12 = raw_input("Enter File Name, type exit to terminate: ")
        b23.send(b12.encode())
        b8 = b23.recv(2048)
        b13 = b8.decode()
        print b13
    b14 = raw_input("Type open to access file and exit to quit or back to open another file ")
    if b14 = = 'open':
        b15 = 'exit'
        fonk3(b12)
    elif b14 = = 'exit':
        b14.encode()
        b23.send(b14.encode())
        print'Application Terminated'
    elif b14 = = 'back':
        fonk2()
def fonk3(f):
    b16 = fonk4(f)
    b17 = ['r', 'a']
    if b16 = = 'locked':
        b18 = raw_input ('File is locked for writing, only read b17 avaliable. Type yes to continue or exit to quit ')
        if b18 = = 'yes':
            b19 = 'r'
            if b19 = = b17[0] :
                b20 = [f, b17[0]]
                b24.send(str(b20))
                with open('received_file', 'wb') as f1:
                    print 'file opened'
                    while True:
                        print('receiving b8...')
                        b8 = b24.recv(1024)
                        print b8
                        if not b8:
                            break
        fonk2()
        f1.close()
    else:
        b19 = raw_input('File unlocked, read and write avaliable. Type r to read and a to append ')
        if(b19 = = b17[1]):
            b20 = [f, b17[1]]
            b25.send((str(b20[0])).encode())
            b24.send(str(b20))
            b13 = raw_input("What do you want to write to file  " + str(b20[0]))
            print "Modified content: " + str(b13)
            b24.send(b13)
            print "Changes sent!"
            b25.send('done'.encode())
        else:
            b20 = [f, b17[0]]
            b24.send(str(b20))
            with open('received_file', 'wb') as f1:
                print 'file opened'
                while True:
                    print('receiving b8...')
                    b8 = b24.recv(1024)
                    print b8
                    if not b8:
                        break
        fonk2()
        f1.close()
def fonk4(b12):
    b25.send(b12.encode())
    b16 = b25.recv(1024)
    print ('Status of file is : ' +str(b16.decode()))
    return b16
if b21 = = '__main__':
    b22 = 'localhost'
    a1 = 5001
    b23 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    b23.connect((b22, a1))
    b24 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    a2 = 5003
    b24.connect((b22, a2))
    a3 = 6002
    b25 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    b25.connect((b22, a3))
    a4 = 5009
    b26 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    b26.connect((b22, a4))
    fonk1()