from PIL import Image, ImageStat
import glob
import numpy as np
import math
def get_luminance(im):
    stat = ImageStat.Stat(im)
    r, g, b = stat.mean
    lum = math.sqrt(0.241 * (r ** 2) + 0.691 * (g ** 2) + 0.068 * (b ** 2))
    return lum
def calculate_distance(avg, image):
    return abs(avg - get_luminance(image))
def adjust_image_luminance(image, target_luminance):
    pixels = image.load()
    modifier = -1 if get_luminance(image) > target_luminance else 1
    while calculate_distance(target_luminance, image) > 1:
        for k in range(image.width):
            for l in range(image.height):
                if not all(i > 245 for i in pixels[k, l]):
                    pixels[k, l] = tuple(x + modifier for x in pixels[k, l])
def main():
    path = 'C:\\folder'
    files = glob.glob(path + '/*.png')
    imagewidth = 256
    imageheight = 256
    lums = [get_luminance(Image.open(filename)) for filename in files]
    average_lum = np.mean(lums)
    print('Starting average luminance:', average_lum, '(standard deviation:', np.std(lums), ')')
    new_lums = []
    for i, filename in enumerate(files):
        im = Image.open(filename)
        adjust_image_luminance(im, average_lum)
        im.save(filename)
        new_lums.append(get_luminance(im))
        print(i, 'done')
    final_average_lum = np.mean(new_lums)
    print('Finishing average luminance:', final_average_lum, '(standard deviation:', np.std(new_lums), ')')
if __name__ == '__main__':
    main()