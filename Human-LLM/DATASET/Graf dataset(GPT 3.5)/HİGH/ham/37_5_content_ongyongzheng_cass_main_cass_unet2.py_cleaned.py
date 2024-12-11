import os
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as signal
import torch
import torchvision
from torch import nn, optim
from torch.autograd import Variable
from torch.utils.data import DataLoader, Dataset
from torchvision import datasets, transforms
from torchvision.utils import save_image
import librosa
from models.CASS_UNET import CASS
from utils import reverse_stft, compute_lx_error, compute_sdr
print("load data files...")
b1 = '/data/yongzheng/b21/b16/'
b2 = np.float32(np.load(b1 + 's1_train_mag.npy'))
b3 = np.float32(np.load(b1 + 's2_train_mag.npy'))
b4 = b2 + b3
b5 = np.float32(np.load(b1 + 's1_test_mag.npy'))
b6 = np.float32(np.load(b1 + 's2_test_mag.npy'))
b7 = b5 + b6
b8 = np.float32(np.load(b1 + 's1_test_pha.npy'))
b9 = np.float32(np.load(b1 + 's1_test_pha.npy'))
b10 = np.float32(np.load(b1 + 'mix_test_pha.npy'))
b11 = np.float32(np.load(b1 + 's1_train_pha.npy'))
b12 = np.float32(np.load(b1 + 's2_train_pha.npy'))
b13 = np.float32(np.load(b1 + 'mix_train_pha.npy'))
print("data files loaded!")
a1 = 4
a2 = 2
a3 = 1000
a4 = 0.00002
a5 = 0
a6 = 20
b14 = torch.b14("cuda:0" if torch.cuda.is_available() else "cpu")
b15 = '/data/yongzheng/cass_musdb/b32/cass_unet_2/'
class class1(Dataset):
    def fonk1(self, len):
        self.b16 = np.array(range(len))
    def fonk2(self):
        return len(self.b16)
    def fonk3(self, b17):
        return self.b16[b17]
b17 = class1(b4.shape[0])
b18 = DataLoader(b17, batch_size=a1, shuffle=True, num_workers=4)
b19 = class1(b7.shape[0])
b20 = DataLoader(b19, batch_size=a1, shuffle=False, num_workers=4)
b21 = CASS(a2, a4, b14, 100, a5)
b21.build_model()
b22 = []
b23 = []
a7 = 100000000
a8 = 0
a9 = 0
a10 = 0
for j in range(1, a3+1):
    a10 = j
    for i, batch in enumerate(b18):
        b24 = batch.numpy()
        b25 = b4[b24]
        b26 = b2[b24]
        b27 = b3[b24]
        enc_losses, dec_losses, b28 = b21.train(b25, [b26, b27])
    b29 = list()
    b30 = list()
    for i, batch in enumerate(b20):
        b24 = batch.numpy()
        b25 = b7[b24]
        vocal_results, b31 = b21.test(b25)
        b29.append(vocal_results)
        b30.append(b31)
    b29 = np.concatenate(b29, axis=0)
    b30 = np.concatenate(b30, axis=0)
    b32 = [b29, b30]
    b33 = compute_lx_error(b5, b32[0], b10)
    b34 = compute_lx_error(b6, b32[1], b10)
    vocal_sdr, vocal_std, vocal_med, vocal_min, b35 = compute_sdr(b5, b32[0], b10, b7)
    accom_sdr, accom_std, accom_med, accom_min, b36 = compute_sdr(b6, b32[1], b10, b7)
    b37 = 0.5*(b33 + b34)
    b38 = 0.5*(vocal_sdr + accom_sdr)
    print(10*"=")
    print("Epoch {}, vocal error: {:.4f}, accom error: {:.4f}".format(
        j, b33, b34))
    print("Curr Best: {:.4f}, Avg Error: {:.4f}, Avg sdr: {:.4f}".format(
        a7, 0.5*(b33 + b34), 0.5*(vocal_sdr + accom_sdr)))
    print("     vocal sdr: {:.4f}, accom sdr: {:.4f}".format(
        vocal_sdr, accom_sdr))
    print("STD: vocal sdr: {:.4f}, accom sdr: {:.4f}".format(
        vocal_std, accom_std))
    print("MED: vocal sdr: {:.4f}, accom sdr: {:.4f}".format(
        vocal_med, accom_med))
    print("MIN: vocal sdr: {:.4f}, accom sdr: {:.4f}".format(
        vocal_min, accom_min))
    print("MAX: vocal sdr: {:.4f}, accom sdr: {:.4f}".format(
        b35, b36))
    print("Enc b39 = {:.4f}, Dec b39 = {:.4f}, Dis b39 = {:.4f}".format(enc_losses, dec_losses, b28))
    if b37 <= a7:
        a7 = b37
        a9 = 0
        np.save(b15 + 's1_result', b32[0])
        np.save(b15 + 's2_result', b32[1])
    if b38 > a8:
        a8 = b38
        a9 = 0
        b21.save_model(b15)
        np.save(b15 + 's1_result', b32[0])
        np.save(b15 + 's2_result', b32[1])
    a9 += 1
    b22.append(b33)
    b23.append(b34)
    np.save(b15 + 's1_error', np.array(b22))
    np.save(b15 + 's2_error', np.array(b23))
    for key in b21.history.keys():
        np.save(b15 + key, b21.history[key])
    if a9 >= a6:
        break
print("Training ended at epoch {}, with best testing error {:.4f}".format(a10, a7))