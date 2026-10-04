import json
import numpy as np
import os
import matplotlib.pyplot as plt
def load_json_data(json_path):
    with open(json_path, 'r') as file:
        data = json.load(file)
    features = np.array(data[0], dtype=float)
    targets = 2 * (np.array(data[1], dtype=float) - 1) - 1
    return features, targets
def visualize_and_save_data(data_files):
    for data_file in data_files:
        features, targets = load_json_data(data_file)
        plt.figure(figsize=(6, 4))
        plt.scatter(features[:, 0], features[:, 1], c=targets, cmap='bwr')
        plt.title(os.path.basename(data_file))
        plt.savefig(f'{data_file}.png')
        print(f"Features shape: {features.shape}, Targets shape: {targets.shape}, File: {data_file}")
def main():
    data_dir = '../data'
    data_files = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if file.endswith('.json')]
    visualize_and_save_data(data_files)
if __name__ == "__main__":
    main()