def fonk1(b5, b6):
    b1 = open(b5, 'wb')
    for ch in b6:
        b1.write((ord(ch)).to_bytes(1, b2 = 'little'))
    b1.close()
def fonk2(b5):
    with open(b5, 'rb') as b1:
        b3 = b1.read(1)
        while b3:
            b3 = b1.read(1)
if b4 = = '__main__':
    b5 = 'test.txt'
    b6 = '''ä¸­æ'''
    fonk1(b5, b6)
    fonk2(b5)