def fonk1(b4, b5):
    with open(b4, 'wb') as file:
        for char in b5:
            file.write((ord(char)).to_bytes(1, b1 = 'little'))
def fonk2(b4):
    with open(b4, 'rb') as file:
        b2 = file.read(1)
        while b2:
            print(chr(int.from_bytes(b2, b1 = 'little')), end='')
            b2 = file.read(1)
if b3 = = '__main__':
    b4 = 'test.txt'
    b5 = 'ä¸­æ'
    fonk1(b4, b5)
    fonk2(b4)