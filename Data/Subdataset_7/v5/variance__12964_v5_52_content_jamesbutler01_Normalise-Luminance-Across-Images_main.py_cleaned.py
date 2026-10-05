from PIL import Image, ImageStat
import glob
import numpy as np
import math
def fonk1(b11):
    b1 = ImageStat.Stat(b11)
    r, g, b2 = b1.mean
    b3 = math.sqrt(0.241 * (r ** 2) + 0.691 * (g ** 2) + 0.068 * (b2 ** 2))
    return b3
def fonk2(avg, image):
    return abs(avg - fonk1(image))
def fonk3(image, target_luminance):
    b4 = image.load()
    b5 = -1 if fonk1(image) > target_luminance else 1
    while fonk2(target_luminance, image) > 1:
        for k in range(image.width):
            for l in range(image.height):
                if not all(i > 245 for i in b4[k, l]):
                    b4[k, l] = tuple(x + b5 for x in b4[k, l])
def fonk4():
    b6 = 'C:\\folder'
    b7 = glob.glob(b6 + '/*.png')
    a1 = 256
    a2 = 256
    b8 = [fonk1(Image.open(filename)) for filename in b7]
    b9 = np.mean(b8)
    print('Starting average luminance:', b9, '(standard deviation:', np.std(b8), ')')
    b10 = []
    for i, filename in enumerate(b7):
        b11 = Image.open(filename)
        fonk3(b11, b9)
        b11.save(filename)
        b10.append(fonk1(b11))
        print(i, 'done')
    b12 = np.mean(b10)
    print('Finishing average luminance:', b12, '(standard deviation:', np.std(b10), ')')
if b13 = = '__main__':
    fonk4()