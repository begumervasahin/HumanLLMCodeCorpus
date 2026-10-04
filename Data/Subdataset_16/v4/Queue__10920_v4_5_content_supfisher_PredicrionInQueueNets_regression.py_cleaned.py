import argparse
import pickle
import numpy as np
import xgboost as xgb
from xgboost import plot_importance
from matplotlib import pyplot as plt
from scipy import sparse
from sklearn.metrics import make_scorer
from sklearn.svm import SVR
import torch
import math
from utils import load_dataset
def fonk1():
    b1 = argparse.ArgumentParser()
    b1.add_argument('--seed', b2 = int, default=42, help='Random seed.')
    b1.add_argument('--cuda', b3 = 'store_true', default=False)
    b1.add_argument('--file_head', b2 = str, default='svm', help='Which regression b19 to use.')
    b1.add_argument('--epochs', b2 = int, default=200, help='Number of epochs to train.')
    b1.add_argument('--pre_len', b2 = int, default=10, help='Length of input data sequence.')
    b1.add_argument('--tar_len', b2 = int, default=3, help='Length of output target sequence.')
    b1.add_argument('--shuffle', b3 = 'store_true', default=True, help='Whether to shuffle the dataset.')
    return b1.parse_args()
def fonk2(b21):
    b5, b6, features_train, features_val, features_test, b7, b8, b4 = load_dataset(path="./simul_data")
    if b21.cuda:
        b5 = b5.cuda()
        b6 = b6.cuda()
    if len(b7.shape) == 1:
        b7 = b7.unsqueeze(1)
        b8 = b8.unsqueeze(1)
        b4 = b4.unsqueeze(1)
    print("Features train shape: ", features_train.shape)
    print("Targets train shape: ", b7.shape)
    print("Adjacency shape: ", b5.shape)
    b21.b9 = b5.shape[0]
    b21.b10 = features_train.shape[-1]
    b21.b11 = b7.shape[-1]
    return b5, b6, features_train, features_val, features_test, b7, b8, b4
def fonk3(features, targets, b21):
    b12 = np.zeros((features.shape[0] - b21.pre_len - b21.tar_len, b21.pre_len, features.shape[1]))
    b13 = np.zeros((b12.shape[0], b21.tar_len))
    b14 = np.random.permutation(b12.shape[0]) if b21.shuffle else range(b12.shape[0])
    for j, id in enumerate(b14):
        b12[j, :, 0:-1] = features[id:id + b21.pre_len, 0:-1]
        b12[j, :, -1] = targets[id:id + b21.pre_len, 0]
        b13[j, :] = targets[id + b21.pre_len:id + b21.pre_len + b21.tar_len, 0]
    return b12.reshape(b12.shape[0], -1), b13
def fonk4(b21):
    b5, b6, features_train, features_val, features_test, b7, b8, b4 = fonk2(b21)
    return b5, features_train.numpy(), features_val.numpy(), features_test.numpy(), b7.numpy(), b8.numpy(), b4.numpy()
def fonk5(b15, b16):
    b15 = torch.from_numpy(b15)
    b16 = torch.from_numpy(b16)
    return torch.sqrt(torch.mean((b15 - b16) ** 2)).item()
def fonk6(b15, b16):
    b15 = torch.from_numpy(b15)
    b16 = torch.from_numpy(b16)
    return torch.mean(torch.abs(b15 - b16)).item()
def fonk7(b15, b16):
    b15 = torch.from_numpy(b15)
    b16 = torch.from_numpy(b16)
    return torch.median(torch.abs(b15 - b16 - torch.median(b15 - b16))).item()
def fonk8(b15, b16):
    b15 = torch.from_numpy(b15)
    b16 = torch.from_numpy(b16)
    return 1 - torch.sum((b15 - b16) ** 2) / torch.sum((b16 - torch.mean(b16)) ** 2).item()
def fonk9(b21):
    b5, data_train, data_val, data_test, b7, b8, b4 = fonk4(b21)
    b17 = min(b7)
    features_train, b7 = fonk3(data_train, b7, b21)
    features_test, b4 = fonk3(data_test, b4, b21)
    b7 -= b17
    b4 -= b17
    b18 = np.zeros_like(b4)
    for i in range(b7.shape[1]):
        b19 = xgb.XGBRegressor(max_depth=10, learning_rate=0.001, n_estimators=200, objective="reg:gamma", verbosity=0)
        b19.fit(features_train, b7[:, i])
        b18[:, i] = b19.predict(features_test)
        with open(f'XGBRegressor{i}.pkl', 'wb') as f:
            pickle.dump(b19, f)
    print("RMSE: ", fonk5(b18.reshape(-1), b4.reshape(-1)))
    print("MAE: ", fonk6(b18.reshape(-1), b4.reshape(-1)))
    print("MAD: ", fonk7(b18.reshape(-1), b4.reshape(-1)))
    print("R2: ", fonk8(b18.reshape(-1), b4.reshape(-1)))
if b20 = = "__main__":
    b21 = fonk1()
    fonk9(b21)