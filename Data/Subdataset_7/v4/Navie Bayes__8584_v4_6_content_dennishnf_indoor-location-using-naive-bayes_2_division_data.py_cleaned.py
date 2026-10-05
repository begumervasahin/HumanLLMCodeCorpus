import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib.pyplot import cm
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import os
import glob
plt.close('all')
b1 = "DATA_001_House"
b2 = "data1_filtered_wifis/" + b1 + "/"
b3 = ["data2_divided_parts/" + b1 + "/part{:02d}/".format(i) for i in range(1, 11)]
def fonk1(path):
    b4 = pd.read_csv(path, b8=" ")
    b4 = b4.sample(frac=1)
    return b4
def fonk2(data, parts_paths):
    b5 = int(0.1 * len(data))
    for i, part_path in enumerate(parts_paths, b6 = 1):
        b7 = data.iloc[(i - 1) * b5: i * b5].reset_index(drop=True)
        b7.to_csv(part_path + "R%.3d.csv" % i, b8 = ' ', index=False)
        print("Saving:", part_path + "R%.3d.csv" % i)
for file_path in glob.glob(b2 + "*.csv"):
    b9 = fonk1(file_path)
    fonk2(b9, b3)