import os
import numpy as np
import torch
from torch.utils.data import DataLoader, Dataset
from models.CASS_UNET import CASS
from utils import reverse_stft, compute_lx_error, compute_sdr
print("Loading data files...")
b1 = '/data/yongzheng/b18/b13/'
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
a4 = 0.00002
a5 = 0
a6 = 20
b11 = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
b12 = '/data/yongzheng/cass_musdb/results/cass_unet_2/'
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
b18 = CASS(a2, a4, b11, 100, a5)
b18.build_model()
b19 = float('inf')
a7 = 0
a8 = 0
for epoch in range(1, a3 + 1):
    print("=" * 10)
    print("Epoch:", epoch)
    for i, batch in enumerate(b15):
        b20 = batch.numpy()
        b21 = b4[b20]
        b22 = b2[b20]
        b23 = b3[b20]
        enc_losses, dec_losses, b24 = b18.train(b21, [b22, b23])
    b25 = []
    b26 = []
    b27 = []
    b28 = []
    for i, batch in enumerate(b17):
        b20 = batch.numpy()
        b21 = b7[b20]
        vocal_results, b29 = b18.test(b21)
        b30 = compute_lx_error(b5, vocal_results, b10)
        b31 = compute_lx_error(b6, b29, b10)
        b33, b32, b32, b32, b32 = compute_sdr(b5, vocal_results, b10, b7)
        b34, b32, b32, b32, b32 = compute_sdr(b6, b29, b10, b7)
        b25.append(b30)
        b26.append(b31)
        b27.append(b33)
        b28.append(b34)
    b30 = np.mean(b25)
    b31 = np.mean(b26)
    b33 = np.mean(b27)
    b34 = np.mean(b28)
    b35 = 0.5 * (b30 + b31)
    b36 = 0.5 * (b33 + b34)
    print("Total error:", b35)
    print("Total SDR:", b36)
    if b35 < b19:
        b19 = b35
        a8 = 0
        np.save(os.path.join(b12, 's1_result'), vocal_results)
        np.save(os.path.join(b12, 's2_result'), b29)
    if b36 > a7:
        a7 = b36
        a8 = 0
        b18.save_model(b12)
        np.save(os.path.join(b12, 's1_result'), vocal_results)
        np.save(os.path.join(b12, 's2_result'), b29)
    a8 += 1
    if a8 >= a6:
        break
print("Training ended at epoch {}, with best testing error {:.4f}".format(epoch, b19))