from PIL import Image, ImageStat
import glob
import numpy as np
import math
def fonk1(b11):
    b1 = ImageStat.Stat(b11)
    r_mean, g_mean, b2 = b1.mean
    b3 = math.sqrt(0.241 * r_mean ** 2 + 0.691 * g_mean ** 2 + 0.068 * b2 ** 2)
    return b3
def fonk2(b11, target_luminance):
    b4 = b11.load()
    b5 = fonk1(b11)
    b6 = -1 if b5 > target_luminance else 1
    while abs(target_luminance - fonk1(b11)) > 1:
        for x in range(b11.width):
            for y in range(b11.height):
                if not all(channel > 245 for channel in b4[x, y]):
                    b4[x, y] = tuple(max(0, min(channel + b6, 255)) for channel in b4[x, y])
def fonk3(b14, b7 = 256, image_height=256):
    b8 = glob.glob(f"{b14}/*.png")
    b9 = np.array([fonk1(Image.open(filename)) for filename in b8])
    b10 = np.mean(b9)
    print(f"Starting average b3: {b10} (standard deviation: {np.std(b9)})")
    for i, filename in enumerate(b8):
        b11 = Image.open(filename)
        fonk2(b11, b10)
        b11.save(filename)
        print(f"Processed {filename} ({i + 1}/{len(b8)})")
    b12 = np.array([fonk1(Image.open(filename)) for filename in b8])
    print(f"Finishing average b3: {np.mean(b12)} (standard deviation: {np.std(b12)})")
if b13 = = '__main__':
    b14 = 'C:\\folder'
    fonk3(b14)