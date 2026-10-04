import json
import numpy as np
import os
import matplotlib.pyplot as plt
def fonk1(json_path):
    with open(json_path, 'r') as f:
        b1 = json.load(f)
    b2 = np.array(b1[0], dtype=float)
    b3 = 2 * (np.array(b1[1], dtype=float) - 1) - 1
    return b2, b3
def fonk2(b8):
    for data_file in b8:
        b2, b3 = fonk1(data_file)
        plt.figure(b4 = (6, 4))
        plt.scatter(b2[:, 0], b2[:, 1], b5 = b3, cmap='bwr')
        plt.title(os.path.basename(data_file))
        plt.savefig(f'{data_file}.png')
        print(f"{b2.shape} {b3.shape} {data_file}")
if b6 = = "__main__":
    b7 = '../b1'
    b8 = [os.path.join(b7, file) for file in os.listdir(b7) if file.endswith('.json')]
    fonk2(b8)