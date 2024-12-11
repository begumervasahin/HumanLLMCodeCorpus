import socket as mysoc
import sys
a1 = 5678
a2 = 5677
def fonk1():
    if len(sys.argv) != 4:
        print("Usage: python script.py <b1> <b2> <b3>")
        return
    b1 = sys.argv[1]
    b2 = sys.argv[2]
    b3 = sys.argv[3]
    b4 = fonk2()
    b5 = fonk2()
    b6 = fonk2()
    b7 = fonk3(b3, b2, b1)
    fonk5(b4)
    crsd, b8 = b4.accept()
    print('Got a connection request from a client at', b8)
    fonk6(crsd, b7, b2, b1, b5, b6)
    b4.close()
def fonk2():
    try:
        return mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
    except mysoc.error as err:
        print('Socket open error: ', err)
        sys.exit()
def fonk3(b3, b2, b1):
    b7 = {}
    try:
        with open(b3, "r") as fr:
            for line in fr:
                b9 = line.split()
                if b9[1].strip() != '-':
                    b7[b9[0].strip()] = {'ip': b9[1].strip(), 'flag': b9[2].strip()}
    except IOError as err:
        print('File Open Error: ', err)
        print("Please ensure the desired file to reverse exists in the source folder")
        sys.exit()
    fonk4(b7, b2, mysoc.gethostbyname(b2), 'NS')
    fonk4(b7, b1, mysoc.gethostbyname(b1), 'NS')
    return b7
def fonk4(b7, host, ip, flag):
    if host:
        b7[host] = {'ip': ip, 'flag': flag}
def fonk5(sock):
    try:
        b10 = ('', 50008)
        sock.bind(b10)
        sock.listen(1)
    except mysoc.error as err:
        print('Socket bind error: ', err)
        sys.exit()
def fonk6(crsd, b7, b2, b1, b5, b6):
    while True:
        b11 = crsd.recv(100)
        b12 = b11.decode('utf-8')
        if not b12:
            break
        b13 = fonk7(b12, b7, b2, b1, b5, b6)
        crsd.send(b13.encode('utf-8'))
def fonk7(b12, b7, b2, b1, b5, b6):
    if b12 in b7:
        b13 = f"{b12} {b7[b12]['ip']} {b7[b12]['flag']}"
    else:
        if ".edu" in b12:
            b13 = fonk8(b12, b2, b6, b7)
        elif ".com" in b12:
            b13 = fonk8(b12, b1, b5, b7)
        else:
            b13 = f"{b12} - Error:HOST NOT FOUND"
    return b13
def fonk8(b12, host, rstots, b7):
    if not host:
        return f"{b12} - Error:HOST NOT FOUND"
    try:
        b14 = b7[host]['ip']
        b15 = a1 if "com" in host else a2
        b10 = (b14, b15)
        rstots.connect(b10)
    except mysoc.error as err:
        print('TOTS connect error: ', err)
        sys.exit()
    rstots.send(b12.strip().encode('utf-8'))
    b16 = rstots.recv(100).decode('utf-8')
    return b16
if b17 = = '__main__':
    fonk1()