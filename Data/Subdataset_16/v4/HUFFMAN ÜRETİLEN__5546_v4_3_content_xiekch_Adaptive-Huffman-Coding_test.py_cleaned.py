def fonk1(b3, b4):
    with open(b3, 'wb') as file:
        for ch in b4:
            file.write(ch.encode('utf-8'))
def fonk2(b3):
    with open(b3, 'rb') as file:
        while (byte := file.read(1)):
            print(byte.decode('utf-8', b1 = 'replace'), end='')
if b2 = = '__main__':
    b3 = 'test.txt'
    b4 = 'ä¸­æ'
    fonk1(b3, b4)
    fonk2(b3)