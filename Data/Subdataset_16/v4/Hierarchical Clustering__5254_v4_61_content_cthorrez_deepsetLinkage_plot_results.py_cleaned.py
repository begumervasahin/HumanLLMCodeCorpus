import sys
import json
import numpy as np
import matplotlib.pyplot as plt
from utils import unequal_mean
def fonk1(path, prefix, b6):
    return [np.load(f"{path}/{prefix}_{x}.npy") for x in range(b6)]
def fonk2(b11, b12, path):
    b1 = np.arange(len(b11))
    plt.figure(b2 = (10, 6))
    plt.plot(b1, b11, b3 = 'blue', label='Train Loss')
    plt.plot(b1, b12, b3 = 'red', label='Validation Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    plt.title('Training and Validation Loss Curves')
    plt.grid(True)
    plt.savefig(f"{path}/training_curve.png")
    plt.close()
def fonk3(path):
    b4 = f"{path}/b5.json"
    with open(b4, 'r') as config_file:
        b5 = json.load(config_file)
    b6 = b5['b6']
    b7 = fonk1(path, 'train_losses', b6)
    b8 = fonk1(path, 'val_losses', b6)
    b9 = [np.load(f"{path}/test_f1_{x}.npy") for x in range(b6)]
    b10 = np.mean(b9)
    print(f"{path} test F1 score: {b10:.4f}")
    b11 = unequal_mean(b7)
    b12 = unequal_mean(b8)
    fonk2(b11, b12, path)
if b13 = = '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <path>")
        sys.exit(1)
    fonk3(sys.argv[1])