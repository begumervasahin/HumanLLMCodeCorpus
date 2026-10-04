'''
This script creates 3-channel gray images from FER 2013 dataset.
It has been done so that the CNNs designed for RGB images can
be used without modifying the input shape.
This script requires two command line parameters:
1. The path to the CSV file
2. The output directory
It generates the images and saves them in three directories inside
the output directory - Training, PublicTest, and PrivateTest.
These are the three original splits in the dataset.
'''
import os
import csv
import argparse
import numpy as np
import scipy.misc
b1 = argparse.ArgumentParser()
b1.add_argument('-f', '--file', b2 = True, help="path of the csv file")
b1.add_argument('-o', '--output', b2 = True, help="path of the output directory")
b3 = b1.parse_args()
w, b4 = 48, 48
b5 = np.zeros((b4, w), dtype=np.uint8)
a1 = 1
with open(b3.file) as csvfile:
    b6 = csv.reader(csvfile, delimiter =',')
    next(b6,None)
    for row in b6:
        b7 = row[0]
        b8 = row[1].split()
        b9 = row[2]
        b10 = np.asarray(b8, dtype=np.int)
        b5 = b10.reshape(w, b4)
        b11 = np.dstack((b5,) * 3)
        b12 = os.path.join(b3.output, b9)
        if not os.path.exists(b12):
            os.makedirs(b12)
        b13 = os.path.join(b12 , str(a1)+'_'+b7+'.jpg')
        scipy.misc.imsave(b13, b11)
        a1 += 1
        if a1 % b14 = = 0:
            print('Processed {} images'.format(a1))
print("Finished processing {} images".format(a1))