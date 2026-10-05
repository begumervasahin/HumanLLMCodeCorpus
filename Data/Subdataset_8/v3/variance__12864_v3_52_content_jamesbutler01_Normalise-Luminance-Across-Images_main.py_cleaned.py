from PIL import Image, ImageStat
import glob
import numpy as np
import math
def calculate_luminance(image):
    stat = ImageStat.Stat(image)
    r_mean, g_mean, b_mean = stat.mean
    luminance = math.sqrt(0.241 * r_mean ** 2 + 0.691 * g_mean ** 2 + 0.068 * b_mean ** 2)
    return luminance
def adjust_image_luminance(image, target_luminance):
    pixels = image.load()
    current_luminance = calculate_luminance(image)
    modifier = -1 if current_luminance > target_luminance else 1
    while abs(target_luminance - calculate_luminance(image)) > 1:
        for x in range(image.width):
            for y in range(image.height):
                if not all(channel > 245 for channel in pixels[x, y]):
                    pixels[x, y] = tuple(max(0, min(channel + modifier, 255)) for channel in pixels[x, y])
def process_images_in_folder(folder_path, image_width=256, image_height=256):
    image_files = glob.glob(f"{folder_path}/*.png")
    luminances = np.array([calculate_luminance(Image.open(filename)) for filename in image_files])
    average_luminance = np.mean(luminances)
    print(f"Starting average luminance: {average_luminance} (standard deviation: {np.std(luminances)})")
    for i, filename in enumerate(image_files):
        image = Image.open(filename)
        adjust_image_luminance(image, average_luminance)
        image.save(filename)
        print(f"Processed {filename} ({i + 1}/{len(image_files)})")
    new_luminances = np.array([calculate_luminance(Image.open(filename)) for filename in image_files])
    print(f"Finishing average luminance: {np.mean(new_luminances)} (standard deviation: {np.std(new_luminances)})")
if __name__ == '__main__':
    folder_path = 'C:\\folder'
    process_images_in_folder(folder_path)