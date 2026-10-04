import os
import argparse
import numpy as np
import pandas as pd
from imageio import imsave
def main(file_path, output_dir):
    w, h = 48, 48
    id = 1
    data = pd.read_csv(file_path)
    for index, row in data.iterrows():
        emotion = row['emotion']
        pixels = row['pixels'].split()
        usage = row['Usage']
        pixels_array = np.asarray(pixels, dtype=np.uint8)
        image = pixels_array.reshape((w, h))
        stacked_image = np.dstack((image,) * 3)
        image_folder = os.path.join(output_dir, usage)
        if not os.path.exists(image_folder):
            os.makedirs(image_folder)
        image_file = os.path.join(image_folder, f'{id}_{emotion}.jpg')
        imsave(image_file, stacked_image)
        id += 1
        if id % 100 == 0:
            print(f'Processed {id} images')
    print(f"Finished processing {id} images")
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process FER 2013 dataset.')
    parser.add_argument('-f', '--file', required=True, help="Path of the CSV file")
    parser.add_argument('-o', '--output', required=True, help="Path of the output directory")
    args = parser.parse_args()
    main(args.file, args.output)