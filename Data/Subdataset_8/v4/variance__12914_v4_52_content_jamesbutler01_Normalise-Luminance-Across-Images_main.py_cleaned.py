from PIL import Image, ImageStat
import glob
import numpy as np
import math
path = 'C:\\folder'
files = glob.glob(path + '/*.png')
imagewidth = 256
imageheight = 256
def get_luminance(im):
    stat = ImageStat.Stat(im)
    r, g, b = stat.mean
    lum = math.sqrt(0.241 * (r ** 2) + 0.691 * (g ** 2) + 0.068 * (b ** 2))
    return lum
def distance(avg, image):
    return abs(avg - get_luminance(image))
def main():
    lums = np.empty(len(files))
    for i, filename in enumerate(files):
        im = Image.open(filename)
        lums[i] = get_luminance(im)
    average_lum = np.mean(lums)
    print('Starting average luminance of ', average_lum, '(stdev', np.std(lums), ')')
    new_lums = np.empty(len(files))
    for i, filename in enumerate(files):
        im = Image.open(filename)
        pixels = im.load()
        if get_luminance(im) > average_lum:
            modifier = -1
        else:
            modifier = 1
        while distance(average_lum, im) > 1:
            for k in range(imagewidth):
                for l in range(imageheight):
                    if not all(i > 245 for i in pixels[k, l]):
                        pixels[k, l] = tuple(x + modifier for x in pixels[k, l])
        im.save(filename)
        new_lums[i] = get_luminance(im)
        print(i, 'done')
    print('Finishing average luminance of ', np.mean(new_lums), '(stdev', np.std(new_lums), ')')
if __name__ == '__main__':
    main()