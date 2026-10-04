def fonk1(b3, b4):
    with open(b3, 'wb') as file:
        for ch in b4:
            file.write(ord(ch).to_bytes(1, b1 = 'little'))
def fonk2(b3):
    with open(b3, 'rb') as file:
        while (c := file.read(1)):
            print(c)
if b2 = = '__main__':
    b3 = 'test.txt'
    b4 = 'ä¸­æ'
    fonk1(b3, b4)
    fonk2(b3)