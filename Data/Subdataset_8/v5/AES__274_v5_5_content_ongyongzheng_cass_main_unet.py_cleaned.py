import os
import numpy as np
import torch
from torch.utils.data import DataLoader, Dataset
from models.UNET_final import UNET
from utils import compute_lx_error, compute_sdr
print("Loading data files...")
data_dir = '/data/yongzheng/cass/samples/'
stft_vocal_train = np.load(os.path.join(data_dir, 's1_train_mag.npy')).astype(np.float32)
stft_accom_train = np.load(os.path.join(data_dir, 's2_train_mag.npy')).astype(np.float32)
stft_mix_train = stft_vocal_train + stft_accom_train
stft_vocal_test = np.load(os.path.join(data_dir, 's1_test_mag.npy')).astype(np.float32)
stft_accom_test = np.load(os.path.join(data_dir, 's2_test_mag.npy')).astype(np.float32)
stft_mix_test = stft_vocal_test + stft_accom_test
stft_vocal_test_phase = np.load(os.path.join(data_dir, 's1_test_pha.npy')).astype(np.float32)
stft_accom_test_phase = np.load(os.path.join(data_dir, 's1_test_pha.npy')).astype(np.float32)
stft_mix_test_pha = np.load(os.path.join(data_dir, 'mix_test_pha.npy')).astype(np.float32)
print("Data files loaded!")
BATCH_SIZE = 4
NUM_NETWORKS = 2
NUM_EPOCHS = 1000
threshold = 20
learning_rate = 0.00002
weight_decay = 1e-5
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
save_dir = '/data/yongzheng/cass_musdb/results/unet/'
class IndexDataset(Dataset):
    def __init__(self, length):
        self.samples = np.arange(length)
    def __len__(self):
        return len(self.samples)
    def __getitem__(self, idx):
        return self.samples[idx]
train_dataset = IndexDataset(len(stft_mix_train))
train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True, num_workers=4)
test_dataset = IndexDataset(len(stft_mix_test))
test_loader = DataLoader(test_dataset, batch_size=BATCH_SIZE, shuffle=False, num_workers=4)
unet = UNET(NUM_NETWORKS, learning_rate, device, 100, weight_decay)
unet.build_model()
vocal_errors = []
accom_errors = []
best_sdr = 0
counter = 0
curr_epoch = 0
for epoch in range(1, NUM_EPOCHS + 1):
    curr_epoch = epoch
    for i, batch in enumerate(train_loader):
        indices = batch.numpy()
        x = stft_mix_train[indices]
        a = stft_vocal_train[indices]
        b = stft_accom_train[indices]
        loss = unet.train(x, [a, b])
    vocal_results_list = []
    accom_results_list = []
    for i, batch in enumerate(test_loader):
        indices = batch.numpy()
        x = stft_mix_test[indices]
        vocal_results, accom_results = unet.test(x)
        vocal_results_list.append(vocal_results)
        accom_results_list.append(accom_results)
    vocal_results = np.concatenate(vocal_results_list, axis=0)
    accom_results = np.concatenate(accom_results_list, axis=0)
    vocal_error = compute_lx_error(stft_vocal_test, vocal_results, stft_mix_test_pha)
    accom_error = compute_lx_error(stft_accom_test, accom_results, stft_mix_test_pha)
    vocal_sdr, _, _, _, _ = compute_sdr(stft_vocal_test, vocal_results, stft_mix_test_pha, stft_mix_test)
    accom_sdr, _, _, _, _ = compute_sdr(stft_accom_test, accom_results, stft_mix_test_pha, stft_mix_test)
    curr_sdr = 0.5 * (vocal_sdr + accom_sdr)
    print("=" * 10)
    print(f"Epoch {epoch}, vocal error: {vocal_error:.4f}, accom error: {accom_error:.4f}")
    print(f"Curr Best: {best_sdr:.4f}, Avg Error: {(vocal_error + accom_error) / 2:.4f}, Avg sdr: {curr_sdr:.4f}")
    print(f"     Vocal SDR: {vocal_sdr:.4f}, Accom SDR: {accom_sdr:.4f}")
    if curr_sdr > best_sdr:
        best_sdr = curr_sdr
        counter = 0
        unet.save_model(save_dir)
        np.save(os.path.join(save_dir, 's1_result'), vocal_results)
        np.save(os.path.join(save_dir, 's2_result'), accom_results)
    counter += 1
    vocal_errors.append(vocal_error)
    accom_errors.append(accom_error)
    np.save(os.path.join(save_dir, 's1_error'), np.array(vocal_errors))
    np.save(os.path.join(save_dir, 's2_error'), np.array(accom_errors))
    for key in unet.history.keys():
        np.save(os.path.join(save_dir, key), unet.history[key])
    if counter >= threshold:
        break
print(f"Training ended at epoch {curr_epoch}, with best testing SDR {best_sdr:.4f}")