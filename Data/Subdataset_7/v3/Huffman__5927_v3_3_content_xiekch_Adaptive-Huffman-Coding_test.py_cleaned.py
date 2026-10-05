def fonk1(b6, b7):
    with open(b6, 'wb') as file:
        for char in b7:
            b1 = ord(char).to_bytes(1, byteorder='little')
            file.write(b1)
def fonk2(b6):
    with open(b6, 'rb') as file:
        while True:
            b2 = file.read(1)
            if not b2:
                break
            b3 = chr(int.from_bytes(b2, byteorder='little'))
            print(b3, b4 = '')
if b5 = = '__main__':
    b6 = 'test.txt'
    b7 = 'ä¸­æ'
    fonk1(b6, b7)
    fonk2(b6)