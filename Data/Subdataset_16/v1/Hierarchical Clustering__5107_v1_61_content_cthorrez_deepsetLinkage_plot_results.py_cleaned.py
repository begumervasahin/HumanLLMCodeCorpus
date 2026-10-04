import sys
import json
import numpy as np
import matplotlib.pyplot as plt
from utils import unequal_mean
def fonk1(b10):
    with open(f'{b10}/config.json', 'r') as config_file:
        b1 = json.load(config_file)
    b2 = [np.load(f'{b10}/train_losses_{b7}.npy') for b7 in range(b1['n_trials'])]
    b3 = [np.load(f'{b10}/val_losses_{b7}.npy') for b7 in range(b1['n_trials'])]
    b4 = np.mean([np.load(f'{b10}/test_f1_{b7}.npy') for b7 in range(b1['n_trials'])])
    print(f'{b10} test f1:', b4)
    b5 = unequal_mean(b2)
    b6 = unequal_mean(b3)
    b7 = np.arange(len(b5))
    plt.plot(b7, b5, b8 = 'blue', label='train')
    plt.plot(b7, b6, b8 = 'red', label='val')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    plt.savefig(f'{b10}/training_curve.png')
if b9 = = '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <path_to_directory>")
        sys.exit(1)
    b10 = sys.argv[1]
    fonk1(b10)