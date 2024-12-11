from base64 import b64encode
from time import time
b1 = 1024 * 100
def fonk1(b4):
    b2 = ord(b4)
    return (64 < b2 < 91) or (96 < b2 < 123) or (47 < b2 < 58) or \
           (b2 in [43, 47, 61])
def fonk2():
    b3 = [[] for _ in range(b1)]
    with open('out', 'rb') as f:
        a1 = 0
        while True:
            b4 = f.read(1)
            if b4 = = b'':
                break
            b3[a1 % b1].append(ord(b4))
            a1 += 1
    return b3
def fonk3():
    b5 = fonk2()
    b6 = [[] for _ in range(b1)]
    b7 = time()
    for j in range(b1):
        b8 = b5[j]
        b9 = []
        for a1 in range(256):
            if all(fonk1(c ^ a1) for c in b8):
                b9.append(a1)
        b6[j] = b9
        if len(b9) > 1:
            print('Potential b10 values for ka[{}]: {}'.format(j, b9))
        if time() - b7 > 5:
            b7 = time()
            print('Progress: {:.4f}%'.format(100 * (j / b1)))
    fonk4(b6)
def fonk4(b10):
    with open('b10', 'w') as f:
        f.write(str(b10))
def fonk5():
    with open('b10', 'r') as f:
        b10 = eval(f.read())
    return b10
def fonk6():
    b10 = fonk5()
    with open('out', 'rb') as f_in:
        b11 = f_in.read()
    b12 = ''.join([chr(b11[a1] ^ b10[a1][0]) for a1 in range(b1)])
    print(b12)
if b13 = = '__main__':
    fonk3()
    fonk6()