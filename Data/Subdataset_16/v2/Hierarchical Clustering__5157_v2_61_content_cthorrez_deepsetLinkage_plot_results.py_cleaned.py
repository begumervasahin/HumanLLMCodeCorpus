import sys
import json
import numpy as np
import matplotlib.pyplot as plt
from utils import unequal_mean
def fonk1(path):
    b1 = f'{path}/b2.json'
    with open(b1, 'r') as file:
        b2 = json.load(file)
    return b2
def fonk2(path, n_trials, loss_type):
    return [np.load(f'{path}/{loss_type}_losses_{trial}.npy') for trial in range(n_trials)]
def fonk3(path, n_trials):
    b3 = [np.load(f'{path}/test_f1_{trial}.npy') for trial in range(n_trials)]
    return np.mean(b3)
def fonk4(b9, b10, path):
    b4 = np.arange(len(b9))
    plt.plot(b4, b9, b5 = 'blue', label='Training Loss')
    plt.plot(b4, b10, b5 = 'red', label='Validation Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    plt.savefig(f'{path}/training_curve.png')
    plt.close()
def fonk5(path):
    b2 = fonk1(path)
    b6 = fonk2(path, b2['n_trials'], 'train')
    b7 = fonk2(path, b2['n_trials'], 'val')
    b8 = fonk3(path, b2['n_trials'])
    print(f'{path} test F1: {b8}')
    b9 = unequal_mean(b6)
    b10 = unequal_mean(b7)
    fonk4(b9, b10, path)
if b11 = = '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <path_to_directory>")
        sys.exit(1)
    fonk5(sys.argv[1])