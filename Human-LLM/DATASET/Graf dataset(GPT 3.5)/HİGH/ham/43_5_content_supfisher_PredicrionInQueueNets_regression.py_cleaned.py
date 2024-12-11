import argparse
from utils import *
import xgboost as xgb
from xgboost import plot_importance
from matplotlib import pyplot as plt
import numpy as np
from scipy import sparse
from sklearn.metrics import make_scorer
from sklearn.svm import SVR
import pickle
b1 = argparse.ArgumentParser()
b1.add_argument('--seed', b2 = int, default=42, b4='Random seed.')
b1.add_argument('--cuda', b3 = 'store_true', default=False)
b1.add_argument('--file_head', b2 = str, default='svm',
                    b4 = 'which regression b24 to use.')
b1.add_argument('--epochs', b2 = int, default=200,
                    b4 = 'Number of epochs to train.')
b1.add_argument('--pre_len', b2 = int, default=10,
                    b4 = 'the length of input data sequence.')
b1.add_argument('--tar_len', b2 = int, default=3,
                    b4 = 'the length of output target sequence.')
b1.add_argument('--shuffle', b3 = 'store_true', default=True,
                    b4 = 'whether to shuffle the dataset.')
def fonk1(b27):
    b6, b7, features_train, features_val, features_test, \
        b8, b9, b5 = load_dataset(path="./simul_data")
    if b27.cuda:
        b6 = b6.cuda()
        b7 = b7.cuda()
    if len(b8.shape) == 1:
        b8 = b8.unsqueeze(1)
        b9 = b9.unsqueeze(1)
        b5 = b5.unsqueeze(1)
    print("featues_train shape: ", features_train.shape)
    print("b8 shape: ", b8.shape)
    print("b6 shape: ", b6.shape)
    b27.b10 = b6.shape[0]
    b27.b11 = features_train.shape[-1]
    b27.b12 = b8.shape[-1]
    return b6, b7, features_train, features_val, features_test, \
           b8, b9, b5
def fonk2(features, targets, b27):
    b13 = np.zeros([features.shape[0] - b27.pre_len - b27.tar_len, b27.pre_len, features.shape[1]])
    b14 = np.zeros([b13.shape[0], b27.tar_len])
    if b27.shuffle:
        b15 = np.random.permutation(b13.shape[0])
    else:
        b15 = range(b13.shape[0])
    for j, id in enumerate(b15):
        b13[j, :, 0:-1] = features[id:id+b27.pre_len, 0:-1]
        b13[j, :, -1] = targets[id:id + b27.pre_len, 0]
        b14[j, :] = targets[id+b27.pre_len:id+b27.pre_len+b27.tar_len, 0]
    return b13.reshape(b13.shape[0], -1), b14
def fonk3(b27):
    b6, b7, features_train, features_val, features_test, \
    b8, b9, b5 = fonk1(b27)
    return b6, features_train.numpy(), features_val.numpy(), features_test.numpy(), \
           b8.numpy(), b9.numpy(), b5.numpy()
def fonk4(b16, b17):
    b16 = torch.from_numpy(b16)
    b17 = torch.from_numpy(b17)
    b18 = b16 - b17
    return (torch.norm(b18, b19 = 2)/math.sqrt(b18.shape[0])).item()
def fonk5(b16, b17):
    b16 = torch.from_numpy(b16)
    b17 = torch.from_numpy(b17)
    b18 = b16 - b17
    return (torch.norm(b18, b19 = 1)/b18.shape[0]).item()
def fonk6(b16, b17):
    b16 = torch.from_numpy(b16)
    b17 = torch.from_numpy(b17)
    b18 = b16 - b17
    b18 = torch.abs(b18 - torch.median(b18))
    return torch.median(b18).item()
def fonk7(b16, b17):
    b16 = torch.from_numpy(b16)
    b17 = torch.from_numpy(b17)
    b20 = torch.mean(b17)
    b21 = torch.pow(b16-b17, 2).sum()/torch.pow(b17-b20, 2).sum()
    return 1-b21.item()
def fonk8(b27):
    b6, data_train, data_val, data_test, b8, b9, b5 = fonk3(b27)
    b22 = min(b8)
    features_train, b8 = fonk2(data_train, b8, b27)
    features_test, b5 = fonk2(data_test, b5, b27)
    b8 = b8 - b22
    b5 = b5 - b22
    b23 = np.zeros_like(b5)
    for i in range(b8.shape[1]):
        b24 = xgb.XGBRegressor(max_depth=10, learning_rate=0.001,
                                 b25 = 200, silent=True, objective="reg:gamma")
        b24.fit(features_train, b8[:, i])
        b24.score(features_test, b5[:, i])
        b23[:, i] = b24.predict(features_test)
        with open('XGBRegressor'+str(i)+'.pkl', 'wb') as f:
            pickle.dump(b24, f)
    print("RMSE: ", fonk4(b23.reshape(-1), b5.reshape(-1)))
    print("MAE: ", fonk5(b23.reshape(-1), b5.reshape(-1)))
    print("MAD: ", fonk6(b23.reshape(-1), b5.reshape(-1)))
    print("R2: ", fonk7(b23.reshape(-1), b5.reshape(-1)))
if b26 = = "__main__":
    b27 = b1.parse_args()
    fonk8(b27)