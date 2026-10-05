import sys
import json
import numpy as np
import matplotlib.pyplot as plt
from utils import unequal_mean
def fonk1(path):
    with open(path + '/b1.json') as config_file:
        b1 = json.load(config_file)
    b2 = [np.load(f'{path}/train_losses_{trial}.npy') for trial in range(b1['n_trials'])]
    b3 = [np.load(f'{path}/val_losses_{trial}.npy') for trial in range(b1['n_trials'])]
    b4 = [np.load(f'{path}/test_f1_{trial}.npy') for trial in range(b1['n_trials'])]
    b5 = np.mean(b4)
    print(f'{path} - Mean test F1 score: {b5}')
    b6 = unequal_mean(b2)
    b7 = unequal_mean(b3)
    b8 = np.arange(len(b6))
    plt.plot(b8, b6, b9 = 'blue', label='Train')
    plt.plot(b8, b7, b9 = 'red', label='Validation')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    plt.savefig(f'{path}/training_curve.png')
if b10 = = '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_experiment_directory>")
        sys.exit(1)
    b11 = sys.argv[1]
    fonk1(b11)