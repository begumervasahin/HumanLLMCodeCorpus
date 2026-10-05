import sys
import json
import numpy as np
import matplotlib.pyplot as plt
from utils import unequal_mean
def main(path):
    with open(f"{path}/config.json") as config_file:
        config = json.load(config_file)
    train_losses = [np.load(f"{path}/train_losses_{x}.npy") for x in range(config["n_trials"])]
    val_losses = [np.load(f"{path}/val_losses_{x}.npy") for x in range(config["n_trials"])]
    test_f1_scores = [np.load(f"{path}/test_f1_{x}.npy") for x in range(config["n_trials"])]
    mean_test_f1 = np.mean(test_f1_scores)
    print(f"{path} - Test F1 score: {mean_test_f1}")
    train_means = unequal_mean(train_losses)
    val_means = unequal_mean(val_losses)
    epochs = np.arange(len(train_means))
    plt.plot(epochs, train_means, color="blue", label="Train")
    plt.plot(epochs, val_means, color="red", label="Validation")
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.legend()
    plt.savefig(f"{path}/training_curve.png")
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <experiment_directory>")
        sys.exit(1)
    main(sys.argv[1])