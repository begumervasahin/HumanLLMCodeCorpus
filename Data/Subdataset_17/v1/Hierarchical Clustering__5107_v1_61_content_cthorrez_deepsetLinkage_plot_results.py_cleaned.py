import sys
import json
import numpy as np
import matplotlib.pyplot as plt
from utils import unequal_mean
def main(path):
    with open(f'{path}/config.json', 'r') as config_file:
        args = json.load(config_file)
    train_arrays = [np.load(f'{path}/train_losses_{x}.npy') for x in range(args['n_trials'])]
    val_arrays = [np.load(f'{path}/val_losses_{x}.npy') for x in range(args['n_trials'])]
    test_f1 = np.mean([np.load(f'{path}/test_f1_{x}.npy') for x in range(args['n_trials'])])
    print(f'{path} test f1:', test_f1)
    train_means = unequal_mean(train_arrays)
    val_means = unequal_mean(val_arrays)
    x = np.arange(len(train_means))
    plt.plot(x, train_means, color='blue', label='train')
    plt.plot(x, val_means, color='red', label='val')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    plt.savefig(f'{path}/training_curve.png')
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <path_to_directory>")
        sys.exit(1)
    path = sys.argv[1]
    main(path)