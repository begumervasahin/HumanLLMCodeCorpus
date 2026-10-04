import sys
import json
import numpy as np
import matplotlib.pyplot as plt
from utils import unequal_mean
def fonk1(config_path):
    with open(config_path, 'r') as file:
        return json.load(file)
def fonk2(path, n_trials, loss_type):
    return [np.load(f'{path}/{loss_type}_losses_{trial}.npy') for trial in range(n_trials)]
def fonk3(path, n_trials):
    b1 = [np.load(f'{path}/test_f1_{trial}.npy') for trial in range(n_trials)]
    return np.mean(b1)
def fonk4(b8, b9, save_path):
    b2 = np.arange(len(b8))
    plt.plot(b2, b8, b3 = 'blue', label='Training Loss')
    plt.plot(b2, b9, b3 = 'red', label='Validation Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    plt.savefig(f'{save_path}/training_curve.png')
    plt.close()
def fonk5(directory_path):
    b4 = fonk1(f'{directory_path}/b4.json')
    b5 = fonk2(directory_path, b4['n_trials'], 'train')
    b6 = fonk2(directory_path, b4['n_trials'], 'val')
    b7 = fonk3(directory_path, b4['n_trials'])
    print(f'{directory_path} test F1: {b7}')
    b8 = unequal_mean(b5)
    b9 = unequal_mean(b6)
    fonk4(b8, b9, directory_path)
if b10 = = '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <path_to_directory>")
        sys.exit(1)
    fonk5(sys.argv[1])