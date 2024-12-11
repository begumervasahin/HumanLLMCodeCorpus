from base64 import b64encode
from time import time
b1 = 1024 * 100
def fonk1(b2):
    return ((64 < b2 < 91) or
            (96 < b2 < 123) or
            (47 < b2 < 58) or
            (b2 = = 43) or
            (b2 = = 47) or
            (b2 = = 61))
def fonk2():
    b3 = [[] for _ in range(b1)]
    with open('out', 'rb') as f:
        a1 = 0
        b4 = False
        while not b4:
            b2 = f.read(1)
            if b2 != b'':
                b3[a1 % b1].append(ord(b2))
                a1 += 1
            else:
                b4 = True
    return b3
def fonk3():
    b5 = fonk2()
    b6 = [[] for _ in range(b1)]
    b7 = time()
    for j in range(b1):
        b8 = b5[j]
        b9 = []
        for a1 in range(2**8):
            b10 = True
            for b2 in b8:
                if not fonk1(b2 ^ a1):
                    b10 = False
                    break
            if b10:
                b9.append(a1)
        if len(b9) > 1:
            print('Potential b11 values for ka[{}]: {}'.format(j, b9))
        b6[j] = b9
        if time() - b7 > 5:
            b7 = time()
            print('Progress: {:.4f}%'.format(100 * (j / b1)))
    fonk4(b6)
def fonk4(b11):
    with open('b11', 'w') as f:
        f.write(str(b11))
def fonk5():
    with open('b11', 'r') as f:
        b11 = eval(f.read())
    return b11
if b12 = = '__main__':
    b11 = fonk5()
    b13 = ''
    with open('out', 'rb') as f_in:
        b13 = f_in.read()
    b14 = ''.join([chr(b13[a1] ^ b11[a1][0]) for a1 in range(b1)])
    print(b14)