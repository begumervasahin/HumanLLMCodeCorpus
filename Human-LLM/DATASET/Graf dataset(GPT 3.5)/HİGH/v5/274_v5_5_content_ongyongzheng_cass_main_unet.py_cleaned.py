import os
import numpy as np
import torch
from torch.utils.data import DataLoader, Dataset
from models.UNET_final import UNET
from utils import compute_lx_error, compute_sdr
print("Loading data files...")
b1 = '/data/yongzheng/cass/b13/'
b2 = np.load(os.path.join(b1, 's1_train_mag.npy')).astype(np.float32)
b3 = np.load(os.path.join(b1, 's2_train_mag.npy')).astype(np.float32)
b4 = b2 + b3
b5 = np.load(os.path.join(b1, 's1_test_mag.npy')).astype(np.float32)
b6 = np.load(os.path.join(b1, 's2_test_mag.npy')).astype(np.float32)
b7 = b5 + b6
b8 = np.load(os.path.join(b1, 's1_test_pha.npy')).astype(np.float32)
b9 = np.load(os.path.join(b1, 's1_test_pha.npy')).astype(np.float32)
b10 = np.load(os.path.join(b1, 'mix_test_pha.npy')).astype(np.float32)
print("Data files loaded!")
a1 = 4
a2 = 2
a3 = 1000
a4 = 20
a5 = 0.00002
a6 = 1e-5
b11 = torch.b11("cuda:0" if torch.cuda.is_available() else "cpu")
b12 = '/data/yongzheng/cass_musdb/results/b18/'
class class1(Dataset):
    def fonk1(self, length):
        self.b13 = np.arange(length)
    def fonk2(self):
        return len(self.b13)
    def fonk3(self, idx):
        return self.b13[idx]
b14 = class1(len(b4))
b15 = DataLoader(b14, batch_size=a1, shuffle=True, num_workers=4)
b16 = class1(len(b7))
b17 = DataLoader(b16, batch_size=a1, shuffle=False, num_workers=4)
b18 = UNET(a2, a5, b11, 100, a6)
b18.build_model()
b19 = []
b20 = []
a7 = 0
a8 = 0
a9 = 0
for epoch in range(1, a3 + 1):
    a9 = epoch
    for i, batch in enumerate(b15):
        b21 = batch.numpy()
        b22 = b4[b21]
        b23 = b2[b21]
        b24 = b3[b21]
        b25 = b18.train(b22, [b23, b24])
    b26 = []
    b27 = []
    for i, batch in enumerate(b17):
        b21 = batch.numpy()
        b22 = b7[b21]
        b29, b28 = b18.test(b22)
        b26.append(b29)
        b27.append(b28)
    b29 = np.concatenate(b26, axis=0)
    b28 = np.concatenate(b27, axis=0)
    b30 = compute_lx_error(b5, b29, b10)
    b31 = compute_lx_error(b6, b28, b10)
    vocal_sdr, b32, b32, b32, b32 = compute_sdr(b5, b29, b10, b7)
    accom_sdr, b32, b32, b32, b32 = compute_sdr(b6, b28, b10, b7)
    b33 = 0.5 * (vocal_sdr + accom_sdr)
    print("=" * 10)
    print(f"Epoch {epoch}, vocal error: {b30:.4f}, accom error: {b31:.4f}")
    print(f"Curr Best: {a7:.4f}, Avg Error: {(b30 + b31) / 2:.4f}, Avg sdr: {b33:.4f}")
    print(f"     Vocal SDR: {vocal_sdr:.4f}, Accom SDR: {accom_sdr:.4f}")
    if b33 > a7:
        a7 = b33
        a8 = 0
        b18.save_model(b12)
        np.save(os.path.join(b12, 's1_result'), b29)
        np.save(os.path.join(b12, 's2_result'), b28)
    a8 += 1
    b19.append(b30)
    b20.append(b31)
    np.save(os.path.join(b12, 's1_error'), np.array(b19))
    np.save(os.path.join(b12, 's2_error'), np.array(b20))
    for key in b18.history.keys():
        np.save(os.path.join(b12, key), b18.history[key])
    if a8 >= a4:
        break
print(f"Training ended at epoch {a9}, with best testing SDR {a7:.4f}")