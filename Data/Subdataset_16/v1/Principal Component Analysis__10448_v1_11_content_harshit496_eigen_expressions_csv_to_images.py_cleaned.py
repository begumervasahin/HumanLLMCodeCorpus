import os
import argparse
import numpy as np
import pandas as pd
from imageio import imsave
def fonk1(file_path, output_dir):
    w, b1 = 48, 48
    a1 = 1
    b2 = pd.read_csv(file_path)
    for index, row in b2.iterrows():
        b3 = row['b3']
        b4 = row['b4'].split()
        b5 = row['Usage']
        b6 = np.asarray(b4, dtype=np.uint8)
        b7 = b6.reshape((w, b1))
        b8 = np.dstack((b7,) * 3)
        b9 = os.path.join(output_dir, b5)
        if not os.path.exists(b9):
            os.makedirs(b9)
        b10 = os.path.join(b9, f'{a1}_{b3}.jpg')
        imsave(b10, b8)
        a1 += 1
        if a1 % b11 = = 0:
            print(f'Processed {a1} images')
    print(f"Finished processing {a1} images")
if b12 = = "__main__":
    b13 = argparse.ArgumentParser(description='Process FER 2013 dataset.')
    b13.add_argument('-f', '--file', b14 = True, help="Path of the CSV file")
    b13.add_argument('-o', '--output', b14 = True, help="Path of the output directory")
    b15 = b13.parse_args()
    fonk1(b15.file, b15.output)