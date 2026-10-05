import sys
import json
import numpy as np
import matplotlib.pyplot as plt
from utils import unequal_mean
def main(path):
    with open(path + '/config.json') as config_file:
        config = json.load(config_file)
    train_losses = [np.load(f'{path}/train_losses_{trial}.npy') for trial in range(config['n_trials'])]
    val_losses = [np.load(f'{path}/val_losses_{trial}.npy') for trial in range(config['n_trials'])]
    test_f1_scores = [np.load(f'{path}/test_f1_{trial}.npy') for trial in range(config['n_trials'])]
    mean_test_f1 = np.mean(test_f1_scores)
    print(f'{path} - Mean test F1 score: {mean_test_f1}')
    train_means = unequal_mean(train_losses)
    val_means = unequal_mean(val_losses)
    epochs = np.arange(len(train_means))
    plt.plot(epochs, train_means, color='blue', label='Train')
    plt.plot(epochs, val_means, color='red', label='Validation')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    plt.savefig(f'{path}/training_curve.png')
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_experiment_directory>")
        sys.exit(1)
    experiment_path = sys.argv[1]
    main(experiment_path)