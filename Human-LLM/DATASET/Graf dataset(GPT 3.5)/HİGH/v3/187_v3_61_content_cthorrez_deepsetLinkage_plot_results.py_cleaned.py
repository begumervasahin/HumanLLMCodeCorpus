import sys
import json
import numpy as np
import matplotlib.pyplot as plt
from utils import unequal_mean
def fonk1(path, b8):
    b1 = [np.load(f'{path}/train_losses_{trial}.npy') for trial in range(b8['n_trials'])]
    b2 = [np.load(f'{path}/val_losses_{trial}.npy') for trial in range(b8['n_trials'])]
    b3 = [np.load(f'{path}/test_f1_{trial}.npy') for trial in range(b8['n_trials'])]
    return b1, b2, b3
def fonk2(b3):
    return np.mean(b3)
def fonk3(b1, b2):
    b4 = unequal_mean(b1)
    b5 = unequal_mean(b2)
    return b4, b5
def fonk4(b4, b5):
    b6 = np.arange(len(b4))
    plt.plot(b6, b4, b7 = 'blue', label='Train')
    plt.plot(b6, b5, b7 = 'red', label='Validation')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    plt.show()
def fonk5(path):
    with open(f'{path}/b8.json') as config_file:
        b8 = json.load(config_file)
    b1, b2, b3 = fonk1(path, b8)
    b9 = fonk2(b3)
    print(f'{path} - Mean test F1 score: {b9}')
    b4, b5 = fonk3(b1, b2)
    fonk4(b4, b5)
if b10 = = '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_experiment_directory>")
        sys.exit(1)
    b11 = sys.argv[1]
    fonk5(b11)