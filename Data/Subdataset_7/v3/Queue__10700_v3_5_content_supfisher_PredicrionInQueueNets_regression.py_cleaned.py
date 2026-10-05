import argparse
import numpy as np
import xgboost as xgb
import math
import torch
import pickle
from utils import load_dataset
def fonk1():
    b1 = argparse.ArgumentParser()
    b1.add_argument('--seed', b2 = int, default=42, help='Random seed.')
    b1.add_argument('--cuda', b3 = 'store_true', default=False)
    b1.add_argument('--file_head', b2 = str, default='svm', help='which regression b23 to use.')
    b1.add_argument('--epochs', b2 = int, default=200, help='Number of epochs to train.')
    b1.add_argument('--pre_len', b2 = int, default=10, help='the length of input data sequence.')
    b1.add_argument('--tar_len', b2 = int, default=3, help='the length of output target sequence.')
    b1.add_argument('--shuffle', b3 = 'store_true', default=True, help='whether to shuffle the dataset.')
    return b1.parse_args()
def fonk2(b26):
    b5, b6, features_train, features_val, features_test, \
        b7, b8, b4 = load_dataset(path="./simul_data")
    if b26.cuda:
        b5 = b5.cuda()
        b6 = b6.cuda()
    if len(b7.shape) == 1:
        b7 = b7.unsqueeze(1)
        b8 = b8.unsqueeze(1)
        b4 = b4.unsqueeze(1)
    print("features_train shape: ", features_train.shape)
    print("b7 shape: ", b7.shape)
    print("b5 shape: ", b5.shape)
    b26.b9 = b5.shape[0]
    b26.b10 = features_train.shape[-1]
    b26.b11 = b7.shape[-1]
    return b5, b6, features_train, features_val, features_test, \
           b7, b8, b4
def fonk3(features, targets, b26):
    b12 = np.zeros([features.shape[0] - b26.pre_len - b26.tar_len, b26.pre_len, features.shape[1]])
    b13 = np.zeros([b12.shape[0], b26.tar_len])
    if b26.shuffle:
        b14 = np.random.permutation(b12.shape[0])
    else:
        b14 = range(b12.shape[0])
    for j, id in enumerate(b14):
        b12[j, :, 0:-1] = features[id:id+b26.pre_len, 0:-1]
        b12[j, :, -1] = targets[id:id + b26.pre_len, 0]
        b13[j, :] = targets[id+b26.pre_len:id+b26.pre_len+b26.tar_len, 0]
    return b12.reshape(b12.shape[0], -1), b13
def fonk4(b26):
    b5, b6, features_train, features_val, features_test, \
    b7, b8, b4 = fonk2(b26)
    return b5, features_train.numpy(), features_val.numpy(), features_test.numpy(), \
           b7.numpy(), b8.numpy(), b4.numpy()
def fonk5(b15, b16):
    b15 = torch.from_numpy(b15)
    b16 = torch.from_numpy(b16)
    b17 = b15 - b16
    return (torch.norm(b17, b18 = 2) / math.sqrt(b17.shape[0])).item()
def fonk6(b15, b16):
    b15 = torch.from_numpy(b15)
    b16 = torch.from_numpy(b16)
    b17 = b15 - b16
    return (torch.norm(b17, b18 = 1) / b17.shape[0]).item()
def fonk7(b15, b16):
    b15 = torch.from_numpy(b15)
    b16 = torch.from_numpy(b16)
    b17 = b15 - b16
    b17 = torch.abs(b17 - torch.median(b17))
    return torch.median(b17).item()
def fonk8(b15, b16):
    b15 = torch.from_numpy(b15)
    b16 = torch.from_numpy(b16)
    b19 = torch.b19(b16)
    b20 = torch.pow(b15 - b16, 2).sum() / torch.pow(b16 - b19, 2).sum()
    return 1 - b20.item()
def fonk9(b26):
    b5, data_train, data_val, data_test, b7, b8, b4 = fonk4(b26)
    b21 = min(b7)
    features_train, b7 = fonk3(data_train, b7, b26)
    features_test, b4 = fonk3(data_test, b4, b26)
    b7 = b7 - b21
    b4 = b4 - b21
    b22 = np.zeros_like(b4)
    for i in range(b7.shape[1]):
        b23 = xgb.XGBRegressor(max_depth=10, learning_rate=0.001,
                                 b24 = 200, silent=True, objective="reg:gamma")
        b23.fit(features_train, b7[:, i])
        b23.score(features_test, b4[:, i])
        b22[:, i] = b23.predict(features_test)
        with open('XGBRegressor'+str(i)+'.pkl', 'wb') as f:
            pickle.dump(b23, f)
    print("RMSE: ", fonk5(b22.reshape(-1), b4.reshape(-1)))
    print("MAE: ", fonk6(b22.reshape(-1), b4.reshape(-1)))
    print("MAD: ", fonk7(b22.reshape(-1), b4.reshape(-1)))
    print("R2: ", fonk8(b22.reshape(-1), b4.reshape(-1)))
if b25 = = "__main__":
    b26 = fonk1()
    fonk9(b26)