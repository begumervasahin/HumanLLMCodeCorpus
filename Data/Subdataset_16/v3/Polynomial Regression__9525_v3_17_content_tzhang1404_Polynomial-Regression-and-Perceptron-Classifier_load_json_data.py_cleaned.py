import json
import numpy as np
import os
import matplotlib.pyplot as plt
def fonk1(json_path):
    with open(json_path, 'r') as file:
        b1 = json.load(file)
    b2 = np.array(b1[0], dtype=float)
    b3 = 2 * (np.array(b1[1], dtype=float) - 1) - 1
    return b2, b3
def fonk2(b7):
    for data_file in b7:
        b2, b3 = fonk1(data_file)
        plt.figure(b4 = (6, 4))
        plt.scatter(b2[:, 0], b2[:, 1], b5 = b3, cmap='bwr')
        plt.title(os.path.basename(data_file))
        plt.savefig(f'{data_file}.png')
        print(f"Features shape: {b2.shape}, Targets shape: {b3.shape}, File: {data_file}")
def fonk3():
    b6 = '../b1'
    b7 = [os.path.join(b6, file) for file in os.listdir(b6) if file.endswith('.json')]
    fonk2(b7)
if b8 = = "__main__":
    fonk3()