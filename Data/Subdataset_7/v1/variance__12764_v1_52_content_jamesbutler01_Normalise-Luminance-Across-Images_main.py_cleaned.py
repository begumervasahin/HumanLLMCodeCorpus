from PIL import Image, ImageStat
import glob
import numpy as np
import math
b1 = 'C:\\folder'
b2 = glob.glob(b1 + '/*.png')
a1 = 256
a2 = 256
def fonk1(b7):
    b3 = ImageStat.Stat(b7)
    r, g, b4 = b3.mean
    b5 = math.sqrt(0.241 * (r ** 2) + 0.691 * (g ** 2) + 0.068 * (b4 ** 2))
    return b5
def fonk2(avg, image):
    return abs(avg - fonk1(image))
def fonk3():
    b6 = np.empty(len(b2))
    for i, filename in enumerate(b2):
        b7 = Image.open(filename)
        b6[i] = fonk1(b7)
    b8 = np.mean(b6)
    print('Starting average luminance of', b8, '(stdev', np.std(b6), ')')
    b9 = np.empty(len(b2))
    for i, filename in enumerate(b2):
        b7 = Image.open(filename)
        b10 = b7.load()
        if fonk1(b7) > b8:
            a3 = -1
        else:
            a3 = 1
        while fonk2(b8, b7) > 1:
            for k in range(a1):
                for l in range(a2):
                    if not all(i > 245 for i in b10[k, l]):
                        b10[k, l] = tuple(x + a3 for x in b10[k, l])
        b7.save(filename)
        b9[i] = fonk1(b7)
        print(i, 'done')
    print('Finishing average luminance of', np.mean(b9), '(stdev', np.std(b9), ')')
if b11 = = '__main__':
    fonk3()