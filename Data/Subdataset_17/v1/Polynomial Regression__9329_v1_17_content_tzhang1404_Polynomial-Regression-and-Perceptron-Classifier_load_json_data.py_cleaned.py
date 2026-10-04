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
if __name__ == "__main__":
    data_dir = '../data'
    data_files = [
        os.path.join(data_dir, x)
        for x in os.listdir(data_dir)
        if x.endswith('.json')
    ]
    for data_file in data_files:
        features, targets = load_json_data(data_file)
        plt.figure(figsize=(6, 4))
        plt.scatter(features[:, 0], features[:, 1], c=targets, cmap='bwr')
        plt.title(data_file)
        plt.savefig(f'{data_file}.png')
        print(features.shape, targets.shape, data_file)