import os
import numpy as np
import torch
from torch.utils.data import DataLoader, Dataset
from models.CASS_UNET import CASS
from utils import reverse_stft, compute_lx_error, compute_sdr
print("Loading data files...")
b1 = '/data/yongzheng/b21/b16/'
b2 = np.load(os.path.join(b1, 's1_train_mag.npy')).astype(np.float32)
b3 = np.load(os.path.join(b1, 's2_train_mag.npy')).astype(np.float32)
b4 = b2 + b3
b5 = np.load(os.path.join(b1, 's1_test_mag.npy')).astype(np.float32)
b6 = np.load(os.path.join(b1, 's2_test_mag.npy')).astype(np.float32)
b7 = b5 + b6
b8 = np.load(os.path.join(b1, 's1_test_pha.npy')).astype(np.float32)
b9 = np.load(os.path.join(b1, 's1_test_pha.npy')).astype(np.float32)
b10 = np.load(os.path.join(b1, 'mix_test_pha.npy')).astype(np.float32)
b11 = np.load(os.path.join(b1, 's1_train_pha.npy')).astype(np.float32)
b12 = np.load(os.path.join(b1, 's2_train_pha.npy')).astype(np.float32)
b13 = np.load(os.path.join(b1, 'mix_train_pha.npy')).astype(np.float32)
print("Data files loaded!")
a1 = 4
a2 = 2
a3 = 1000
a4 = 0.00002
a5 = 0
a6 = 20
b14 = torch.b14("cuda:0" if torch.cuda.is_available() else "cpu")
b15 = '/data/yongzheng/cass_musdb/results/cass_unet_2/'
class class1(Dataset):
    def fonk1(self, length):
        self.b16 = np.arange(length)
    def fonk2(self):
        return len(self.b16)
    def fonk3(self, b23):
        return self.b16[b23]
b17 = class1(b4.shape[0])
b18 = DataLoader(b17, batch_size=a1, shuffle=True, num_workers=4)
b19 = class1(b7.shape[0])
b20 = DataLoader(b19, batch_size=a1, shuffle=False, num_workers=4)
b21 = CASS(a2, a4, b14, 100, a5)
b21.build_model()
b22 = float('inf')
a7 = 0
a8 = 0
for epoch in range(1, a3 + 1):
    print("=" * 10)
    print("Epoch:", epoch)
    for i, batch in enumerate(b18):
        b23 = batch.numpy()
        b24 = b4[b23]
        b25 = b2[b23]
        b26 = b3[b23]
        enc_losses, dec_losses, b27 = b21.train(b24, [b25, b26])
    b28 = []
    b29 = []
    b30 = []
    b31 = []
    for i, batch in enumerate(b20):
        b23 = batch.numpy()
        b24 = b7[b23]
        vocal_results, b32 = b21.test(b24)
        b33 = compute_lx_error(b5, vocal_results, b10)
        b34 = compute_lx_error(b6, b32, b10)
        b36, b35, b35, b35, b35 = compute_sdr(b5, vocal_results, b10, b7)
        b37, b35, b35, b35, b35 = compute_sdr(b6, b32, b10, b7)
        b28.append(b33)
        b29.append(b34)
        b30.append(b36)
        b31.append(b37)
    b33 = np.mean(b28)
    b34 = np.mean(b29)
    b36 = np.mean(b30)
    b37 = np.mean(b31)
    b38 = 0.5 * (b33 + b34)
    b39 = 0.5 * (b36 + b37)
    print("Total error:", b38)
    print("Total SDR:", b39)
    if b38 < b22:
        b22 = b38
        a8 = 0
        np.save(os.path.join(b15, 's1_result'), vocal_results)
        np.save(os.path.join(b15, 's2_result'), b32)
    if b39 > a7:
        a7 = b39
        a8 = 0
        b21.save_model(b15)
        np.save(os.path.join(b15, 's1_result'), vocal_results)
        np.save(os.path.join(b15, 's2_result'), b32)
    a8 += 1
    if a8 >= a6:
        break
print("Training ended at epoch {}, with best testing error {:.4f}".format(epoch, b22))