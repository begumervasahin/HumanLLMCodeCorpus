
import os
import csv
import argparse
import numpy as np
from imageio import imsave
def process_fer2013(csv_path, output_dir):
    width, height = 48, 48
    image_id = 1
    with open(csv_path) as csvfile:
        datareader = csv.reader(csvfile, delimiter=',')
        next(datareader, None)
        for row in datareader:
            emotion, pixels, usage = row[0], row[1], row[2]
            pixels_array = np.asarray(pixels.split(), dtype=np.uint8).reshape(width, height)
            stacked_image = np.dstack([pixels_array] * 3)
            image_folder = os.path.join(output_dir, usage)
            os.makedirs(image_folder, exist_ok=True)
            image_file = os.path.join(image_folder, f"{image_id}_{emotion}.jpg")
            imsave(image_file, stacked_image)
            if image_id % 100 == 0:
                print(f'Processed {image_id} images')
            image_id += 1
    print(f"Finished processing {image_id - 1} images")
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate 3-channel gray images from FER 2013 dataset.")
    parser.add_argument('-f', '--file', required=True, help="Path to the CSV file")
    parser.add_argument('-o', '--output', required=True, help="Path to the output directory")
    args = parser.parse_args()
    process_fer2013(args.file, args.output)