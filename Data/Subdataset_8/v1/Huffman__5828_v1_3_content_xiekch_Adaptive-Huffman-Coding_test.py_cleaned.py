def writeFile(fileName, data):
    with open(fileName, 'wb') as file:
        for ch in data:
            file.write((ord(ch)).to_bytes(1, byteorder='little'))
def readFile(fileName):
    with open(fileName, 'rb') as file:
        c = file.read(1)
        while c:
            print(chr(int.from_bytes(c, byteorder='little')), end='')
            c = file.read(1)
if __name__ == '__main__':
    fileName = 'test.txt'
    data =  'ä¸­æ'
    writeFile(fileName, data)
    readFile(fileName)