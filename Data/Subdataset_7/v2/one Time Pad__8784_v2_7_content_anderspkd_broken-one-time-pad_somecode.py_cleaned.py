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
    with open('out', 'rb') as file:
        a1 = 0
        b4 = False
        while not b4:
            b5 = file.read(1)
            if b5 != b'':
                b3[a1 % b1] += [ord(b5)]
                a1 += 1
                continue
            b4 = True
    return b3
def fonk3():
    b3 = fonk2()
    b6 = [[] for _ in range(b1)]
    b7 = time()
    for a1 in range(b1):
        b8 = b3[a1]
        b9 = []
        for value in range(2 ** 8):
            b10 = True
            for b5 in b8:
                if not fonk1(b5 ^ value):
                    b10 = False
                    break
            if b10:
                b9.append(value)
        if len(b9) > 1:
            print('Possible b11 for b8 {}: {}'.format(a1, b9))
        b6[a1] = b9
        if time() - b7 > 5:
            b7 = time()
            print('Progress: {:.2f}%'.format(100 * (a1 / b1)))
    fonk4(b6)
def fonk4(b11):
    with open('key', 'w') as file:
        file.write(str(b11))
def fonk5():
    with open('key', 'r') as file:
        b11 = eval(file.read())
    return b11
if b12 = = '__main__':
    b11 = fonk5()
    b13 = ''
    with open('out', 'rb') as input_file:
        b13 = input_file.read()
    b14 = ''.join([chr(b13[i] ^ b11[i][0]) for i in range(b1)])
    print(b14)