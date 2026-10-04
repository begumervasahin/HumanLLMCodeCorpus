import json
import numpy as np
import os
import matplotlib.pyplot as plt
def load_json_data(json_path):
    with open(json_path, 'r') as f:
        data = json.load(f)
    features = np.array(data[0]).astype(float)
    targets = 2 * (np.array(data[1]).astype(float) - 1) - 1
    return features, targets
def visualize_data(data_files):
    for data_file in data_files:
        features, targets = load_json_data(data_file)
        plt.figure(figsize=(6, 4))
        plt.scatter(features[:, 0], features[:, 1], c=targets, cmap='coolwarm', edgecolor='k')
        plt.title(os.path.basename(data_file))
        plt.savefig(f'{data_file}.png')
        plt.close()
        print(f"Features shape: {features.shape}, Targets shape: {targets.shape}, File: {data_file}")
if __name__ == "__main__":
    data_directory = '../data'
    data_files = [
        os.path.join(data_directory, file)
        for file in os.listdir(data_directory)
        if file.endswith('.json')
    ]
    visualize_data(data_files)