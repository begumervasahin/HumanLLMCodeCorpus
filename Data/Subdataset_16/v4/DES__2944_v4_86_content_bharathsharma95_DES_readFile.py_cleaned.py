def fonk1(b4):
    b1 = []
    with open(b4, 'rb') as file:
        while byte := file.read(1):
            b1.append(byte)
    return b1
def fonk2(b4):
    b2 = fonk1(b4)
    print(b2)
if b3 = = "__main__":
    b4 = 'path/to/your/file'
    fonk2(b4)