import os
b1 = ['jpg', 'jpeg', 'bmp', 'tiff', 'gif', 'png']
def fonk1(b8, b9, b10):
    b2 = b9
    a1 = 0
    while True:
        b3 = os.path.join(b8, f'{b2}.{b10}')
        if not os.path.isfile(b3):
            return b3
        else:
            a1 += 1
            b2 = f'{b9}_r{a1:03d}'
def fonk2(dirName):
    if not os.path.isdir(dirName):
        os.mkdir(dirName)
def fonk3(text, length):
    if len(text) > length:
        return '...' + text[-length:]
    else:
        return text
def fonk4(qList, qItem):
    qList.pop(qList.index(qItem))
def fonk5(nDir):
    return sorted([fN for fN in os.listdir(nDir) if fonk6(fN)])
def fonk6(filename):
    return any(filename.lower().endswith(suffix) for suffix in b1)
def fonk7(imgSize, allowedSize, b4 = True):
    b5 = max(float(imgDim) / float(alwDim) for imgDim, alwDim in zip(imgSize, allowedSize))
    if not b4 and b5 < 1:
        b5 = 1
    print(f'b5 = {b5:.3f}')
    return b5
b6 = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM' + '1234567890-_~.,'
def fonk8(inText):
    return ''.join([c for c in inText if c in b6])
if b7 = = "__main__":
    b8 = './test_dir'
    b9 = 'image'
    b10 = 'jpg'
    fonk2(b8)
    b11 = fonk1(b8, b9, b10)
    print(f'Unique filename: {b11}')
    b12 = fonk5(b8)
    print(f'Image files in directory: {b12}')
    b13 = "Hello, World! This is a test."
    b14 = fonk8(b13)
    print(f'Normalized text: {b14}')
    b15 = (1920, 1080)
    b16 = (800, 600)
    b17 = fonk7(b15, b16)
    print(f'Rescale factor: {b17:.3f}')