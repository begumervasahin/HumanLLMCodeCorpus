import sys
import json
import numpy as np
import matplotlib.pyplot as plt
from utils import unequal_mean
def load_config(config_path):
    with open(config_path, 'r') as file:
        return json.load(file)
def load_loss_arrays(path, n_trials, loss_type):
    return [np.load(f'{path}/{loss_type}_losses_{trial}.npy') for trial in range(n_trials)]
def calculate_mean_test_f1(path, n_trials):
    test_f1_scores = [np.load(f'{path}/test_f1_{trial}.npy') for trial in range(n_trials)]
    return np.mean(test_f1_scores)
def plot_training_curve(train_means, val_means, save_path):
    epochs = np.arange(len(train_means))
    plt.plot(epochs, train_means, color='blue', label='Training Loss')
    plt.plot(epochs, val_means, color='red', label='Validation Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    plt.savefig(f'{save_path}/training_curve.png')
    plt.close()
def main(directory_path):
    config = load_config(f'{directory_path}/config.json')
    train_arrays = load_loss_arrays(directory_path, config['n_trials'], 'train')
    val_arrays = load_loss_arrays(directory_path, config['n_trials'], 'val')
    mean_test_f1 = calculate_mean_test_f1(directory_path, config['n_trials'])
    print(f'{directory_path} test F1: {mean_test_f1}')
    train_means = unequal_mean(train_arrays)
    val_means = unequal_mean(val_arrays)
    plot_training_curve(train_means, val_means, directory_path)
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <path_to_directory>")
        sys.exit(1)
    main(sys.argv[1])