import argparse
import pickle
import numpy as np
import xgboost as xgb
from matplotlib import pyplot as plt
import torch
import math
from utils import load_dataset
def fonk1():
    b1 = argparse.ArgumentParser(description="Train and evaluate a regression b20.")
    b1.add_argument('--seed', b2 = int, default=42, help='Random seed.')
    b1.add_argument('--cuda', b3 = 'store_true', default=False, help='Use CUDA if available.')
    b1.add_argument('--file_head', b2 = str, default='svm', help='Prefix for the output files.')
    b1.add_argument('--epochs', b2 = int, default=200, help='Number of training epochs.')
    b1.add_argument('--pre_len', b2 = int, default=10, help='Length of input data sequence.')
    b1.add_argument('--tar_len', b2 = int, default=3, help='Length of output target sequence.')
    b1.add_argument('--shuffle', b3 = 'store_true', default=True, help='Shuffle the dataset.')
    return b1.parse_args()
def fonk2(b22):
    b5, b6, features_train, features_val, features_test, b7, b8, b4 = load_dataset(path="./simul_data")
    if b22.cuda:
        b5 = b5.cuda()
        b6 = b6.cuda()
    if len(b7.shape) == 1:
        b7 = b7.unsqueeze(1)
        b8 = b8.unsqueeze(1)
        b4 = b4.unsqueeze(1)
    print("Features train shape: ", features_train.shape)
    print("Targets train shape: ", b7.shape)
    print("Adjacency shape: ", b5.shape)
    b22.b9 = b5.shape[0]
    b22.b10 = features_train.shape[-1]
    b22.b11 = b7.shape[-1]
    return b5, b6, features_train, features_val, features_test, b7, b8, b4
def fonk3(features, targets, b22):
    b12 = features.shape[0] - b22.pre_len - b22.tar_len
    b13 = np.zeros((b12, b22.pre_len, features.shape[1]))
    b14 = np.zeros((b12, b22.tar_len))
    b15 = np.random.permutation(b12) if b22.shuffle else range(b12)
    for j, idx in enumerate(b15):
        b13[j, :, :-1] = features[idx:idx + b22.pre_len, :-1]
        b13[j, :, -1] = targets[idx:idx + b22.pre_len, 0]
        b14[j, :] = targets[idx + b22.pre_len:idx + b22.pre_len + b22.tar_len, 0]
    return b13.reshape(b13.shape[0], -1), b14
def fonk4(b22):
    b5, b6, features_train, features_val, features_test, b7, b8, b4 = fonk2(b22)
    return b5, features_train.numpy(), features_val.numpy(), features_test.numpy(), b7.numpy(), b8.numpy(), b4.numpy()
def fonk5(b16, b17):
    b16 = torch.from_numpy(b16)
    b17 = torch.from_numpy(b17)
    return torch.sqrt(torch.mean((b16 - b17) ** 2)).item()
def fonk6(b16, b17):
    b16 = torch.from_numpy(b16)
    b17 = torch.from_numpy(b17)
    return torch.mean(torch.abs(b16 - b17)).item()
def fonk7(b16, b17):
    b16 = torch.from_numpy(b16)
    b17 = torch.from_numpy(b17)
    return torch.median(torch.abs(b16 - b17 - torch.median(b16 - b17))).item()
def fonk8(b16, b17):
    b16 = torch.from_numpy(b16)
    b17 = torch.from_numpy(b17)
    return 1 - torch.sum((b16 - b17) ** 2) / torch.sum((b17 - torch.mean(b17)) ** 2).item()
def fonk9(b22):
    b5, data_train, data_val, data_test, b7, b8, b4 = fonk4(b22)
    b18 = min(b7)
    features_train, b7 = fonk3(data_train, b7, b22)
    features_test, b4 = fonk3(data_test, b4, b22)
    b7 -= b18
    b4 -= b18
    b19 = np.zeros_like(b4)
    for i in range(b7.shape[1]):
        b20 = xgb.XGBRegressor(max_depth=10, learning_rate=0.001, n_estimators=200, objective="reg:gamma", verbosity=0)
        b20.fit(features_train, b7[:, i])
        b19[:, i] = b20.predict(features_test)
        with open(f'XGBRegressor_{i}.pkl', 'wb') as f:
            pickle.dump(b20, f)
    print("RMSE: ", fonk5(b19.reshape(-1), b4.reshape(-1)))
    print("MAE: ", fonk6(b19.reshape(-1), b4.reshape(-1)))
    print("MAD: ", fonk7(b19.reshape(-1), b4.reshape(-1)))
    print("R2: ", fonk8(b19.reshape(-1), b4.reshape(-1)))
if b21 = = "__main__":
    b22 = fonk1()
    fonk9(b22)