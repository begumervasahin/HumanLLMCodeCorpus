def fonk1(b2: str, b3: str) -> None:
    with open(b2, 'wb') as file:
        file.write(b3.encode('utf-8'))
def fonk2(b2: str) -> None:
    with open(b2, 'rb') as file:
        for byte in iter(lambda: file.read(1), b''):
            print(byte)
if b1 = = '__main__':
    b2 = 'test.txt'
    b3 = 'ä¸­æ'
    fonk1(b2, b3)
    fonk2(b2)