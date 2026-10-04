import argparse
import xgboost as xgb
from matplotlib import pyplot as plt
import numpy as np
from scipy import sparse
from sklearn.metrics import make_scorer
from sklearn.svm import SVR
import pickle
import torch
import math
from utils import load_dataset
def fonk1():
    b1 = argparse.ArgumentParser(description="Train a regression b25.")
    b1.add_argument('--seed', b2 = int, default=42, help='Random seed.')
    b1.add_argument('--cuda', b3 = 'store_true', default=False, help='Use CUDA for GPU acceleration.')
    b1.add_argument('--file_head', b2 = str, default='svm', help='Which regression b25 to use.')
    b1.add_argument('--epochs', b2 = int, default=200, help='Number of epochs to train.')
    b1.add_argument('--pre_len', b2 = int, default=10, help='The length of input data sequence.')
    b1.add_argument('--tar_len', b2 = int, default=3, help='The length of output target sequence.')
    b1.add_argument('--shuffle', b3 = 'store_true', default=True, help='Whether to shuffle the dataset.')
    return b1.parse_args()
def fonk2(b27):
    b5, b6, features_train, features_val, features_test, \
        b7, b8, b4 = load_dataset(path="./simul_data")
    if b27.cuda:
        b5 = b5.cuda()
        b6 = b6.cuda()
    if len(b7.shape) == 1:
        b7 = b7.unsqueeze(1)
        b8 = b8.unsqueeze(1)
        b4 = b4.unsqueeze(1)
    print(f"features_train shape: {features_train.shape}")
    print(f"b7 shape: {b7.shape}")
    print(f"b5 shape: {b5.shape}")
    b27.b9 = b5.shape[0]
    b27.b10 = features_train.shape[-1]
    b27.b11 = b7.shape[-1]
    return b5, b6, features_train, features_val, features_test, \
           b7, b8, b4
def fonk3(features, targets, b27):
    b12 = features.shape[0] - b27.pre_len - b27.tar_len
    b13 = np.zeros([b12, b27.pre_len, features.shape[1]])
    b14 = np.zeros([b12, b27.tar_len])
    b15 = np.random.permutation(b12) if b27.shuffle else range(b12)
    for j, idx in enumerate(b15):
        b13[j, :, :-1] = features[idx:idx+b27.pre_len, :-1]
        b13[j, :, -1] = targets[idx:idx+b27.pre_len, 0]
        b14[j, :] = targets[idx+b27.pre_len:idx+b27.pre_len+b27.tar_len, 0]
    return b13.reshape(b12, -1), b14
def fonk4(b27):
    b5, b6, features_train, features_val, features_test, \
        b7, b8, b4 = fonk2(b27)
    return b5, features_train.numpy(), features_val.numpy(), features_test.numpy(), \
           b7.numpy(), b8.numpy(), b4.numpy()
def fonk5(b16, b17):
    b16 = torch.from_numpy(b16)
    b17 = torch.from_numpy(b17)
    b18 = b16 - b17
    return (torch.norm(b18, b19 = 2) / math.sqrt(b18.shape[0])).item()
def fonk6(b16, b17):
    b16 = torch.from_numpy(b16)
    b17 = torch.from_numpy(b17)
    b18 = b16 - b17
    return (torch.norm(b18, b19 = 1) / b18.shape[0]).item()
def fonk7(b16, b17):
    b16 = torch.from_numpy(b16)
    b17 = torch.from_numpy(b17)
    b18 = torch.abs(b16 - b17)
    return torch.median(b18 - torch.median(b18)).item()
def fonk8(b16, b17):
    b16 = torch.from_numpy(b16)
    b17 = torch.from_numpy(b17)
    b20 = torch.mean(b17)
    b21 = torch.pow(b17 - b20, 2).sum()
    b22 = torch.pow(b16 - b17, 2).sum()
    return 1 - (b22 / b21).item()
def fonk9(b27):
    b5, data_train, data_val, data_test, b7, b8, b4 = fonk4(b27)
    b23 = np.min(b7)
    features_train, b7 = fonk3(data_train, b7, b27)
    features_test, b4 = fonk3(data_test, b4, b27)
    b7 -= b23
    b4 -= b23
    b24 = np.zeros_like(b4)
    for i in range(b7.shape[1]):
        b25 = xgb.XGBRegressor(max_depth=10, learning_rate=0.001, n_estimators=200, verbosity=1, objective="reg:gamma")
        b25.fit(features_train, b7[:, i])
        b24[:, i] = b25.predict(features_test)
        with open(f'XGBRegressor_{i}.pkl', 'wb') as f:
            pickle.dump(b25, f)
    print("RMSE: ", fonk5(b24.reshape(-1), b4.reshape(-1)))
    print("MAE: ", fonk6(b24.reshape(-1), b4.reshape(-1)))
    print("MAD: ", fonk7(b24.reshape(-1), b4.reshape(-1)))
    print("R2: ", fonk8(b24.reshape(-1), b4.reshape(-1)))
if b26 = = "__main__":
    b27 = fonk1()
    fonk9(b27)