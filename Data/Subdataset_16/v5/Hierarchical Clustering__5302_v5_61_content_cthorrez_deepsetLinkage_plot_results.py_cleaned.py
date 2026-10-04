import sys
import json
import numpy as np
import matplotlib.pyplot as plt
from utils import unequal_mean
def fonk1(path, prefix, b6):
    return [np.load(f"{path}/{prefix}_{trial_idx}.npy") for trial_idx in range(b6)]
def fonk2(b10, b11, output_path):
    b1 = np.arange(len(b10))
    plt.figure(b2 = (10, 6))
    plt.plot(b1, b10, b3 = 'blue', label='Train Loss')
    plt.plot(b1, b11, b3 = 'red', label='Validation Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    plt.title('Training and Validation Loss Curves')
    plt.grid(True)
    plt.savefig(f"{output_path}/training_curve.png")
    plt.close()
def fonk3(config_path):
    with open(config_path, 'r') as config_file:
        return json.load(config_file)
def fonk4(path, b6):
    b4 = [np.load(f"{path}/test_f1_{trial_idx}.npy") for trial_idx in range(b6)]
    return np.mean(b4)
def fonk5(path):
    b5 = fonk3(f"{path}/b5.json")
    b6 = b5['b6']
    b7 = fonk1(path, 'train_losses', b6)
    b8 = fonk1(path, 'val_losses', b6)
    b9 = fonk4(path, b6)
    print(f"{path} test F1 score: {b9:.4f}")
    b10 = unequal_mean(b7)
    b11 = unequal_mean(b8)
    fonk2(b10, b11, path)
if b12 = = '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <path>")
        sys.exit(1)
    fonk5(sys.argv[1])