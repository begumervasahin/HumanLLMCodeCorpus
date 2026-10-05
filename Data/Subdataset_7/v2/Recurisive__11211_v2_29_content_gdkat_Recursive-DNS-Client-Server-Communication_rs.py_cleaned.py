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
        print('Socket open error: ', err)
        return
    try:
        b7 = open(b3, "r")
    except IOError as err:
        print('File Open Error: ', err)
        print("Please ensure the desired file to reverse exists in the source folder")
        return
    b8 = {}
    b9 = b2
    b10 = b1
    if b9:
        b8[b9] = {'ip': mysoc.gethostbyname(b9), 'flag': 'NS'}
    if b10:
        b8[b10] = {'ip': mysoc.gethostbyname(b10), 'flag': 'NS'}
    for line in b7:
        b11 = line.split()
        if b11[1].strip() != '-':
            b8[b11[0].strip()] = {'ip': b11[1].strip(), 'flag': b11[2].strip()}
    try:
        b12 = ('', 50008)
        b4.bind(b12)
        b4.listen(1)
    except mysoc.error as err:
        print('Socket bind error: ', err)
        return
    crsd, b13 = b4.accept()
    print('Got a connection request from a client at', b13)
    while True:
        b14 = crsd.recv(100)
        b15 = b14.decode('utf-8')
        if not b15:
            break
        b16 = fonk2(b15, b8, b9, b10, b5, b6)
        crsd.send(b16.encode('utf-8'))
    b7.close()
    b4.close()
def fonk2(b15, b8, b9, b10, b5, b6):
    if b15 in b8:
        b16 = b15 + ' ' + b8[b15]['ip'] + ' ' + b8[b15]['flag']
    else:
        if ".b9" in b15:
            b16 = fonk3(b15, b9, b6, b8)
        elif ".b10" in b15:
            b16 = fonk3(b15, b10, b5, b8)
        else:
            b16 = b15 + " - Error:HOST NOT FOUND"
    return b16
def fonk3(b15, host, rstots, b8):
    if not host:
        return b15 + " - Error:HOST NOT FOUND"
    try:
        b17 = b8[host]['ip']
        b18 = 5678 if "b10" in host else 5677
        b12 = (b17, b18)
        rstots.connect(b12)
    except mysoc.error as err:
        print('TOTS connect error: ', err)
        exit()
    rstots.send(b15.strip().encode('utf-8'))
    b19 = rstots.recv(100).decode('utf-8')
    return b19
if b20 = = '__main__':
    fonk1()