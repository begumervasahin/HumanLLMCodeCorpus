def fonk1(b4: str, b5: str) -> None:
    with open(b4, 'wb') as file:
        file.write(b5.encode('utf-8'))
def fonk2(b4: str) -> None:
    with open(b4, 'rb') as file:
        b1 = file.read()
        print(b1.decode('utf-8', b2 = 'replace'))
if b3 = = '__main__':
    b4 = 'test.txt'
    b5 = 'ä¸­æ'
    fonk1(b4, b5)
    fonk2(b4)