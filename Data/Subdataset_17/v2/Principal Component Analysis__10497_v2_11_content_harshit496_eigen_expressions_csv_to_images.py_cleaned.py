import os
import argparse
import numpy as np
import pandas as pd
from imageio import imsave
def process_fer2013_dataset(file_path, output_dir):
    img_width, img_height = 48, 48
    img_id = 1
    data = pd.read_csv(file_path)
    for _, row in data.iterrows():
        emotion = row['emotion']
        pixels = row['pixels'].split()
        usage = row['Usage']
        pixels_array = np.asarray(pixels, dtype=np.uint8)
        image = pixels_array.reshape((img_width, img_height))
        stacked_image = np.dstack((image,) * 3)
        image_folder = os.path.join(output_dir, usage)
        os.makedirs(image_folder, exist_ok=True)
        image_file = os.path.join(image_folder, f'{img_id}_{emotion}.jpg')
        imsave(image_file, stacked_image)
        img_id += 1
        if img_id % 100 == 0:
            print(f'Processed {img_id} images')
    print(f"Finished processing {img_id} images")
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process the FER 2013 dataset to create 3-channel grayscale images.')
    parser.add_argument('-f', '--file', required=True, help="Path to the CSV file containing the FER 2013 dataset")
    parser.add_argument('-o', '--output', required=True, help="Path to the output directory where images will be saved")
    args = parser.parse_args()
    process_fer2013_dataset(args.file, args.output)