
import os
import csv
import argparse
import numpy as np
from imageio import imsave
def fonk1(csv_path, output_dir):
    width, b1 = 48, 48
    a1 = 1
    with open(csv_path) as csvfile:
        b2 = csv.reader(csvfile, delimiter=',')
        next(b2, None)
        for row in b2:
            emotion, pixels, b3 = row[0], row[1], row[2]
            b4 = np.asarray(pixels.split(), dtype=np.uint8).reshape(width, b1)
            b5 = np.dstack([b4] * 3)
            b6 = os.path.join(output_dir, b3)
            os.makedirs(b6, b7 = True)
            b8 = os.path.join(b6, f"{a1}_{emotion}.jpg")
            imsave(b8, b5)
            if a1 % b9 = = 0:
                print(f'Processed {a1} images')
            a1 += 1
    print(f"Finished processing {a1 - 1} images")
if b10 = = "__main__":
    b11 = argparse.ArgumentParser(description="Generate 3-channel gray images from FER 2013 dataset.")
    b11.add_argument('-f', '--file', b12 = True, help="Path to the CSV file")
    b11.add_argument('-o', '--output', b12 = True, help="Path to the output directory")
    b13 = b11.parse_args()
    fonk1(b13.file, b13.output)