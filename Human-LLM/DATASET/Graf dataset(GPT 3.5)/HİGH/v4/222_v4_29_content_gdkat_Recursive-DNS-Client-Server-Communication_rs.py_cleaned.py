import socket as mysoc
import sys
def fonk1():
    b1 = sys.argv[1]
    b2 = sys.argv[2]
    b3 = sys.argv[3]
    try:
        b4 = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        b5 = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        b6 = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
    except mysoc.error as err:
        print('Socket open error:', err)
    try:
        b7 = open(b3, "r")
    except IOError as err:
        print('File Open Error:', err)
        print("Please ensure the desired file to reverse exists in the source folder")
        exit()
    b8 = {}
    b9 = b2
    b8[b9] = {'ip': mysoc.gethostbyname(b9), 'flag': 'NS'}
    b10 = b1
    b8[b10] = {'ip': mysoc.gethostbyname(b10), 'flag': 'NS'}
    for line in b7:
        b11 = line.split()
        if b11[1].strip() != '-':
            b8[b11[0].strip()] = {'ip': b11[1].strip(), 'flag': b11[2].strip()}
    if not b9:
        print("Warning: no TS.b9 server to redirect miss")
    if not b10:
        print("Warning: no TS.b10 server to redirect miss")
    b12 = ('', 50008)
    b4.bind(b12)
    b4.listen(1)
    b13 = mysoc.gethostname()
    print("Server b13 name is:", b13)
    b14 = (mysoc.gethostbyname(b13))
    print("Attempting to connect to the client.")
    print("Server IP address is", b14)
    crsd, b15 = b4.accept()
    print("Got a connection request from a client at", b15)
    b16 = True
    b17 = True
    while True:
        b18 = crsd.recv(100)
        b19 = b18.decode('utf-8')
        if not b19:
            break
        b20 = ""
        if b19 in b8:
            b20 = b19 + ' ' + b8[b19]['ip'] + ' ' + b8[b19]['flag']
        else:
            if ".b9" in b19:
                if not b9:
                    b20 = b19 + " - Error: HOST NOT FOUND"
                else:
                    if b16:
                        b16 = False
                        try:
                            b21 = b8[b9]['ip']
                            a1 = 5677
                            b12 = (b21, a1)
                            b6.connect(b12)
                        except mysoc.error as err:
                            print('TSEDU connect error:', err)
                            exit()
                    b6.send(b19.strip().encode('utf-8'))
                    b22 = b6.recv(100).decode('utf-8')
                    if not b22:
                        break
                    b20 = b22
            elif ".b10" in b19:
                if not b10:
                    b20 = b19 + " - Error: HOST NOT FOUND"
                else:
                    if b17:
                        b17 = False
                        try:
                            b21 = b8[b10]['ip']
                            a1 = 5678
                            b12 = (b21, a1)
                            b5.connect(b12)
                        except mysoc.error as err:
                            print('TSCOM connect error:', err)
                            exit()
                    b5.send(b19.strip().encode('utf-8'))
                    b22 = b5.recv(100).decode('utf-8')
                    if not b22:
                        break
                    b20 = b22
            else:
                b20 = b19 + " - Error: HOST NOT FOUND"
        crsd.send(b20.encode('utf-8'))
    b7.close()
    b4.close()
fonk1()