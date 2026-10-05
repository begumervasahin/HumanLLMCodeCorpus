from time import time
b1 = 1024 * 100
def fonk1(c):
    return 64 < c < 91 or 96 < c < 123 or 47 < c < 58 or c in (43, 47, 61)
def fonk2():
    b2 = [[] for _ in range(b1)]
    with open('out', 'rb') as file:
        a1 = 0
        while True:
            b3 = file.read(1)
            if b3:
                b2[a1 % b1].append(ord(b3))
                a1 += 1
            else:
                break
    return b2
def fonk3():
    b2 = fonk2()
    b4 = [[] for _ in range(b1)]
    b5 = time()
    for a1, chunk in enumerate(b2):
        b6 = []
        for value in range(256):
            if all(fonk1(b3 ^ value) for b3 in chunk):
                b6.append(value)
        if len(b6) > 1:
            print('Possible b7 for chunk {}: {}'.format(a1, b6))
        b4[a1] = b6
        if time() - b5 > 5:
            b5 = time()
            print('Progress: {:.2f}%'.format(100 * (a1 / b1)))
    fonk4(b4)
def fonk4(b7):
    with open('key', 'w') as file:
        file.write(str(b7))
def fonk5():
    with open('key', 'r') as file:
        b7 = eval(file.read())
    return b7
if b8 = = '__main__':
    b7 = fonk5()
    b9 = ''
    with open('out', 'rb') as input_file:
        b9 = input_file.read()
    b10 = ''.join(chr(b9[i] ^ b7[i][0]) for i in range(b1))
    print(b10)