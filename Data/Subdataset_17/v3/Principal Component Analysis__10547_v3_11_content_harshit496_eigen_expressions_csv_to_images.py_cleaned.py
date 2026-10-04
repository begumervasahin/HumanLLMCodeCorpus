import os
import argparse
import numpy as np
import pandas as pd
from imageio import imsave
def process_fer2013_dataset(file_path, output_dir):
    IMG_WIDTH, IMG_HEIGHT = 48, 48
    image_id = 1
    data = pd.read_csv(file_path)
    for _, row in data.iterrows():
        emotion = row['emotion']
        pixels = row['pixels'].split()
        usage = row['Usage']
        pixels_array = np.asarray(pixels, dtype=np.uint8)
        image = pixels_array.reshape((IMG_WIDTH, IMG_HEIGHT))
        stacked_image = np.dstack((image,) * 3)
        image_folder = os.path.join(output_dir, usage)
        os.makedirs(image_folder, exist_ok=True)
        image_file = os.path.join(image_folder, f'{image_id}_{emotion}.jpg')
        imsave(image_file, stacked_image)
        image_id += 1
        if image_id % 100 == 0:
            print(f'Processed {image_id} images')
    print(f"Finished processing {image_id} images")
def parse_arguments():
    parser = argparse.ArgumentParser(description='Process the FER 2013 dataset to create 3-channel grayscale images.')
    parser.add_argument('-f', '--file', required=True, help="Path to the CSV file containing the FER 2013 dataset")
    parser.add_argument('-o', '--output', required=True, help="Path to the output directory where images will be saved")
    return parser.parse_args()
if __name__ == "__main__":
    args = parse_arguments()
    process_fer2013_dataset(args.file, args.output)