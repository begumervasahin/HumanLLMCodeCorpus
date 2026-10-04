import socket as mysoc
import sys
b1 = sys.argv[1]
b2 = sys.argv[2]
b3 = sys.argv[3]
def fonk1(b3, b2, b1):
    b4 = {
        b2: {'ip': mysoc.gethostbyname(b2), 'flag': 'NS'},
        b1: {'ip': mysoc.gethostbyname(b1), 'flag': 'NS'}
    }
    try:
        with open(b3, "r") as file:
            for line in file:
                b5 = line.split()
                if b5[1].strip() != '-':
                    b4[b5[0].strip()] = {'ip': b5[1].strip(), 'flag': b5[2].strip()}
    except IOError as err:
        print('File Open Error:', err)
        print("Please ensure the file exists in the source folder")
        sys.exit(1)
    return b4
def fonk2():
    try:
        return mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
    except mysoc.error as err:
        print('Socket open error:', err)
        sys.exit(1)
def fonk3(socket, b8, port):
    try:
        b6 = (b8, port)
        socket.connect(b6)
    except mysoc.error as err:
        print(f'Connection error to {b8}:{port}:', err)
        sys.exit(1)
def fonk4():
    b4 = fonk1(b3, b2, b1)
    b7 = fonk2()
    b7.bind(('', 50008))
    b7.listen(1)
    b8 = mysoc.gethostname()
    b9 = mysoc.gethostbyname(b8)
    print(f"[RS]: Server b8 name is {b8}")
    print(f"[RS]: Server IP address is {b9}")
    client_socket, b10 = b7.accept()
    print(f"[RS]: Got a connection request from a client at {b10}")
    b11 = fonk2()
    b12 = fonk2()
    b13 = True
    b14 = True
    while True:
        b15 = client_socket.recv(100)
        b16 = b15.decode('utf-8').strip()
        if not b16:
            break
        if b16 in b4:
            b17 = f"{b16} {b4[b16]['ip']} {b4[b16]['flag']}"
        else:
            b17 = f"{b16} - Error:HOST NOT FOUND"
            if ".edu" in b16:
                if b14:
                    fonk3(b12, b4[b2]['ip'], 5677)
                    b14 = False
                b12.send(b16.encode('utf-8'))
                b17 = b12.recv(100).decode('utf-8')
            elif ".com" in b16:
                if b13:
                    fonk3(b11, b4[b1]['ip'], 5678)
                    b13 = False
                b11.send(b16.encode('utf-8'))
                b17 = b11.recv(100).decode('utf-8')
        client_socket.send(b17.encode('utf-8'))
    b7.close()
if b18 = = '__main__':
    fonk4()