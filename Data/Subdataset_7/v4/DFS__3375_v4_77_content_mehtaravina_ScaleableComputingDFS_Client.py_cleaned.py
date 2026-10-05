import socket
import pickle
def fonk1():
    b1 = input("Enter 1 to login, 2 to sign up, 3 to exit: ")
    b23.send(b1.encode())
    b2 = input("Enter b2: ")
    b23.send(b2.encode())
    b3 = input("Enter b3: ")
    b23.send(b3.encode())
    print(b2, b3, b1)
    b4 = b23.recv(1024).decode()
    if b4 = = 'true':
        fonk2()
    elif b4 = = 'false':
        print('Incorrect b3')
        fonk1()
    elif b4 = = 'exists':
        print('Username already exists')
        fonk1()
    else:
        print('Program terminated')
def fonk2():
    b1 = input('Type 1 to create a new file, 2 to access existing file, 3 to exit: ')
    b20.send(b1.encode())
    if b1 = = '1':
        b5 = input('Enter file name: ')
        b20.send(b5.encode())
        b6 = input('Write b7 into file: ')
        b20.send(b6.encode())
        b7 = b20.recv(2048)
        b8 = pickle.loads(b7)
        print(b8)
        fonk2()
    elif b1 = = '2':
        print('Files in the server:')
        b9 = b20.recv(2048)
        b10 = pickle.loads(b9)
        print(b10)
        b5 = input("Enter File Name, type 'exit' to terminate: ")
        b20.send(b5.encode())
        b7 = b20.recv(2048)
        print(b7.decode())
    b11 = input("Type 'open' to access file and 'exit' to quit or 'back' to open another file: ")
    if b11 = = 'open':
        b11 = 'exit'
        fonk3(b5)
    elif b11 = = 'exit':
        b11.encode()
        b20.send(b11.encode())
        print('Application Terminated')
    elif b11 = = 'back':
        fonk2()
def fonk3(f):
    b12 = fonk4(f)
    b13 = ['r', 'a']
    if b12 = = 'locked':
        b14 = input('File is locked for writing, only read b13 available. Type "yes" to continue or "exit" to quit: ')
        if b14 = = 'yes':
            b15 = 'r'
            if b15 = = b13[0]:
                b16 = [f, b13[0]]
                b21.send(str(b16))
                with open('received_file', 'wb') as f1:
                    print('File opened')
                    while True:
                        print('Receiving b7...')
                        b7 = b21.recv(1024)
                        print(b7)
                        if not b7:
                            break
        fonk2()
        f1.close()
    else:
        b14 = input('File unlocked, read and write available. Type "r" to read and "a" to append: ')
        if b14 = = b13[1]:
            b16 = [f, b13[1]]
            b22.send((str(b16[0])).encode())
            b21.send(str(b16))
            b17 = input("What do you want to write to file " + str(b16[0]) + ": ")
            print("Modified content: " + str(b17))
            b21.send(b17.encode())
            print("Changes sent!")
            b22.send('done'.encode())
        else:
            b16 = [f, b13[0]]
            b21.send(str(b16))
            with open('received_file', 'wb') as f1:
                print('File opened')
                while True:
                    print('Receiving b7...')
                    b7 = b21.recv(1024)
                    print(b7)
                    if not b7:
                        break
        fonk2()
        f1.close()
def fonk4(b5):
    b22.send(b5.encode())
    b12 = b22.recv(1024)
    print('Status of file is : ' + str(b12.decode()))
    return b12
if b18 = = '__main__':
    b19 = 'localhost'
    a1 = 5001
    b20 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    b20.connect((b19, a1))
    a2 = 5003
    b21 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    b21.connect((b19, a2))
    a3 = 6002
    b22 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    b22.connect((b19, a3))
    a4 = 5009
    b23 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    b23.connect((b19, a4))
    fonk1()