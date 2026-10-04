import socket as mysoc
import sys
def fonk1(b11, b10, b9):
    try:
        b1 = {
            b10: {'ip': mysoc.gethostbyname(b10), 'flag': 'NS'},
            b9: {'ip': mysoc.gethostbyname(b9), 'flag': 'NS'}
        }
        with open(b11, "r") as file:
            for line in file:
                b2 = line.split()
                if b2[1].strip() != '-':
                    b1[b2[0].strip()] = {'ip': b2[1].strip(), 'flag': b2[2].strip()}
        return b1
    except IOError as err:
        print('File Open Error:', err)
        print("Please ensure the file exists in the source folder")
        sys.exit(1)
def fonk2():
    try:
        return mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
    except mysoc.error as err:
        print('Socket open error:', err)
        sys.exit(1)
def fonk3(socket, b13, port):
    try:
        b3 = (b13, port)
        socket.connect(b3)
    except mysoc.error as err:
        print(f'Connection error to {b13}:{port}:', err)
        sys.exit(1)
def fonk4(client_socket, b1, b16, b17, b10, b9):
    b4 = True
    b5 = True
    while True:
        b6 = client_socket.recv(100)
        b7 = b6.decode('utf-8').strip()
        if not b7:
            break
        if b7 in b1:
            b8 = f"{b7} {b1[b7]['ip']} {b1[b7]['flag']}"
        else:
            b8 = f"{b7} - Error:HOST NOT FOUND"
            if ".edu" in b7:
                if b5:
                    fonk3(b17, b1[b10]['ip'], 5677)
                    b5 = False
                b17.send(b7.encode('utf-8'))
                b8 = b17.recv(100).decode('utf-8')
            elif ".com" in b7:
                if b4:
                    fonk3(b16, b1[b9]['ip'], 5678)
                    b4 = False
                b16.send(b7.encode('utf-8'))
                b8 = b16.recv(100).decode('utf-8')
        client_socket.send(b8.encode('utf-8'))
def fonk5():
    if len(sys.argv) != 4:
        print("Usage: python script.py <b9> <b10> <b11>")
        sys.exit(1)
    b9 = sys.argv[1]
    b10 = sys.argv[2]
    b11 = sys.argv[3]
    b1 = fonk1(b11, b10, b9)
    b12 = fonk2()
    b12.bind(('', 50008))
    b12.listen(1)
    b13 = mysoc.gethostname()
    b14 = mysoc.gethostbyname(b13)
    print(f"[RS]: Server b13 name is {b13}")
    print(f"[RS]: Server IP address is {b14}")
    client_socket, b15 = b12.accept()
    print(f"[RS]: Got a connection request from a client at {b15}")
    b16 = fonk2()
    b17 = fonk2()
    fonk4(client_socket, b1, b16, b17, b10, b9)
    b12.close()
if b18 = = '__main__':
    fonk5()