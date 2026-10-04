import os
import argparse
import numpy as np
import pandas as pd
from imageio import imsave
def fonk1(file_path, output_dir):
    img_width, b1 = 48, 48
    a1 = 1
    b2 = pd.read_csv(file_path)
    for _, row in b2.iterrows():
        b3 = row['b3']
        b4 = row['b4'].split()
        b5 = row['Usage']
        b6 = np.asarray(b4, dtype=np.uint8)
        b7 = b6.reshape((img_width, b1))
        b8 = np.dstack((b7,) * 3)
        b9 = os.path.join(output_dir, b5)
        os.makedirs(b9, b10 = True)
        b11 = os.path.join(b9, f'{a1}_{b3}.jpg')
        imsave(b11, b8)
        a1 += 1
        if a1 % b12 = = 0:
            print(f'Processed {a1} images')
    print(f"Finished processing {a1} images")
if b13 = = "__main__":
    b14 = argparse.ArgumentParser(description='Process the FER 2013 dataset to create 3-channel grayscale images.')
    b14.add_argument('-f', '--file', b15 = True, help="Path to the CSV file containing the FER 2013 dataset")
    b14.add_argument('-o', '--output', b15 = True, help="Path to the output directory where images will be saved")
    b16 = b14.parse_args()
    fonk1(b16.file, b16.output)