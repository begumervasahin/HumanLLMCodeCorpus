from PIL import Image, ImageStat
import glob
import numpy as np
import math
def fonk1(b10):
    b1 = ImageStat.Stat(b10)
    r, g, b2 = b1.mean
    return math.sqrt(0.241 * r**2 + 0.691 * g**2 + 0.068 * b2**2)
def fonk2(b10, target_luminance):
    b3 = b10.load()
    b4 = fonk1(b10)
    b5 = -1 if b4 > target_luminance else 1
    while abs(target_luminance - fonk1(b10)) > 1:
        for x in range(b10.width):
            for y in range(b10.height):
                if not all(channel > 245 for channel in b3[x, y]):
                    b3[x, y] = tuple(max(0, min(channel + b5, 255)) for channel in b3[x, y])
def fonk3(folder_path, b6 = 256, image_height=256):
    b7 = glob.glob(f"{folder_path}/*.png")
    b8 = np.array([fonk1(Image.open(filename)) for filename in b7])
    b9 = np.mean(b8)
    print(f"Starting average luminance: {b9} (stdev {np.std(b8)})")
    for i, filename in enumerate(b7):
        b10 = Image.open(filename)
        fonk2(b10, b9)
        b10.save(filename)
        print(f"{i} done")
    b11 = np.array([fonk1(Image.open(filename)) for filename in b7])
    print(f"Finishing average luminance: {np.mean(b11)} (stdev {np.std(b11)})")
if b12 = = '__main__':
    b13 = 'C:\\folder'
    fonk3(b13)