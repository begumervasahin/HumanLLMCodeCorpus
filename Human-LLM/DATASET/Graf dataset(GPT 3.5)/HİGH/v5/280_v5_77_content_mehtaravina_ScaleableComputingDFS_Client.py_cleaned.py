import socket
import pickle
def fonk1():
    b1 = input("Enter 1 to login, 2 to sign up, 3 to exit: ")
    b22.send(b1.encode())
    b2 = input("Enter b2: ")
    b22.send(b2.encode())
    b3 = input("Enter b3: ")
    b22.send(b3.encode())
    print(b2, b3, b1)
    b4 = b22.recv(1024).decode()
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
    b19.send(b1.encode())
    if b1 = = '1':
        fonk3()
    elif b1 = = '2':
        fonk4()
def fonk3():
    b5 = input('Enter file name: ')
    b19.send(b5.encode())
    b6 = input('Write b7 into file: ')
    b19.send(b6.encode())
    b7 = b19.recv(2048)
    b8 = pickle.loads(b7)
    print(b8)
    fonk2()
def fonk4():
    print('Files in the server:')
    b9 = b19.recv(2048)
    b10 = pickle.loads(b9)
    print(b10)
    b5 = input("Enter File Name, type 'exit' to terminate: ")
    b19.send(b5.encode())
    b7 = b19.recv(2048)
    print(b7.decode())
    b11 = input("Type 'open' to access file and 'exit' to quit or 'back' to open another file: ")
    if b11 = = 'open':
        b11 = 'exit'
        fonk5(b5)
    elif b11 = = 'exit':
        b11.encode()
        b19.send(b11.encode())
        print('Application Terminated')
    elif b11 = = 'back':
        fonk2()
def fonk5(f):
    b12 = fonk6(f)
    b13 = ['r', 'a']
    if b12 = = 'locked':
        b14 = input('File is locked for writing, only read b13 available. Type "yes" to continue or "exit" to quit: ')
        if b14 = = 'yes':
            fonk7(f)
    else:
        b14 = input('File unlocked, read and write available. Type "r" to read and "a" to append: ')
        if b14 = = b13[1]:
            fonk8(f)
        else:
            fonk7(f)
def fonk6(b5):
    b21.send(b5.encode())
    b12 = b21.recv(1024)
    print('Status of file is : ' + str(b12.decode()))
    return b12
def fonk7(f):
    b15 = [f, 'r']
    b20.send(str(b15))
    with open('received_file', 'wb') as f1:
        print('File opened')
        while True:
            print('Receiving b7...')
            b7 = b20.recv(1024)
            print(b7)
            if not b7:
                break
    fonk2()
    f1.close()
def fonk8(f):
    b15 = [f, 'a']
    b21.send((str(b15[0])).encode())
    b20.send(str(b15))
    b16 = input("What do you want to write to file " + str(b15[0]) + ": ")
    print("Modified content: " + str(b16))
    b20.send(b16.encode())
    print("Changes sent!")
    b21.send('done'.encode())
    fonk2()
if b17 = = '__main__':
    b18 = 'localhost'
    a1 = 5001
    b19 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    b19.connect((b18, a1))
    a2 = 5003
    b20 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    b20.connect((b18, a2))
    a3 = 6002
    b21 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    b21.connect((b18, a3))
    a4 = 5009
    b22 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    b22.connect((b18, a4))
    fonk1()