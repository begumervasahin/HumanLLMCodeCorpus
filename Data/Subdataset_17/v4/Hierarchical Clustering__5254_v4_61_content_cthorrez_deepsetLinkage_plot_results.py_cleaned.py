import sys
import json
import numpy as np
import matplotlib.pyplot as plt
from utils import unequal_mean
def load_loss_arrays(path, prefix, n_trials):
    return [np.load(f"{path}/{prefix}_{x}.npy") for x in range(n_trials)]
def plot_training_curve(train_means, val_means, path):
    epochs = np.arange(len(train_means))
    plt.figure(figsize=(10, 6))
    plt.plot(epochs, train_means, color='blue', label='Train Loss')
    plt.plot(epochs, val_means, color='red', label='Validation Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    plt.title('Training and Validation Loss Curves')
    plt.grid(True)
    plt.savefig(f"{path}/training_curve.png")
    plt.close()
def main(path):
    config_path = f"{path}/config.json"
    with open(config_path, 'r') as config_file:
        config = json.load(config_file)
    n_trials = config['n_trials']
    train_arrays = load_loss_arrays(path, 'train_losses', n_trials)
    val_arrays = load_loss_arrays(path, 'val_losses', n_trials)
    test_f1_scores = [np.load(f"{path}/test_f1_{x}.npy") for x in range(n_trials)]
    test_f1_mean = np.mean(test_f1_scores)
    print(f"{path} test F1 score: {test_f1_mean:.4f}")
    train_means = unequal_mean(train_arrays)
    val_means = unequal_mean(val_arrays)
    plot_training_curve(train_means, val_means, path)
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <path>")
        sys.exit(1)
    main(sys.argv[1])