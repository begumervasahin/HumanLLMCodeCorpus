import torch
import torch.nn as nn
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from torch.utils.data import DataLoader, Dataset
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error
from visdom import Visdom
torch.manual_seed(1234)
np.random.seed(1234)
LR = 0.001
EPOCHS = 5
BATCH = 256
WINDOWS_LENGTH = 24
HIDDEN_SIZE = 64
PREDICTION_LENGTH = 24
TS_FEATURE = 1
RNN_INPUT_FEATURES = 8
TRAIN_PROP = 0.8
SILD_STEP = 1
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
def generate_sample(dataset, in_seq_len, out_seq_len, slid_step=1):
    samples = []
    step = slid_step
    valid_len = dataset.shape[0] - in_seq_len - out_seq_len + 1
    for i in range(0, valid_len, step):
        time_step = dataset[i:i + in_seq_len, 0]
        enc_seqs = dataset[i:i + in_seq_len, 1]
        dec_output_seqs = dataset[i + in_seq_len:i + in_seq_len + out_seq_len, 1]
        samples.append([time_step, enc_seqs, dec_output_seqs])
    return np.array(samples)
def calc_rmse(real, pred):
    return np.sqrt(mean_squared_error(real, pred))
def calc_mae(real, pred):
    return mean_absolute_error(real, pred)
def calc_mape(real, pred, epsilon=1E-7):
    real += epsilon
    return np.sum(np.abs((real - pred) / real)) / len(real) * 100
def calc_smape(real, pred):
    denom = (np.abs(real) + np.abs(pred)) / 2.0
    return np.sum(np.abs((real - pred) / denom)) / len(real) * 100
class CustomDataset(Dataset):
    def __init__(self, values):
        self.raw_data = values
        self.length = self.raw_data.shape[0]
    def __len__(self):
        return self.length
    def __getitem__(self, index):
        idx = index % self.length
        data = self.raw_data[idx]
        time_step, enc_seqs, dec_output_seqs = data[0].astype(np.float32), data[1].astype(np.float32), data[2].astype(np.float32)
        return time_step, enc_seqs, dec_output_seqs
class MLPAttention(nn.Module):
    def __init__(self, q_size, k_size, attn_size, bias=True, dropout=0.):
        super(MLPAttention, self).__init__()
        self.Wq = nn.Linear(q_size, attn_size, bias=bias)
        self.Wk = nn.Linear(k_size, attn_size, bias=bias)
        self.dropout = nn.Dropout(dropout)
    def forward(self, q, k, v):
        q = self.Wq(q)
        k = self.Wk(k)
        scores = torch.matmul(q, k.transpose(-2, -1))
        weights = self.dropout(torch.softmax(scores, dim=-1))
        atten_value = torch.bmm(weights, v)
        return atten_value, weights
class Seq2SeqPred(nn.Module):
    def __init__(self, ts_features, rnn_input_features, hidden_size, out_seq_len, use_pe=False, use_atten=False):
        super(Seq2SeqPred, self).__init__()
        self.input_size = ts_features
        self.hidden_size = hidden_size
        self.out_seq_len = out_seq_len
        self.rnn_input_size = rnn_input_features
        self.use_pe = use_pe
        self.use_attention = use_atten
        self.embed = nn.Linear(self.input_size, self.rnn_input_size)
        self.encoder = nn.LSTMCell(self.rnn_input_size, self.hidden_size)
        self.out_linear = nn.Linear(self.hidden_size, 1)
        if self.use_attention:
            self.attention = MLPAttention(hidden_size, hidden_size, hidden_size)
            self.decoder = nn.LSTMCell(self.hidden_size + self.hidden_size, self.hidden_size)
        else:
            self.decoder = nn.LSTMCell(self.hidden_size, self.hidden_size)
        if self.use_pe:
            self.time_embed = nn.Linear(self.input_size, self.rnn_input_size)
    def forward(self, enc_inputs, timestep=None):
        enc_inputs = self.embed(enc_inputs.unsqueeze(-1))
        if self.use_pe:
            enc_inputs = enc_inputs + self.time_embed(timestep.unsqueeze(-1))
        batch = enc_inputs.shape[0]
        in_hx, in_cx = torch.zeros(batch, self.hidden_size).to(device), torch.zeros(batch, self.hidden_size).to(device)
        out_seqs = []
        in_hxs = []
        for in_step in range(enc_inputs.shape[1]):
            in_hx, in_cx = self.encoder(enc_inputs[:, in_step, :], (in_hx, in_cx))
            if self.use_attention:
                in_hxs.append(in_hx)
        out_hx = in_hx
        out_cx = in_cx
        if self.use_attention:
            in_hxs = torch.stack(in_hxs, dim=1)
        for _ in range(self.out_seq_len):
            if self.use_attention:
                context, _ = self.attention(out_hx.unsqueeze(1), in_hxs, in_hxs)
                dec_input_i = torch.cat((out_hx, context.squeeze(1)), dim=-1)
            else:
                dec_input_i = out_hx
            out_hx, out_cx = self.decoder(dec_input_i, (out_hx, out_cx))
            out_seqs.append(out_hx)
        outs = self.out_linear(torch.stack(out_seqs, dim=1)).squeeze()
        return outs
    def plot_prediction_result(self, preds, real):
        plt.figure(figsize=(16, 2 * 2))
        plt.plot(preds, color="r", label="test prediction")
        plt.plot(real, color='b', label="ground truth")
        plt.legend(loc="best")
        plt.show()
    def calculate_metrics(self, real, pred):
        real = np.array(real)
        pred = np.array(pred)
        return calc_rmse(real, pred), calc_mae(real, pred), calc_mape(real, pred), calc_smape(real, pred)
if __name__ == '__main__':
    viz = Visdom()
    viz.line([[0., 0.]], [0.], win="train_loss", opts=dict(title="train loss ,val loss", legend=["train loss", "val loss"]))
    train_file_path = "pollution.csv"
    training = pd.read_csv(train_file_path).values