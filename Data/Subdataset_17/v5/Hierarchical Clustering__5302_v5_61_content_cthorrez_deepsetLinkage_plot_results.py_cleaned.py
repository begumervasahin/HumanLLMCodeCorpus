import sys
import json
import numpy as np
import matplotlib.pyplot as plt
from utils import unequal_mean
def load_loss_arrays(path, prefix, n_trials):
    return [np.load(f"{path}/{prefix}_{trial_idx}.npy") for trial_idx in range(n_trials)]
def plot_training_curve(train_means, val_means, output_path):
    epochs = np.arange(len(train_means))
    plt.figure(figsize=(10, 6))
    plt.plot(epochs, train_means, color='blue', label='Train Loss')
    plt.plot(epochs, val_means, color='red', label='Validation Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    plt.title('Training and Validation Loss Curves')
    plt.grid(True)
    plt.savefig(f"{output_path}/training_curve.png")
    plt.close()
def load_config(config_path):
    with open(config_path, 'r') as config_file:
        return json.load(config_file)
def calculate_mean_test_f1(path, n_trials):
    test_f1_scores = [np.load(f"{path}/test_f1_{trial_idx}.npy") for trial_idx in range(n_trials)]
    return np.mean(test_f1_scores)
def main(path):
    config = load_config(f"{path}/config.json")
    n_trials = config['n_trials']
    train_arrays = load_loss_arrays(path, 'train_losses', n_trials)
    val_arrays = load_loss_arrays(path, 'val_losses', n_trials)
    mean_test_f1 = calculate_mean_test_f1(path, n_trials)
    print(f"{path} test F1 score: {mean_test_f1:.4f}")
    train_means = unequal_mean(train_arrays)
    val_means = unequal_mean(val_arrays)
    plot_training_curve(train_means, val_means, path)
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <path>")
        sys.exit(1)
    main(sys.argv[1])