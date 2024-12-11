def fonk1(b4, b5):
    with open(b4, 'wb') as file:
        for ch in b5:
            file.write((ord(ch)).to_bytes(1, b1 = 'little'))
def fonk2(b4):
    with open(b4, 'rb') as file:
        while True:
            b2 = file.read(1)
            if not b2:
                break
if b3 = = '__main__':
    b4 = 'test.txt'
    b5 = 'ä¸­æ'
    fonk1(b4, b5)
    fonk2(b4)