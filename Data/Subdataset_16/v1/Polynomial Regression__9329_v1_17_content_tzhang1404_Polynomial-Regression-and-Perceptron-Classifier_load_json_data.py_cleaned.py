import json
import numpy as np
import os
import matplotlib.pyplot as plt
def fonk1(json_path):
    with open(json_path, 'r') as f:
        b1 = json.load(f)
    b2 = np.array(b1[0]).astype(float)
    b3 = 2 * (np.array(b1[1]).astype(float) - 1) - 1
    return b2, b3
if b4 = = "__main__":
    b5 = '../b1'
    b6 = [
        os.path.join(b5, x)
        for x in os.listdir(b5)
        if x.endswith('.json')
    ]
    for data_file in b6:
        b2, b3 = fonk1(data_file)
        plt.figure(b7 = (6, 4))
        plt.scatter(b2[:, 0], b2[:, 1], b8 = b3, cmap='bwr')
        plt.title(data_file)
        plt.savefig(f'{data_file}.png')
        print(b2.shape, b3.shape, data_file)