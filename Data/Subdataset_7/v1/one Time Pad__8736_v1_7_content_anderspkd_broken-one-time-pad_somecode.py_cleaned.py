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
    with open('out', 'rb') as b12:
        a1 = 0
        b4 = False
        while not b4:
            b2 = b12.read(1)
            if b2 != b9'':
                b3[a1 % b1] += [ord(b2)]
                a1 += 1
                continue
            b4 = True
    return b3
def fonk3():
    b3 = fonk2()
    b5 = [[] for _ in range(b1)]
    a2 = 0
    b6 = time()
    for a2 in range(b1):
        b7 = b3[a2]
        b8 = []
        for a1 in range(2 ** 8):
            b9 = False
            for b2 in b7:
                if fonk1(b2 ^ a1):
                    continue
                b9 = True
            if not b9:
                b8 += [a1]
        if len(b8) > 1:
            print('b5[{}]: {}'.format(a2, b8))
        b5[a2] = b8
        if time() - b6 > 5:
            b6 = time()
            print('Progress: {:4f}%'.format(100 * (float(a2) / b1)))
    fonk4(b5)
def fonk4(b10):
    with open('key', 'w') as b12:
        b12.write(str(b10))
def fonk5():
    with open('key', 'r') as b12:
        b10 = eval(b12.read())
    return b10
if b11 = = '__main__':
    b10 = fonk5()
    b12 = ''
    with open('out', 'rb') as f_in:
        b12 = f_in.read()
    b13 = ''.join([chr(b12[a1] ^ b10[a1][0]) for a1 in range(b1)])
    print(b13)